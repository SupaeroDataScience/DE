import base64
import io
import random
from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import numpy as np
import requests
import streamlit as st
from PIL import Image
from PIL import ImageDraw, ImageFont
from pydantic import BaseModel

# ---- Functions ---


class Detection(BaseModel):
    x_min: int
    y_min: int
    x_max: int
    y_max: int
    class_name: str
    confidence: float


class Result(BaseModel):
    detections: List[Detection] = []
    time: float = 0.0
    model: str


@st.cache(show_spinner=True)
def make_dummy_request(model_url: str, model: str, image: Image) -> Result:
    """
    This simulates a fake answer for you to test your application without having access to any other input from other teams
    """
    # We do a dummy encode and decode pass to check that the file is correct
    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG")
        buffer: str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        data = {"model": model, "image": buffer}

    # We do a dummy decode
    _image = data.get("image")
    _image = _image.encode("utf-8")
    _image = base64.b64decode(_image)
    _image = Image.open(io.BytesIO(_image))  # type: Image
    if _image.mode == "RGBA":
        _image = _image.convert("RGB")

    _model = data.get("model")

    # We generate a random prediction
    w, h = _image.size

    detections = [
        Detection(
            x_min=random.randint(0, w // 2 - 1),
            y_min=random.randint(0, h // 2 - 1),
            x_max=random.randint(w // w, w - 1),
            y_max=random.randint(h // 2, h - 1),
            class_name="dummy",
            confidence=round(random.random(), 3),
        )
        for _ in range(random.randint(1, 10))
    ]

    # We return the result
    result = Result(time=0.1, model=_model, detections=detections)

    return result


@st.cache(show_spinner=True)
def make_request(model_url: str, model: str, image: Image) -> Result:
    """
    Process our data and send a proper request
    """
    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG")
        buffer: str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        data = {"model": model, "image": buffer}

        response = requests.post("{}/predict".format(model_url), json=data)

    if not response.status_code == 200:
        raise ValueError("Error in processing payload, {}".format(response.text))

    response = response.json()

    return Result.parse_obj(response)


def draw_preds(image: Image, detections: [Detection]):

    class_names = list(set([detection.class_name for detection in detections]))

    image_with_preds = image.copy()

    # Define colors
    colors = plt.cm.get_cmap("viridis", len(class_names)).colors
    colors = (colors[:, :3] * 255.0).astype(np.uint8)

    # Define font
    font = list(Path("/usr/share/fonts").glob("**/*.ttf"))[0].name
    font = ImageFont.truetype(font=font, size=np.floor(3e-2 * image_with_preds.size[1] + 0.5).astype("int32"))
    thickness = (image_with_preds.size[0] + image_with_preds.size[1]) // 300

    # Draw detections
    for detection in detections:
        left, top, right, bottom = detection.x_min, detection.y_min, detection.x_max, detection.y_max
        score = float(detection.confidence)
        predicted_class = detection.class_name
        class_idx = class_names.index(predicted_class)

        label = "{} {:.2f}".format(predicted_class, score)

        draw = ImageDraw.Draw(image_with_preds)
        label_size = draw.textsize(label, font)

        top = max(0, np.floor(top + 0.5).astype("int32"))
        left = max(0, np.floor(left + 0.5).astype("int32"))
        bottom = min(image_with_preds.size[1], np.floor(bottom + 0.5).astype("int32"))
        right = min(image_with_preds.size[0], np.floor(right + 0.5).astype("int32"))

        if top - label_size[1] >= 0:
            text_origin = np.array([left, top - label_size[1]])
        else:
            text_origin = np.array([left, top + 1])

        # My kingdom for a good redistributable image drawing library.
        for r in range(thickness):
            draw.rectangle([left + r, top + r, right - r, bottom - r], outline=tuple(colors[class_idx]))
        draw.rectangle([tuple(text_origin), tuple(text_origin + label_size)], fill=tuple(colors[class_idx]))

        if any(colors[class_idx] > 128):
            fill = (0, 0, 0)
        else:
            fill = (255, 255, 255)

        draw.text(text_origin, label, fill=fill, font=font)

        del draw

    return image_with_preds


# ---- Streamlit App ---

st.title("Yolo v5 Companion App")

st.markdown(
    "A super nice companion application to send requests and parse results\n"
    "We wrap https://pytorch.org/hub/ultralytics_yolov5/"
)

# ---- Sidebar ----

test_mode_on = st.sidebar.checkbox(label="Test Mode - Generate dummy answer", value=False)

st.sidebar.markdown("Enter the cluster URL")
model_url = st.sidebar.text_input(label="Cluster URL", value="http://localhost:8000")

_model_url = model_url.strip("/")

if st.sidebar.button("Send 'is alive' to IP"):
    try:
        health = requests.get("{}/health".format(_model_url))
        title = requests.get("{}/".format(_model_url))
        version = requests.get("{}/version".format(_model_url))
        describe = requests.get("{}/describe".format(_model_url))

        if health.status_code == 200:
            st.sidebar.success("Webapp responding at {}".format(_model_url))
            st.sidebar.json({"title": title.text, "version": version.text, "description": describe.text})
        else:
            st.sidebar.error("Webapp not respond at {}, check url".format(_model_url))
    except ConnectionError:
        st.sidebar.error("Webapp not respond at {}, check url".format(_model_url))


# ---- Main window ----

st.markdown("## Inputs")
st.markdown("Select your model (Small, Medium or Large)")

# Data input
model_name = st.radio(label="Model Name", options=["yolov5s", "yolov5m", "yolov5l"])

st.markdown("Upload an image")

image_file = st.file_uploader(label="Image File", type=["png", "jpg", "tif"])

confidence_threshold = st.slider(label="Confidence filter", min_value=0.0, max_value=1.0, value=0.0, step=0.05)

# UploadFile to PIL Image
if image_file is not None:
    image_file.seek(0)
    image = image_file.read()
    image = Image.open(io.BytesIO(image))

st.markdown("Send the payload to {}/predict".format(_model_url))

# Send payload
if st.button(label="SEND PAYLOAD"):
    if test_mode_on:
        st.warning("Simulating a dummy request to {}".format(model_url))
        result = make_dummy_request(model_url=_model_url, model=model_name, image=image)
    else:
        result = make_request(model_url=_model_url, model=model_name, image=image)

    st.balloons()

    # Display results
    st.markdown("## Display")

    st.text("Model : {}".format(result.model))
    st.text("Processing time : {}s".format(result.time))

    detections = [detection for detection in result.detections if detection.confidence > confidence_threshold]

    image_with_preds = draw_preds(image, detections)
    st.image(image_with_preds, width=1024, caption="Image with detections")

    st.markdown("### Detection dump")
    for detection in result.detections:
        st.json(detection.json())
