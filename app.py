from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":pray:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_gis_analysis = Image.open("images/gis.png")




# ---- HEADER SECTION ----
with st.container():
    st.title("Data Analyst Portfolio ")
    st.write("##")
    st.subheader("Hi, I am Manas :wave:")
    st.write(
        "I am passionate about finding ways to use **R** and **SQL** to be more efficient and effective in solving big and complex problems related to any work field available."
    )
    #st.write("[Learn More >]()")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            """
            Hi, my name is Manas Ranjan Singh. I hold a  Bachelor of Technology degree in **_Civil Engineering_**.
            - I've always had an approach for working with numbers, collecting data, and finding trends and patterns that others miss. 
            Being a data analyst is a bit like being a detective—tracking the clues within the numbers to find the culprit is always rewarding. 
            I'm passionate about using this type of analysis to drive strategic decision-making.
            - I believe having a strong technical background and knowledge of database tools is a good foundation. But data analysts should also have an eye for detail, be curious and analytical, and be able to interpret data in original ways.
            """
        )
        st.write("[View Resume >]()")
        with right_column:
         st_lottie(lottie_coding, height=300, key="coding")  


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Project(s)")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_gis_analysis)
    with text_column:
        st.subheader("GEO-STATISTICAL ANALYSIS OF INDIAN RIVER BASINS: USING MAP CORRELATION METHOD")
        st.write(
            """
             It introduces the map correlation method, a
             method to estimate the correlation in daily streamflow
             between a streamgage and an ungaged location.
            """
        )
        st.markdown("[Click here...]()")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header(" :mailbox: Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/sunlight.06278@gmail.com
" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()