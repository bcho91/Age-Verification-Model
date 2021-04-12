import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image, ImageOps
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tempfile import NamedTemporaryFile



st.title('Is this person a child or an adult?')
st.write('Using convolutional neural networks, we at the Dream Team LLC have developed a method of detecting whether a photo depicts a child or an adult.')

st.set_option('deprecation.showfileUploaderEncoding', False)
temp_file = NamedTemporaryFile(delete=False)

def predictImage(filename):
    model = tf.keras.models.load_model('cnn')    

    temp_file.write(filename.getvalue())
    
    
    img = image.load_img((temp_file.name), target_size=(224, 224))
    img_array = image.img_to_array(img)
   
    img_batch = np.expand_dims(img_array, axis=0)

    img_preprocessed = img_batch/255.

    prediction = model.predict(img_preprocessed)

    prediction = np.max(prediction, axis=1).round()

    print(prediction)
    if prediction >= .51:   
        return "adult"     
    else: 
        return "child"

uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg","png"])

if uploaded_file is not None:
    pic = Image.open(uploaded_file)
    st.image(pic, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = predictImage(uploaded_file)
    st.write(label.upper())
    st.success('Classification Complete!') # success widget 
    st.balloons() # just for fun, shows balloon animations on the page




#if __name__== '__main__': #if this file gets run from our terminal, then run it
 #   app.run(debug=True)