import os,sys
sys.path.append(os.getcwd())
import io   
from flask import Flask,request,render_template,jsonify
import numpy as np
from PIL import Image
from components.logger import logging
from prediction.predict import DogCat
from components.exception import CustomException
from tensorflow.keras.preprocessing.image import load_img

app = Flask(__name__)


@app.route("/",methods = ['GET'])
def home():
    return render_template('home.html')

@app.route("/predict",methods = ['POST','GET'])
def predictionImage():
    try:
        if request.method == 'GET':
            return render_template('prediction.html')
        else:

            uploaded_file = request.files['upload']
            
            img = Image.open(io.BytesIO(uploaded_file.read()))
            # img = load_img(uploaded_file,target_size = (224,224))

            class_obj = DogCat()
            result = class_obj.predictionDogCat(img)

            return render_template('prediction.html',final_result = result)        
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = 8000,debug=True)