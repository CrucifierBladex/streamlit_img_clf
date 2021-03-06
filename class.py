import streamlit as st

from PIL import Image

	
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

	
from keras.applications.vgg16 import VGG16
from keras.applications import preprocess_input
st.title('Img Clf Tool')
file=st.file_uploader('Choose a file(JPEG format)',type='jpeg')
image=Image.open(file)
st.image(file,caption='Uploaded Image',use_column_width=True)

def predict(image_path): 
    model = VGG16()
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    image = preprocess_input(image)
    yhat = model.predict(image)
    label = decode_predictions(yhat)
    # return highest probability 
    label = label[0][0]
    return label
res=predict(image)
st.write(res)
