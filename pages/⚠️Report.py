import os
import streamlit as st
import dropbox

style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    .main {
        background: rgb(0,118,239);
        background: linear-gradient(164deg, rgba(0,118,239,1) 0%, rgba(128,180,255,1) 100%);
    }

    h1 {
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 40px;
        color: #ffffff;
    }

    p {
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
    }

    .st-b7 {
        background-color: #1a2936;
    }

    .st-emotion-cache-1erivf3 {
        background-color: #1a2936;
    }
    
    .st-emotion-cache-1dj0hjr{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
        text-align: justify;
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

st.markdown(style, unsafe_allow_html=True)


with open("token.txt", "r") as f:
    TOKEN = f.read()

# Initialize Dropbox client
dbx = dropbox.Dropbox(TOKEN)

# Streamlit app title
st.title("Report your content")

# File uploader
uploaded_file = st.file_uploader("The File Name must include your name and phone number!")

# Function to upload files to Dropbox
def upload_to_dropbox(file):
    if file is not None:
        file_name = file.name
        file_content = file.getvalue()
        try:
            # Upload file to Dropbox
            dbx.files_upload(file_content, f"/{file_name}")
            st.success(f"File '{file_name}' uploaded successfully!")
        except dropbox.exceptions.ApiError as e:
            st.error(f"Failed to upload file '{file_name}': {e}")

# Call the upload function when the user clicks the upload button
if st.button("Upload"):
    upload_to_dropbox(uploaded_file)
