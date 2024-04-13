import streamlit as st
from PIL import Image
import torch
import pathlib
from torchvision import transforms


style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    .main{
        background: linear-gradient(to bottom, #ff0066 0%, #6666ff 100%);
    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #ffffff;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
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

st.markdown(style,unsafe_allow_html=True)

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model_path = "C:/Users/sharm/OneDrive/Desktop/ChildGaurd_AI/CGAI_model/ChildGaurdAI_resnet.pkl"
new_model = torch.load(model_path, map_location=torch.device('cpu'))

# Define class labels
class_labels = {0: "nsfw_1", 1: "nsfw_2", 2: "nsfw_3", 3: "safe"}

# Streamlit app
def main():
    st.title("Explicit Image Detection")

    # File uploader
    st.write("Upload an image to check for explicit content:")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)

        # Preprocess the image
        preprocess = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)  # Add a batch dimension

        # Perform model inference
        with torch.no_grad():
            output = new_model.forward(input_batch)

        # Get the predicted class label
        _, predicted_class = torch.max(output, 1)
        predicted_label = class_labels[predicted_class.item()]

        if predicted_label == 'nsfw_3':
            st.markdown('<p style="color:red; background-color: white; border: 2px solid red; padding: 10px;">Highly Dangerous!</p>', unsafe_allow_html=True)
        elif predicted_label == 'nsfw_2':
            st.markdown('<p style="color:red; background-color: white;border: 2px solid red; padding: 10px;">Dangerous!</p>', unsafe_allow_html=True)
        elif predicted_label == 'nsfw_1':
            st.markdown('<p style="color:red; background-color: white;border: 2px solid red; padding: 10px;">Explicit cartoon!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color:green; background-color: white; border: 2px solid green; padding: 10px;">Safe</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()