import requests
import streamlit as st
from PIL import Image
import io
import base64
from pydantic import BaseModel
from typing import List
import random

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


# ---- Streamlit App ---

st.title("NAME ME BECAUSE I AM AWESOME")

with open("APP.md") as f:
    st.markdown(f.read())

# --- Sidebar ---
# defines an h1 header

model_url = st.sidebar.text_input(label="Cluster URL", value="http://localhost:8000")

_model_url = model_url.strip("/")

if st.sidebar.button("Send 'is alive' to IP"):
    try:
        response = requests.get("{}/health".format(_model_url))
        if response.status_code == 200:
            st.sidebar.success("Webapp responding at {}".format(_model_url))
        else:
            st.sidebar.error("Webapp not respond at {}, check url".format(_model_url))
    except ConnectionError:
        st.sidebar.error("Webapp not respond at {}, check url".format(_model_url))

test_mode_on = st.sidebar.checkbox(label="Test Mode - Generate dummy answer", value=False)

# --- Main window

st.markdown("## Inputs")
st.markdown("Describe something... You can also add things like confidence slider etc...")

# Here we should be able to choose between ["yolov5s", "yolov5m", "yolov5l"], perhaps a radio button with the three choices ?
model_name = ...

# Here we should be able to upload a file (our image)
image_file = ...

# Converting image, this is done for you :)
if image_file is not None:
    image_file.seek(0)
    image = image_file.read()
    image = Image.open(io.BytesIO(image))

if st.button(label="SEND PAYLOAD"):

    if test_mode_on:
        st.warning("Simulating a dummy request to {}".format(model_url))
        result = ...  # call the proper function
    else:
        result = ...  # call the proper function

    st.balloons()

    st.markdown("## Display")

    st.markdown("Make something pretty, draw polygons and confidence..., here's an ugly output")

    st.image(image, width=512, caption="Uploaded Image")

    st.text("Model : {}".format(result.model))
    st.text("Processing time : {}s".format(result.time))

    for detection in result.detections:
        st.json(detection.json())
