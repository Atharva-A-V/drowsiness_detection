import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid
import os
import time


from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  # or yolov8s.yaml for a slightly larger model

model.train(
    data="D:\projects\drowsiness_detection\data\data.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="drowsiness-detector"
)
