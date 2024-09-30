# app.py
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# Load the trained model (in .keras format)
path = os.path.join(os.getcwd(),"src", 'HerbalPlantClassification.keras')
# path = os.path.join(os.getcwd(), 'HerbalPlantClassification.keras')

if not os.path.isfile(path):
    raise FileNotFoundError(f"Model file not found at {path}. Please make sure to train the model first.")

model = load_model(path)


# Define the class names (Make sure this matches your dataset classes)
classes = ['Aloevera', 'Amla', 'Amruthaballi', 'Arali', 'Astma_weed', 'Badipala', 'Balloon_Vine', 'Bamboo', 'Beans', 'Betel', 'Bhrami', 'Bringaraja', 'Caricature', 'Castor', 'Catharanthus', 'Chakte', 'Chilly', 'Citron lime (herelikai)', 'Coffee', 'Common rue(naagdalli)', 'Coriender', 'Curry', 'Doddpathre', 'Drumstick', 'Ekka', 'Eucalyptus', 'Ganigale', 'Ganike', 'Gasagase', 'Ginger', 'Globe Amarnath', 'Guava', 'Henna', 'Hibiscus', 'Honge', 'Insulin', 'Jackfruit', 'Jasmine', 'Kambajala', 'Kasambruga', 'Kohlrabi', 'Lantana', 'Lemon', 'Lemongrass', 'Malabar_Nut', 'Malabar_Spinach', 'Mango', 'Marigold', 'Mint', 'Neem', 'Nelavembu', 'Nerale', 'Nooni', 'Onion', 'Padri', 'Palak(Spinach)', 'Papaya', 'Parijatha', 'Pea', 'Pepper', 'Pomoegranate', 'Pumpkin', 'Raddish', 'Rose', 'Sampige', 'Sapota', 'Seethaashoka', 'Seethapala', 'Spinach1', 'Tamarind', 'Taro', 'Tecoma', 'Thumbe', 'Tomato', 'Tulsi', 'Turmeric', 'ashoka', 'camphor', 'kamakasturi', 'kepala']

herb_info = {
    'Aloevera': {
        'botanical_name': 'Aloe barbadensis',
        'medicinal_uses': 'Used for skin conditions, burns, and digestive issues.'
    },
    'Amla': {
        'botanical_name': 'Phyllanthus emblica',
        'medicinal_uses': 'Rich in Vitamin C, used for boosting immunity and skin health.'
    },
    'Amruthaballi': {
        'botanical_name': 'Tinospora cordifolia',
        'medicinal_uses': 'Known for its immune-boosting properties and treating fevers.'
    },
    'Arali': {
        'botanical_name': 'Nerium oleander',
        'medicinal_uses': 'Used for heart diseases and as an anti-inflammatory.'
    },
    'Astma_weed': {
        'botanical_name': 'Euphorbia hirta',
        'medicinal_uses': 'Used to treat asthma and respiratory issues.'
    },
    'Badipala': {
        'botanical_name': 'Citrus reticulata',
        'medicinal_uses': 'Used for digestion and respiratory problems.'
    },
    'Balloon_Vine': {
        'botanical_name': 'Cardiospermum halicacabum',
        'medicinal_uses': 'Used for treating skin ailments and as an anti-inflammatory.'
    },
    'Bamboo': {
        'botanical_name': 'Bambusa vulgaris',
        'medicinal_uses': 'Used for digestive issues and as a diuretic.'
    },
    'Beans': {
        'botanical_name': 'Phaseolus vulgaris',
        'medicinal_uses': 'Rich in protein and fiber; aids in digestion.'
    },
    'Betel': {
        'botanical_name': 'Piper betle',
        'medicinal_uses': 'Used for digestive issues and as an antiseptic.'
    },
    'Bhrami': {
        'botanical_name': 'Bacopa monnieri',
        'medicinal_uses': 'Known for its cognitive-enhancing properties.'
    },
    'Bringaraja': {
        'botanical_name': 'Eclipta prostrata',
        'medicinal_uses': 'Used for hair growth and liver health.'
    },
    'Caricature': {
        'botanical_name': 'Carica papaya',
        'medicinal_uses': 'Used for digestion and as an anti-inflammatory.'
    },
    'Castor': {
        'botanical_name': 'Ricinus communis',
        'medicinal_uses': 'Used as a laxative and for skin conditions.'
    },
    'Catharanthus': {
        'botanical_name': 'Catharanthus roseus',
        'medicinal_uses': 'Used in cancer treatment and for lowering blood sugar.'
    },
    'Chakte': {
        'botanical_name': 'Mangifera indica',
        'medicinal_uses': 'Used for digestive health and skin conditions.'
    },
    'Chilly': {
        'botanical_name': 'Capsicum annuum',
        'medicinal_uses': 'Used for pain relief and digestive health.'
    },
    'Citron lime (herelikai)': {
        'botanical_name': 'Citrus limonia',
        'medicinal_uses': 'Used for digestion and as an antiseptic.'
    },
    'Coffee': {
        'botanical_name': 'Coffea',
        'medicinal_uses': 'Used for energy boost and cognitive enhancement.'
    },
    'Common rue(naagdalli)': {
        'botanical_name': 'Ruta graveolens',
        'medicinal_uses': 'Used for digestive disorders and as a mild sedative.'
    },
    'Coriender': {
        'botanical_name': 'Coriandrum sativum',
        'medicinal_uses': 'Used for digestive issues and anti-inflammatory properties.'
    },
    'Curry': {
        'botanical_name': 'Murraya koenigii',
        'medicinal_uses': 'Used for digestion and promoting hair health.'
    },
    'Doddpathre': {
        'botanical_name': 'Peperomia pellucida',
        'medicinal_uses': 'Used for treating colds and respiratory conditions.'
    },
    'Drumstick': {
        'botanical_name': 'Moringa oleifera',
        'medicinal_uses': 'Rich in nutrients; used for anti-inflammatory and antioxidant properties.'
    },
    'Ekka': {
        'botanical_name': 'Solanum melongena',
        'medicinal_uses': 'Used for digestive health and skin conditions.'
    },
    'Eucalyptus': {
        'botanical_name': 'Eucalyptus globulus',
        'medicinal_uses': 'Used for respiratory issues and as an antiseptic.'
    },
    'Ganigale': {
        'botanical_name': 'Zingiber zerumbet',
        'medicinal_uses': 'Used for digestive issues and as a pain reliever.'
    },
    'Ganike': {
        'botanical_name': 'Amaranthus sp.',
        'medicinal_uses': 'Used for its rich nutrient content and anti-inflammatory properties.'
    },
    'Gasagase': {
        'botanical_name': 'Vigna radiata',
        'medicinal_uses': 'Used for digestive health and rich in protein.'
    },
    'Ginger': {
        'botanical_name': 'Zingiber officinale',
        'medicinal_uses': 'Used for nausea, digestion, and anti-inflammatory effects.'
    },
    'Globe Amarnath': {
        'botanical_name': 'Amaranthus dubius',
        'medicinal_uses': 'Used for its rich nutrient content and blood sugar regulation.'
    },
    'Guava': {
        'botanical_name': 'Psidium guajava',
        'medicinal_uses': 'Used for digestive health and rich in Vitamin C.'
    },
    'Henna': {
        'botanical_name': 'Lawsonia inermis',
        'medicinal_uses': 'Used for skin conditions and as a dye.'
    },
    'Hibiscus': {
        'botanical_name': 'Hibiscus sabdariffa',
        'medicinal_uses': 'Used for lowering blood pressure and as a diuretic.'
    },
    'Honge': {
        'botanical_name': 'Pongamia pinnata',
        'medicinal_uses': 'Used for skin ailments and as an insect repellent.'
    },
    'Insulin': {
        'botanical_name': 'Opuntia',
        'medicinal_uses': 'Used for diabetes management.'
    },
    'Jackfruit': {
        'botanical_name': 'Artocarpus heterophyllus',
        'medicinal_uses': 'Used for digestive health and anti-inflammatory properties.'
    },
    'Jasmine': {
        'botanical_name': 'Jasminum officinale',
        'medicinal_uses': 'Used for relaxation and as an anti-anxiety herb.'
    },
    'Kambajala': {
        'botanical_name': 'Pongamia pinnata',
        'medicinal_uses': 'Used for various ailments including diabetes.'
    },
    'Kasambruga': {
        'botanical_name': 'Evolvulus alsinoides',
        'medicinal_uses': 'Used for cognitive enhancement and treating stress.'
    },
    'Kohlrabi': {
        'botanical_name': 'Brassica oleracea var. gongylodes',
        'medicinal_uses': 'Rich in nutrients; used for digestive health.'
    },
    'Lantana': {
        'botanical_name': 'Lantana camara',
        'medicinal_uses': 'Used for skin ailments and respiratory issues.'
    },
    'Lemon': {
        'botanical_name': 'Citrus limon',
        'medicinal_uses': 'Used for digestion, skin health, and as an antioxidant.'
    },
    'Lemongrass': {
        'botanical_name': 'Cymbopogon citratus',
        'medicinal_uses': 'Used for digestion and as an anti-anxiety herb.'
    },
    'Malabar_Nut': {
        'botanical_name': 'Adhatoda vasica',
        'medicinal_uses': 'Used for respiratory issues and as an anti-inflammatory.'
    },
    'Malabar_Spinach': {
        'botanical_name': 'Basella alba',
        'medicinal_uses': 'Rich in nutrients; used for digestive health.'
    },
    'Mango': {
        'botanical_name': 'Mangifera indica',
        'medicinal_uses': 'Rich in vitamins; used for skin health and digestion.'
    },
    'Marigold': {
        'botanical_name': 'Tagetes',
        'medicinal_uses': 'Used for skin conditions and as an anti-inflammatory.'
    },
    'Mint': {
        'botanical_name': 'Mentha',
        'medicinal_uses': 'Used for digestive issues and as a flavoring.'
    },
    'Neem': {
        'botanical_name': 'Azadirachta indica',
        'medicinal_uses': 'Used for skin conditions, dental health, and as an anti-inflammatory.'
    },
    'Nelavembu': {
        'botanical_name': 'Andrographis paniculata',
        'medicinal_uses': 'Used for fevers and boosting immunity.'
    },
    'Nerale': {
        'botanical_name': 'Morus alba',
        'medicinal_uses': 'Used for blood purification and respiratory issues.'
    },
    'Nooni': {
        'botanical_name': 'Trichosanthes dioica',
        'medicinal_uses': 'Used for digestive health and as a cooling agent.'
    },
    'Onion': {
        'botanical_name': 'Allium cepa',
        'medicinal_uses': 'Used for respiratory health and as an anti-inflammatory.'
    },
    'Padri': {
        'botanical_name': 'Amaranthus',
        'medicinal_uses': 'Used for its rich nutrient content and in traditional remedies.'
    },
    'Palak(Spinach)': {
        'botanical_name': 'Spinacia oleracea',
        'medicinal_uses': 'Rich in iron; used for overall health and blood purification.'
    },
    'Papaya': {
        'botanical_name': 'Carica papaya',
        'medicinal_uses': 'Used for digestion and skin health.'
    },
    'Parijatha': {
        'botanical_name': 'Nyctanthes arbor-tristis',
        'medicinal_uses': 'Used for respiratory issues and as a sleep aid.'
    },
    'Pea': {
        'botanical_name': 'Pisum sativum',
        'medicinal_uses': 'Rich in protein and fiber; used for digestive health.'
    },
    'Pepper': {
        'botanical_name': 'Piper nigrum',
        'medicinal_uses': 'Used for digestive issues and as an anti-inflammatory.'
    },
    'Pomoegranate': {
        'botanical_name': 'Punica granatum',
        'medicinal_uses': 'Rich in antioxidants; used for heart health and anti-inflammatory properties.'
    },
    'Pumpkin': {
        'botanical_name': 'Cucurbita pepo',
        'medicinal_uses': 'Rich in nutrients; used for digestive health and skin conditions.'
    },
    'Raddish': {
        'botanical_name': 'Raphanus sativus',
        'medicinal_uses': 'Used for digestion and as a detoxifier.'
    },
    'Rose': {
        'botanical_name': 'Rosa',
        'medicinal_uses': 'Used for skin health and as an anti-inflammatory.'
    },
    'Sampige': {
        'botanical_name': 'Michelia champaca',
        'medicinal_uses': 'Used for respiratory health and relaxation.'
    },
    'Sapota': {
        'botanical_name': 'Manilkara zapota',
        'medicinal_uses': 'Rich in nutrients; used for digestive health.'
    },
    'Seethaashoka': {
        'botanical_name': 'Saraca asoca',
        'medicinal_uses': "Used for women's health and as an anti-inflammatory."
    },
    'Seethapala': {
        'botanical_name': 'Annona squamosa',
        'medicinal_uses': 'Used for digestive health and skin conditions.'
    },
    'Spinach1': {
        'botanical_name': 'Spinacia oleracea',
        'medicinal_uses': 'Rich in iron; used for overall health and blood purification.'
    },
    'Tamarind': {
        'botanical_name': 'Tamarindus indica',
        'medicinal_uses': 'Used for digestive health and as a laxative.'
    },
    'Taro': {
        'botanical_name': 'Colocasia esculenta',
        'medicinal_uses': 'Used for digestive health and as a source of starch.'
    },
    'Tecoma': {
        'botanical_name': 'Tecoma stans',
        'medicinal_uses': 'Used for respiratory conditions and as an anti-inflammatory.'
    },
    'Thumbe': {
        'botanical_name': 'Solanum torvum',
        'medicinal_uses': 'Used for digestive health and as a blood purifier.'
    },
    'Tomato': {
        'botanical_name': 'Solanum lycopersicum',
        'medicinal_uses': 'Rich in antioxidants; used for heart health and skin health.'
    },
    'Tulsi': {
        'botanical_name': 'Ocimum sanctum',
        'medicinal_uses': 'Used for respiratory disorders, stress relief, and boosting immunity.'
    },
    'Turmeric': {
        'botanical_name': 'Curcuma longa',
        'medicinal_uses': 'Used for its anti-inflammatory and antioxidant properties.'
    },
    'ashoka': {
        'botanical_name': 'Saraca asoca',
        'medicinal_uses': "Used for women's health and as an anti-inflammatory."
    },
    'camphor': {
        'botanical_name': 'Cinnamomum camphora',
        'medicinal_uses': 'Used for pain relief and as an antiseptic.'
    },
    'kamakasturi': {
        'botanical_name': 'Hedychium sp.',
        'medicinal_uses': 'Used for its aromatic properties and as a stimulant.'
    },
    'kepala': {
        'botanical_name': 'Carica papaya',
        'medicinal_uses': 'Used for digestion and skin health.'
    }
}

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
    
    if predicted_class in herb_info:
        botanical_name = herb_info[predicted_class]['botanical_name']
        medicinal_uses = herb_info[predicted_class]['medicinal_uses']
        st.write(f"**Botanical Name:** {botanical_name}")
        st.write(f"**Medicinal Uses:** {medicinal_uses}")
    else:
        st.write("No additional information available for this plant.")
