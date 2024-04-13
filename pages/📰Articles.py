import streamlit as st
from deta import Deta

style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

    
    .main{
        background-color: #85FFBD;
        background-image: linear-gradient(45deg, #85FFBD 0%, #FFFB7D 100%);

    }
    
    h1{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 60px;
        color: #1f4202;
    }
    
    h2{
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 20px;
        color: #1f4202;
        text-align: justify;
        
    }
    
    h3{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #1f4202;
        text-align: justify;
    }
    
    p{
        font-family: 'Poppins', sans-serif;
        font-weight: 400;
        font-size: 20px;
        color: #1f4202;
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

# Initialize Deta Base
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
deta = Deta(DETA_KEY)
articles_db = deta.Base("CGAI_Articles")

# Function to display individual articles
def display_article(article):
    st.header(article["Title"])
    st.subheader(f"Author: {article['Author']}")
    st.write(f"<div style='border: 2px solid black; border-radius: 10px; background: linear-gradient(164deg, rgba(0,233,242,0.3787640056022409) 0%, rgba(230,230,230,0.5608368347338936) 100%); font-family: \"Poppins\", sans-serif; font-weight: 400; font-size: 20px; color: #1f4202; text-align: justify; padding: 10px;'>{article['Content']}</div>", unsafe_allow_html=True)


# Main function to display the article page
def main():
    st.title("Welcome to Learnopia!")

    # Fetch articles from the database
    articles_data = articles_db.fetch().items

    # Display articles
    if articles_data:
        for article in articles_data:
            display_article(article)
    else:
        st.write("No articles found.")

if __name__ == "__main__":
    main()
