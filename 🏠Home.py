import streamlit as st
from datetime import datetime
from deta import Deta


# Initialize Deta Base
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
deta = Deta(DETA_KEY)
my_db = deta.Base("ChildGaurd_Regis")

# Custom CSS
custom_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Anta&display=swap');
   
    .main{
        background-color: #f0f0f0;
        background: url("https://i.ibb.co/59hn9Kh/bg-2.png") no-repeat center center fixed;
        background-size: cover;
    }
    
    body{
        background-color: #fffcfc;
    }
    h1{
        color: #554400ff;
        font-family: "Anta", sans-serif;
        font-weight: 400;
        font-style: normal;
        text-align: center;
    }
    
    h2{
        color: #554400ff;
        font-family: "Anta", sans-serif;
        font-weight: 400;
        font-style: normal;
        text-align: center;
    }
    p{
        color:#554400ff;
        font-family: "Anta", sans-serif;
        font-size: 18px;
    }
    .st-emotion-cache-19rxjzo{
        background-color: #fffcfc;
        border-radius: 2rem;
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

# Display the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Registration function
def register_user(age, gender, role, u_id, username, date_of_registration):
    registration_data = {
        "Age": age,
        "Gender": gender,
        "Role": role,
        "U_ID": u_id,
        "Username": username,
        "Date_of_Registration": date_of_registration
    }

    try:
        # Store registration data in Deta Base
        my_db.put(registration_data)
        st.success("Registration successful!")
    except Exception as e:
        st.error(f"Error: {e}")

# Initialize session state
if 'form_visible' not in st.session_state:
    st.session_state.form_visible = False

# Your Streamlit app content
st.title("Welcome to ChildGuard AI")

# Description of ChildGaurd AI platform
st.header("Introducing ChildGuard AI - Empowering Children and Parents")

description = """
Our comprehensive ChildGaurd AI platform is a groundbreaking solution designed to empower both children and parents in navigating the digital landscape Gaurdly. This education portal serves as a knowledge hub, delivering vital information in various formats—audio, text, and video—covering critical topics such as recognizing good touch and bad touch, identifying potential threats, and guiding on reporting mechanisms.

Our platform goes beyond awareness; it equips users with the tools to actively analyze online content for explicit texts, images, and videos. With a robust reporting system featuring comprehensive categories and anonymous reporting options, children and parents can confidently report any online or offline incidents. Reports are meticulously verified by our team to ensure accuracy and swift response.

Safety is paramount, and our geolocation alerts offer an added layer of protection, allowing children to share their location or enabling parents to track them in times of potential danger. In emergencies, a swift and efficient emergency response system is in place, allowing children to send SOS signals for immediate action by authorities.

For those seeking support and guidance, our platform features a user-friendly chatbot capable of addressing a myriad of queries. Additionally, counseling sessions are available via text, call, or video call, ensuring accessibility and comfort for users in discussing their concerns.

Fostering community engagement, our platform includes a dedicated forum for open discussions. Here, children and parents can share experiences, seek advice, and offer support—a virtual space promoting solidarity and collective resilience.

ChildGaurd AI is not just an educational platform; it's a multifaceted tool empowering users to navigate the digital realm confidently, report incidents, receive timely support, and actively contribute to a Gaurdr online community. Together, we build a shield against potential threats, creating a secure space for children and parents to thrive in the digital age.
"""

st.markdown(description)

if st.button("Register"):
    st.session_state.form_visible = not st.session_state.form_visible

# Input fields for registration (conditionally rendered based on visibility state)
if st.session_state.form_visible:
    age = st.text_input("Age")
    
    gender_options = ["","Male", "Female", "Transgender","Cisgender","Non-Binary","Gay","Lesbian"]
    gender = st.selectbox("Gender", gender_options)
    
    role_options = ["","Child", "Parent", "Gaurdian"]
    role = st.selectbox("Role",role_options)
    
    u_id = st.text_input("U_ID", value="", placeholder="Like 'A00__' followed by any number")
    username = st.text_input("Username")
    
    date_of_registration = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

    # Button for submission
    if st.button("Submit"):
        # Call registration function
        register_user(age, gender, role, u_id, username, date_of_registration)

