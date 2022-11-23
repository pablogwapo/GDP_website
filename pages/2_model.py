import streamlit as st
import pandas as pd
from tensorflow.keras.models import model_from_json

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")


#Caching the model for faster loading
@st.cache

# Define the prediction function
def predict(Mv,Hc,Skew,):
    prediction = loaded_model.predict(pd.DataFrame([[Mv,Hc, Skew]], columns=['Mv', 'Hc', 'Skew']))
    return prediction


st.title('Magnet quality')
st.header('Enter the characteristics of the Magnet:')
Mv = st.number_input('Mv: ', min_value=0.0, max_value=1)
Hc = st.number_input('Hc: ', min_value=0.0, max_value=35)
Skew = st.number_input('Skew: ', min_value=0.0, max_value=1.6)


if st.button('Predict Jdp'):
    Jdp = predict(Mv,Hc,Skew)
    st.success(Jdp)
