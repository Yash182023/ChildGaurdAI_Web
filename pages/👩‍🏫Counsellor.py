import streamlit as st

style ="""
<style>
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

def main():
    st.title("Meetings")

    with open("C:/Users/sharm/OneDrive/Desktop/ChildGaurd_AI/pages/meetings.html", "r") as file:
        html_code = file.read()

    st.components.v1.html(html_code, height=1000)

if __name__ == "__main__":
    main()

