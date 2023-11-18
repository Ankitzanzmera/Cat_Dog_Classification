import os,sys
sys.path.append(os.getcwd())
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from components.exception import CustomException
from components.logger import logging

class DogCat:

    def predictionDogCat(self,img):

        try:

            img_data = img.resize((224, 224))   
            img_arr = img_to_array(img_data)
            img_arr = np.expand_dims(img_arr,axis=0)
            model_path = os.path.join(os.getcwd(),'model','model_inception_net.h5')

            model = load_model(model_path)

            y_pred = model.predict(img_arr) 
            y_pred = np.argmax(y_pred,axis = 1)

            result = ''
            if y_pred[0] == 1:
                result = 'Dog'
            else:
                result = 'Cat'

            return result
        except Exception as e:
            CustomException(e,sys)



