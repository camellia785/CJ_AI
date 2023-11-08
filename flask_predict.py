from flask import Flask, jsonify, request
from imp import load_module


model = load_module('./models/ALL_efficientnet_b0_model')
predictList = ['BEET', 'KALE', 'LETTUCE', 'Mustard greens']

preds = model.predict_classes(image)
print(predictList[preds[0]])

data["predictions"] = predictList[preds[0]]
data["success"] = True

return flask.jsonify(data)