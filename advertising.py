import streamlit as st
import pandas as pd
import pickle

#pickle pickle function in Python helps you save Python objects (like lists, dictionaries, or custom-made objects) into files, 
#and later load those files to get back the original objects.

st.write("""
# Iris Flower Prediction App

This app wants to know the **Sales** of each product!
""")

st.sidebar.header('User Input Parameters') #inside sidebar, function we select is

def user_input_features():
    TV = st.sidebar.slider('TV', 0.7, 297.0, 100.0)
    Radio = st.sidebar.slider('Radio', 0.0, 50.0, 15.0)
    Newspaper = st.sidebar.slider('Newspaper', 0.3, 114.0, 20.0)
    data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper}

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters') #headler - title #subheader - sub title
st.write(df) #display

loaded_model = pickle.load(open("Advertisingmodel.h5", "rb"))   #iris_model - 

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)
