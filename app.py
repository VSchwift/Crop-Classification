import streamlit as st
import pandas as pd
from fastai.vision.all import *

model_file = 'resnet101_export.pkl'
model = load_learner(model_file)

@st.cache_data
def load_data():
    df = pd.read_csv('crop_names.csv')
    return df

crop_df = load_data()

st.title('Agricultural Crop Image Classification')
image_input = st.file_uploader('Please upload the file of the crop you would like me to guess below 🌾')

def guess():    
    # Make predictions with the model
    crop_name, _, probs = model.predict(PILImage.create(image_input))
    answer = st.write(f'This is probably a {crop_name} crop/plantation.')
    return answer

if st.button('Guess'):
    answer = guess()

show_crops = pd.DataFrame(crop_df['Crop Name'].unique(), columns=['Crop Name'])
st.dataframe(show_crops)
