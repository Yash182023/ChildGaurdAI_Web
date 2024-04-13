import streamlit as st
from twilio.rest import Client

# give your Twilio credentials
# account_sid = ''
# auth_token = ''
# twilio_number = ''
# recipient_number = ''  # Update with your recipient's phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)
st.title("Welcome to our Education page")

custom_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap');

    .main {
        background-color: #4158D0;
        background-image: linear-gradient(43deg, #4158D0 0%, #C850C0 46%, #FFCC70 100%);

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
        padding-left: 10px;
    }

    .box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 0 0 5px #690021;
    }
    .st-emotion-cache-1dj0hjr{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #ffffff;
        text-align: justify;
    }

    p1 {
        font-family: 'Oswald', sans-serif;
        font-weight: 500;
        font-size: 30px;
        color: #690021;
    }
    
    p2 {
        font-family: 'Oswald', sans-serif;
        font-weight: 500;
        font-size: 20px;
        color: #690021;
    }
    
    p3 {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 20px;
        color: #690021;
    }
    st-emotion-cache-19rxjzo{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 6.5rem;
    min-height: 38.4px;
    margin: 0px;
    margin-top: 32px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: rgb(19, 23, 32);
    border: 1px solid rgba(250, 250, 250, 0.2);
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

st.markdown(custom_style, unsafe_allow_html=True)

user_type = st.selectbox("Select User Type", ["", "Child", "Parent", "Guardian"])

if user_type == "Child":
    st.write("Welcome, Child!")
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>So first we are going to discuss the concept of touch</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #690021;'>There are two types of touch: Good touch and Bad touch</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #25007d;'>Definition of Good Touch: Good touch is when someone touches you in a way that makes you feel happy,\
                safe, and comfortable. It's the kind of touch that happens when you give or receive a hug from someone you love,\
                a high-five with a friend, or a gentle pat on the back. Good touches are friendly,\
                warm, and make you feel cared for and respected.</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #f7021b;'>Bad touch is when someone touches your private parts,\
                or any part of your body, in a way that makes you feel scared, confused, or uncomfortable. Private parts are the areas of your body covered by a swimsuit.\
                No one should touch these parts except to help you stay clean and healthy, or if a doctor or nurse is checking to keep you well.</p>\
                </div>", unsafe_allow_html=True)
    
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>Parts should not be touched by strangers:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>If anybody touches your chest(or breasts), and makes you feel uncomfortable</li>\
                    <li>If anybody touches your back(or hips), and makes you feel uncomfortable</li>\
                    <li>If anybody touches your vagina, and makes you feel uncomfortable</li>\
                    <li>If anybody tries to kiss you on cheeks, and you feel it uncomfortable</li>\
                    <li>If anybody tries to kiss you on lips, that's definitly a bad touch should be reported immediately</li>\
                    <!-- Add more items as needed -->\
                </ul>\
            </div>", unsafe_allow_html=True)
    
    if st.button("\nSOS - Report Emergency"):
        try:
            # Send SOS SMS
            sos_message = "Emergency! ChildGaurd AI SOS activated, Your Child is in Danger!"
            message = client.messages.create(
                from_=twilio_number,
                body=sos_message,
                to=recipient_number
            )
            st.success(f"SOS Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"Error sending SOS message: {str(e)}")
        
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>To whom should you report:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>A trusted adult like Mom, Dad, older Brother or Sister</li>\
                     <li><a href='tel:000'>Call Us Now!</a></li>\
                     <li>Press the SOS button above</li>\
                 </ul>\
            </div>", unsafe_allow_html=True)
elif user_type == "Parent":
    st.write("Welcome, Parent!")
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>This page would contain some important things which parents miss to address in a child socially not the usual ones</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #690021;'>As the child doesn’t know much about his/her body it is very important for the child to know who can touch his/her body\
                and who cannot, there is a lot of literature available on this topic but we want to provide some more.</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #25007d;'>Definition of Good Touch: Good touch is when someone touches you in a way that makes you feel happy,\
                safe, and comfortable. It's the kind of touch that happens when you give or receive a hug from someone you love,\
                a high-five with a friend, or a gentle pat on the back. Good touches are friendly,\
                warm, and make you feel cared for and respected.</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #f7021b;'>Bad touch is when someone touches your private parts,\
                or any part of your body, in a way that makes you feel scared, confused, or uncomfortable. Private parts are the areas of your body covered by a swimsuit.\
                No one should touch these parts except to help you stay clean and healthy, or if a doctor or nurse is checking to keep you well.</p>\
                </div>", unsafe_allow_html=True)
    
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>The concept of good touch and bad touch is widely discussed but let me elaborate on it, a bit:-</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>Anybody whether it is parents, siblings, other family members, relatives, or other people, should ask permission before hugging, kissing on the cheeks, etc. Parents should first initiate this behavior, why I am saying this because the child would have a clear idea from the beginning that his/her body is not a playing object, as the human will grow people will see his/her more as a tool, and the world will use him/her but this would make her/him aware that he/she is not a body.</li>\
                    <li>Similarly, no one should touch their chest area(breast), back area(hip), or vagina, except themselves, as these organs are highly sensual if exploited or abused it would lead to childhood trauma, PTSD, other mental health disorders, and attachment style problems.</li>\
                    <li>They should not go out with any stranger or any other relative alone in a room, they should stay with their well-wishers.</li>\
                    <li>They should be aware of abusive words or sexual words.</li>\
                    <li>The children should not sit on anybody’s lap if asked to do, yes exploitation can happen that way.</li>\
                    <!-- Add more items as needed -->\
                </ul>\
            </div>", unsafe_allow_html=True)
    
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>Here are some specific reasons why child sexual exploitation differs from exploitation experienced by adults:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>Developmental Vulnerability: Children are in a stage of physical, emotional, and psychological development. Exploitation at this stage can disrupt their natural development and have lasting consequences on their self-esteem, relationships, and overall well-being..</li>\
                    <li>Children often lack the cognitive and emotional maturity to comprehend the nature of the exploitation fully. They may not understand that what is happening to them is wrong or abusive, making it challenging for them to report or seek help.</li>\
                    <li>The power dynamic between a child and an adult or older perpetrator is highly imbalanced. The adult may use their authority and manipulation to coerce the child into silence, leading to feelings of helplessness and fear</li>\
                    <li>If the exploitation is perpetrated by someone the child knows and trusts, such as a family member, caregiver, or authority figure, the betrayal can be especially traumatic for the child. This betrayal can make it difficult for the child to trust others in the future./li>\
                    <li>Exploitation can interfere with healthy attachment and bonding processes between the child and their caregivers. This disruption can have significant implications for the child's emotional and social development.</li>\
                    <li>Children may internalize feelings of guilt and self-blame, believing that they somehow caused or deserved the exploitation. This can lead to a distorted sense of self and further exacerbate the trauma.</li>\
                    <!-- Add more items as needed -->\
                </ul>\
            </div>", unsafe_allow_html=True)
    
    if st.button("\nSOS - Report Emergency"):
        try:
            # Send SOS SMS
            sos_message = "Emergency! ChildGaurd AI SOS activated, Your Child is in Danger!"
            message = client.messages.create(
                from_=twilio_number,
                body=sos_message,
                to=recipient_number
            )
            st.success(f"SOS Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"Error sending SOS message: {str(e)}")
        
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>To whom should you report:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>A trusted adult like Mom, Dad, older Brother or Sister</li>\
                     <li><a href='tel:'>Call Us Now!</a></li>\
                     <li>Press the SOS button above</li>\
                 </ul>\
            </div>", unsafe_allow_html=True)

elif user_type == None:
    st.write("Welcome, Common people")

else:
    st.write("Welcome, Guardian!")
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>This page would contain some important things which parents miss to address in a child socially not the usual ones</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #690021;'>As the child doesn’t know much about his/her body it is very important for the child to know who can touch his/her body\
                and who cannot, there is a lot of literature available on this topic but we want to provide some more.</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #25007d;'>Definition of Good Touch: Good touch is when someone touches you in a way that makes you feel happy,\
                safe, and comfortable. It's the kind of touch that happens when you give or receive a hug from someone you love,\
                a high-five with a friend, or a gentle pat on the back. Good touches are friendly,\
                warm, and make you feel cared for and respected.</p>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 400; font-size: 20px; color: #f7021b;'>Bad touch is when someone touches your private parts,\
                or any part of your body, in a way that makes you feel scared, confused, or uncomfortable. Private parts are the areas of your body covered by a swimsuit.\
                No one should touch these parts except to help you stay clean and healthy, or if a doctor or nurse is checking to keep you well.</p>\
                </div>", unsafe_allow_html=True)
    
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>The concept of good touch and bad touch is widely discussed but let me elaborate on it, a bit:-</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>Anybody whether it is parents, siblings, other family members, relatives, or other people, should ask permission before hugging, kissing on the cheeks, etc. Parents should first initiate this behavior, why I am saying this because the child would have a clear idea from the beginning that his/her body is not a playing object, as the human will grow people will see his/her more as a tool, and the world will use him/her but this would make her/him aware that he/she is not a body.</li>\
                    <li>Similarly, no one should touch their chest area(breast), back area(hip), or vagina, except themselves, as these organs are highly sensual if exploited or abused it would lead to childhood trauma, PTSD, other mental health disorders, and attachment style problems.</li>\
                    <li>They should not go out with any stranger or any other relative alone in a room, they should stay with their well-wishers.</li>\
                    <li>They should be aware of abusive words or sexual words.</li>\
                    <li>The children should not sit on anybody’s lap if asked to do, yes exploitation can happen that way.</li>\
                    <!-- Add more items as needed -->\
                </ul>\
            </div>", unsafe_allow_html=True)
    
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>Here are some specific reasons why child sexual exploitation differs from exploitation experienced by adults:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>Developmental Vulnerability: Children are in a stage of physical, emotional, and psychological development. Exploitation at this stage can disrupt their natural development and have lasting consequences on their self-esteem, relationships, and overall well-being..</li>\
                    <li>Children often lack the cognitive and emotional maturity to comprehend the nature of the exploitation fully. They may not understand that what is happening to them is wrong or abusive, making it challenging for them to report or seek help.</li>\
                    <li>The power dynamic between a child and an adult or older perpetrator is highly imbalanced. The adult may use their authority and manipulation to coerce the child into silence, leading to feelings of helplessness and fear</li>\
                    <li>If the exploitation is perpetrated by someone the child knows and trusts, such as a family member, caregiver, or authority figure, the betrayal can be especially traumatic for the child. This betrayal can make it difficult for the child to trust others in the future./li>\
                    <li>Exploitation can interfere with healthy attachment and bonding processes between the child and their caregivers. This disruption can have significant implications for the child's emotional and social development.</li>\
                    <li>Children may internalize feelings of guilt and self-blame, believing that they somehow caused or deserved the exploitation. This can lead to a distorted sense of self and further exacerbate the trauma.</li>\
                    <!-- Add more items as needed -->\
                </ul>\
            </div>", unsafe_allow_html=True)
    
    if st.button("\nSOS - Report Emergency"):
        try:
            # Send SOS SMS
            sos_message = "Emergency! ChildGaurd AI SOS activated, Your Child is in Danger!"
            message = client.messages.create(
                from_=twilio_number,
                body=sos_message,
                to=recipient_number
            )
            st.success(f"SOS Message sent successfully! SID: {message.sid}")
        except Exception as e:
            st.error(f"Error sending SOS message: {str(e)}")
        
    st.markdown("<div class='box'>\
                <p style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #690021;'>To whom should you report:</p>\
                <ul style='font-family: \"Oswald\", sans-serif; font-optical-sizing: auto; font-weight: 500; font-size: 20px; color: #ff0352;'>\
                    <li>A trusted adult like Mom, Dad, older Brother or Sister</li>\
                     <li><a href='tel:'>Call Us Now!</a></li>\
                     <li>Press the SOS button above</li>\
                 </ul>\
            </div>", unsafe_allow_html=True)


st.subheader("Steps to prevent child sexual abuse")
url1 = "https://www.youtube.com/watch?v=ACvqz9Ws9-w"# Replace with your YouTube video URL or ID
st.video(url1)
st.subheader("Healing adults")
url2 = "https://www.youtube.com/watch?v=5viOYkM4CRE"
st.video(url2)