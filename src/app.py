# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Load the trained model (in .keras format)
path = os.path.join(os.getcwd(),"src", 'HerbalModel.keras')

if not os.path.isfile(path):
    raise FileNotFoundError(f"Model file not found at {path}. Please make sure to train the model first.")

model = load_model(path)


# Define the class names (Make sure this matches your dataset classes)
classes = ['Aloevera', 'Amla', 'Amruthaballi', 'Arali', 'Astma_weed', 'Badipala', 'Balloon_Vine', 'Bamboo', 'Beans', 'Betel', 'Bhrami', 'Bringaraja', 'Caricature', 'Castor', 'Catharanthus', 'Chakte', 'Chilly', 'Citron lime (herelikai)', 'Coffee', 'Common rue(naagdalli)', 'Coriender', 'Curry', 'Doddpathre', 'Drumstick', 'Ekka', 'Eucalyptus', 'Ganigale', 'Ganike', 'Gasagase', 'Ginger', 'Globe Amarnath', 'Guava', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jackfruit', 'Jasmine', 'Kambajala', 'Kasambruga', 'Kohlrabi', 'Lantana', 'Lemon', 'Lemongrass', 'Malabar_Nut', 'Malabar_Spinach', 'Mango', 'Marigold', 'Mint', 'Neem', 'Nelavembu', 'Nerale', 'Nooni', 'Onion', 'Padri', 'Palak(Spinach)', 'Papaya', 'Parijatha', 'Pea', 'Pepper', 'Pomoegranate', 'Pumpkin', 'Raddish', 'Rose', 'Sampige', 'Sapota', 'Seethaashoka', 'Seethapala', 'Spinach1', 'Tamarind', 'Taro', 'Tecoma', 'Thumbe', 'Tomato', 'Tulsi', 'Turmeric', 'ashoka', 'camphor', 'kamakasturi', 'kepala']


# Function to prepare the image
def prepare_image(image):
    image = image.resize((224, 224))  # Adjust to the size your model expects
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit app layout
st.title("Herbal Plant Classifier")
st.write("Upload an image of a herbal plant, and the model will predict its class.")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = load_img(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    # Prepare the image for prediction
    image = prepare_image(image)

    # Make a prediction
    prediction = model.predict(image)
    predicted_class = classes[np.argmax(prediction)]
    confidence = np.max(prediction)

    # Display the result
    st.write(f"**Predicted Class:** {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}")
