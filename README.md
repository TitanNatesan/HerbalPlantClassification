Herbal Plant Classification
Overview
This project is designed to classify images of herbal plant leaves into 80 different categories using a deep learning model based on the MobileNetV2 architecture. The model is trained on the Indian Medicinal Leaves Dataset and is deployed using Streamlit to provide a web-based interface for predictions.

Project Structure
bash
Copy code
Herbal Plant Classification/
│
├── Dataset/                           # Directory for dataset
│   └── Medicinal Leaf dataset/        # Dataset directory
│
├── env/                               # Virtual environment directory (not included in repository)
│
├── src/                               # Source code directory
│   ├── app.py                         # Streamlit app for deployment
│   └── HerbalModel.keras              # Trained model file
│
├── requirements.txt                   # Python package dependencies
└── README.md                          # This README file
Requirements
Make sure you have Python 3.6 or later installed. You can create a virtual environment and install the required packages using:

bash
Copy code
pip install -r requirements.txt
requirements.txt:

Copy code
numpy
pillow
tensorflow
streamlit
Setup and Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/TitanNatesan/HerbalPlantClassification.git
cd Herbal-Plant-Classification
Create and Activate a Virtual Environment (optional but recommended):

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Download and Prepare the Dataset:

Download the Indian Medicinal Leaves Dataset and place it in the Dataset/Medicinal Leaf dataset/ directory.

Usage
Running the Streamlit App
To start the Streamlit application, run:

bash
Copy code
streamlit run src/app.py
This command will launch a local web server. Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501) to interact with the app.

Making Predictions
Upload an Image: Use the file uploader to choose an image of a herbal plant.
View Predictions: The app will display the predicted class and confidence level based on the uploaded image.
Training the Model
Setup:

Ensure the dataset is correctly placed in the Dataset/Medicinal Leaf dataset/ directory.

Train the Model:

The training script is not included in the current structure but should be placed in the src/ directory. You can create a training script to train and save the model as HerbalModel.keras.

Contributing
Feel free to open issues or submit pull requests. Contributions are welcome!

License
This project does not currently have a license. You are free to use, modify, and distribute the code as you see fit. If you decide to use or adapt this project, please consider adding an appropriate license to clarify the terms of use.
