import streamlit as st
from transformers import BertForSequenceClassification, BertTokenizerFast, pipeline
import pytesseract
import numpy as np
from PIL import Image


custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: rgb(129,0,242);
        background: linear-gradient(164deg, rgba(129,0,242,1) 0%, rgba(21,1,43,1) 100%);
    }
    
    h1 {
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #ffffff;
    }
    
    .st-emotion-cache-1dj0hjr{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
        text-align: justify;
    }
    
    h3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #2e2409;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff
    }
    

    .st-cf{
        background_color:#ff3300;
    }
    
    .st-ct{
        background_color:#15d100;
    }
    
    .stAlert{
        background_color:#ff3300;
    }
    
    .st-emotion-cache-6qob1r{
        position: relative;
        height: 100%;
        width: 100%;
        overflow: overlay;
        background: rgb(252,0,94);
        background: linear-gradient(164deg, rgba(252,0,94,1) 0%, rgba(89,1,72,1) 100%);
    }
    
    .st-emotion-cache-1avcm0n{
        background: rgb(0,0,89);
background: linear-gradient(164deg, rgba(0,0,89,1) 16%, rgba(0,150,162,1) 100%, rgba(0,255,136,1) 100%);
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Load the BERT model for sequence classification
model_path = "C:/Users/sharm/OneDrive/Desktop/ChildGaurd_AI/Calel_bert"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizerFast.from_pretrained(model_path)
nlp = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Function to perform OCR on the uploaded image
def ocr_image(image):
    text = pytesseract.image_to_string(image)
    return text


st.title("Explicit Content Detection")

# Function to perform OCR followed by text detection
def ocr_and_text_detection():
    # File upload widget for image selection
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR on the image
        extracted_text = ocr_image(image)

        # Display the extracted text
        st.subheader("Extracted Text:")
        st.text(extracted_text)

        # Perform text detection on the extracted text
        if st.button("Detect Explicit Content"):
            # Perform inference on the extracted text
            predictions = nlp(extracted_text)

            # Extract prediction label and score
            label = predictions[0]["label"]
            score = predictions[0]["score"] * 100

            # Define categories based on score thresholds
            if score > 90 and label == "Explicit":
                category = "Highly Dangerous"
            elif 70 <= score <= 90 and label == "Explicit":
                category = "Not Safe"
            elif 50 <= score < 70 and label == "Explicit":
                category = "Mature Content"
            elif 90<=score<=100 and label == "Safe":
                category = "Safe"
            else:
                category = "Not for you!"

            # Output prediction result
            if category == "Safe" and label == "Safe":
                st.success(f"The extracted text does not contain explicit content. Score: {score:.2f}%, Category: {category}")
            elif label == "Safe" and category == "Not for you!":
                st.error(f"The extracted text contains explicit content. Score: {score:.2f}%, Category: {category}")
            elif label == "Explicit" and category=="Mature Content":
                st.error(f"The extracted text contains explicit content. Score: {score:.2f}%, Category: {category}")
    
# Function call to perform OCR followed by text detection
ocr_and_text_detection()
