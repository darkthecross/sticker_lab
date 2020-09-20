from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import cv2
import base64
import numpy as np

app = Flask(__name__)

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/img_process', methods=['POST'])
def handle_image():
    cv_img = data_uri_to_cv2_img(request.form['img_data'])
    return jsonify(cv_img.shape)
