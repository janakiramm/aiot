import os
from tensorflow.keras import models
import flask
from flask import Flask, request, jsonify

model_path = os.getenv('MODEL_DIR')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

pred_model=models.load_model(model_path)

@app.route('/score', methods=['POST'])
def predict():
    arr=request.json ['params']
    print('Predicted: %.3f' % pred_model.predict([arr]))
    fault=('%d' % pred_model.predict([arr]))    
    return jsonify({'fault': fault}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')    