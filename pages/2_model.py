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
Mv = st.number_input('Mv: ', min_value=0.1, max_value=10.0, value=1.0)


if st.button('Predict Price'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success(price)
