import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Portfolio Web App using Python", page_icon="images/favicon.ico",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/styles.css")

lottie_contactus = load_lottieurl("https://lottie.host/427a3e14-ae60-4765-aa79-99830cc5c662/4hLLg5Yg7X.json")
lottie_coding = load_lottieurl("https://lottie.host/8388219d-df0e-4480-b5f2-4b4bc8d81235/JRCAOnDG25.json")

img_lottie_animation = Image.open("images/demo-telegram.jpg")

with st.container():
    st.subheader("Hello, I am Aashif :wave:")
    st.title("Computer Science Student @ BSA Crescent University")
    st.write("I am passionate about tech related stuffs. Excited to explore the depth of technology.")
    st.write("[Visit my website](https://aashifm.netlify.app)")
    st.write("---")

with st.container():
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.header("What I do")
        st.write(
            """
            I usually like to do some coding. My projects are:
            - Course Master, a telegram bot for programming and other courses.
            - CarBuy 360, a command line car buying interface includes buying, payment(cash/card) and bill generation.
            - Banking System, a banking system that a user create new account, login into old account, make transactions(deposit/transfer) amount.
            - Alexa, a task assistant that a user used to open browser, youtube, chatgpt, ask time and all by voice input. 
            """
        )
        st.write("[Check out my GitHub](https://github.com/aashifm1)")
    
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation, width=250)
    with text_column:
        st.subheader("Integrated Telegram bot using python.")
        st.write(
            """
            Course Master Bot is a versatile Telegram bot created to assist with various tasks and inquiries. 
            Designed to be a helpful companion for users, it can provide quick information, answer questions, and streamline routine tasks. 
            Whether you're looking to automate simple processes or need a reliable assistant on hand, Course Master is here to enhance your Telegram experience.
            """
        )
        st.markdown("https://t.me/mastercoursebot")
st.write("---")

with st.container():
    left_col,right_col = st.columns(2)
    with right_col:
        st.header("Get in Touch with Me!")
        contact_form = """
        <form action="https://formsubmit.co/codingisfun.30a43e17a81307f42bec5d01fe085907" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Enter your Name" required><br>
            <input type="email" name="email" placeholder="Enter your Email" required><br>
            <textarea name="message" placeholder="Enter your message here" required></textarea><br>
            <button type="submit">Submit</button>
        </form>
        """
        left_column, right_column=st.columns((1,2))
        with left_column:
            st.markdown(contact_form,unsafe_allow_html=True)
        with right_column:
            st.empty()
    with left_col:
        st_lottie(lottie_contactus, height=300, key="contactus")
st.write("---")
footer = """
<style>
.footer {
    left: 0;
    bottom: 0;
    width: 100%;
    color: #f1f1f1;
    text-align: center;
    padding: 15px;
    font-size: 18px;
}
</style>
<div class="footer">
    © 2024 Aashif | All Rights Reserved
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
