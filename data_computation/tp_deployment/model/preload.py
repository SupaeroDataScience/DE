"""
This scripts download the models inside the dockerfile to avoid downloading them when preloading the application
"""
import torch

_ = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
_ = torch.hub.load("ultralytics/yolov5", "yolov5m", pretrained=True)
_ = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True)
