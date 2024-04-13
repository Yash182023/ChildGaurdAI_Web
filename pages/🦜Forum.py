import streamlit as st
from deta import Deta

style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    
    .main{
        background-color: #0093E9;
        background-image: linear-gradient(160deg, #0093E9 0%, #80D0C7 100%);
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
        text-align: justify;
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
st.markdown(style,unsafe_allow_html=True)

# Initialize Deta with your Deta project key
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
deta = Deta(DETA_KEY)
my_db = deta.Base("ChildGaurd_Post")

# Page title
st.title("Welcome to Our Forum!")

# Sidebar for navigation
st.sidebar.title("Forum Navigation")
selected_page = st.sidebar.radio("Go to", ["Home", "Categories", "New Topic"])

# Home page
if selected_page == "Home":
    st.write("Welcome to our forum! Feel free to explore and participate in discussions.")
    st.subheader("Recent Posts")

    # Fetch posts data from the database
    posts_data = my_db.fetch().items

    # Display recent posts
    for post in posts_data:
        st.markdown(
        f"""
        <div style="padding: 10px;   background: #02a6a3;
            background: -webkit-linear-gradient(to right, #02a6a3, #0363ff);
            background: linear-gradient(to right, #02a6a3, #0363ff);\
            border: 3px solid #ffffff; border-radius: 5px; margin-bottom: 10px;">
            <h3 style="margin-bottom: 5px;">{post['Title']}</h3>
            <p style="margin-bottom: 5px;"><strong>Author:</strong> {post['Author']}</p>
            <p style="margin-bottom: 5px;"><strong>Content:</strong> {post['Content']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Categories page
elif selected_page == "Categories":
    st.write("Here are the main categories in our forum:")
    st.write("- Category 1")
    st.write("- Category 2")
    st.write("- Category 3")
    
elif selected_page == "New Topic":
    st.subheader("Create a New Topic")
    category = st.selectbox("Select Category", ["Category 1", "Category 2", "Category 3"])
    topic_title = st.text_input("Topic Title")
    topic_content = st.text_area("Topic Content", height=200)
    author_name = st.text_area("Author Name")
    if st.button("Submit"):
        # Construct the new topic dictionary
        new_topic = {
            "Author": author_name,
            "Title": topic_title,
            "Content": topic_content
        }
        # Insert the new topic into the database
        my_db.put(new_topic)
        st.success("Topic submitted successfully!")