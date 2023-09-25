import base64
import io
import time
from typing import List, Dict

import numpy as np
import torch
from PIL import Image
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Input(BaseModel):
    model: str
    image: str


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


def parse_prediction(prediction: np.ndarray, classes: [str]) -> Detection:
    x0, y0, x1, y1, cnf, cls = prediction
    detection = Detection(
        x_min=int(x0),
        y_min=int(y0),
        x_max=int(x1),
        y_max=int(y1),
        confidence=round(float(cnf), 3),
        class_name=classes[int(cls)],
    )
    return detection


def load_model(model_name: str) -> Dict:
    # Load model from torch
    model = torch.hub.load("ultralytics/yolov5", model_name, pretrained=True)
    # Evaluation mode + Non maximum threshold
    model = model.eval()

    return model


# %%
app = FastAPI(
    title="YOLO-V5 WebApp created with FastAPI",
    description="""
                Wraps 3 different yolo-v5 models under the same RESTful API
                """,
    version="1.1",
)

# %%
MODEL_NAMES = ["yolov5s", "yolov5m", "yolov5l"]
MODELS = {}


@app.get("/", description="return the title", response_description="title", response_model=str)
def root() -> str:
    return app.title


@app.get("/describe", description="return the description", response_description="description", response_model=str)
def describe() -> str:
    return app.description


@app.get("/version", description="return the version", response_description="version", response_model=str)
def describe() -> str:
    return app.version


@app.get("/health", description="return whether it's alive", response_description="alive", response_model=str)
def health() -> str:
    return "HEALTH OK"


@app.get(
    "/models",
    description="Query the list of models",
    response_description="A list of available models",
    response_model=List[str],
)
def models() -> [str]:
    return MODEL_NAMES


@app.post(
    "/predict",
    description="Send a base64 encoded image + the model name, get detections",
    response_description="Detections + Processing time",
    response_model=Result,
)
def predict(inputs: Input) -> Result:
    global MODELS

    # get correct model
    model_name = inputs.model

    if model_name not in MODEL_NAMES:
        raise HTTPException(status_code=400, detail="wrong model name, choose between {}".format(MODEL_NAMES))

    # check load
    if MODELS.get(model_name) is None:
        MODELS[model_name] = load_model(model_name)

    model = MODELS.get(model_name)

    # Get Image
    # Decode image
    try:
        image = inputs.image.encode("utf-8")
        image = base64.b64decode(image)
        image = Image.open(io.BytesIO(image))
    except:
        raise HTTPException(status_code=400, detail="File is not an image")
    # Convert from RGBA to RGB *to avoid alpha channels*
    if image.mode == "RGBA":
        image = image.convert("RGB")

    # Inference
    t0 = time.time()
    predictions = model(image, size=640)  # includes NMS
    t1 = time.time()
    classes = predictions.names

    # Post processing
    predictions = predictions.xyxy[0].numpy()
    detections = [parse_prediction(prediction=pred, classes=classes) for pred in predictions]

    result = Result(detections=detections, time=round(t1 - t0, 3), model=model_name)

    return result
