import torch
import numpy as np
from torchvision import transforms
from flask import Flask, jsonify, request
from model import ALL_efficientnet_b0_model  # 모델 임포트


if flask.request.method == "POST" and flask.request.files.get("image"):
    image = flask.request.files["image"].read()
    extention = magic.from_buffer(image).split()[0].upper()
    # if extention == 'GIF':
    #     imageObject = Image.open(io.BytesIO(image))
    #     imageObject.seek(0) 
    #     imageObject = imageObject.convert('RGB')
    #     image = np.array(imageObject)
    # elif extention != 'JPEG' and extention != 'PNG':
    #     return flask.jsonify(data)
    # else:
    #     image = Image.open(io.BytesIO(image)).convert('RGB')
    # image, T, R, B, L = prepare_image(image, target=(256, 256))
