import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":dizzy:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)   
    if r.status_code != 200:    #if the status code = 200(succeeded) then return jason file else return nothing)
        return None
    return r.json()
    
    
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qp1q7mct.json")  #copying the link that we have copoied from lottie website.
img_contact_form = Image.open("C:/Users/patha/z/Images/dash.png")   #loading the images that we have saved in the image file
img_lottie_animation = Image.open("C:/Users/patha/z/Images/smart.jpeg")  #loading the images that we have saved in the image file



# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Umang :wave:")
    st.title("Student at KIIT University, Bhubaneswar")
    st.write(
        "As a Computer Science Student, I am passionate about handling and analyzing data."
    )
    st.write("[LINKEDIN >](https://www.linkedin.com/in/umang-pathak03/) || [GITHUB>](https://github.com/pumang03) || pathakumang87@gmail.com")
    

# ----ABOUT----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)  #Here the page is divided into 2 parts right and left. left=written parts,Right=Lottie image
    with left_column:
        st.header("ABOUT")
        st.write("##")
        st.write(
            """
            With an open mind and a strong desire to learn, I have gained experience in database management.
            - looking for a way to leverage the power of Python in day-to-day work.
            - Have strong Troubleshooting abilities, effective Communication Skills
            - Want to have industry level experience on Data Analysis & Data Science task.
            -  I am excited to pursue a career in data science, where I can leverage my skills and experience to drive valuable insights and                make impactful decisions.
            - Open To Work.
            """
        )
        
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:   #here we have called the image that we have saved in the loading assest comments.
        st.image(img_contact_form)
    with text_column:
        st.subheader("Visualisation Of Sales Datasets Using MS Power BI")
        st.write(
            """
            - Worked On Sales Datasets For Visualization further transforming Data By Aggregation And Normalization Process Using SQL.
            - Loading Into The BI environment And Perform Further Power Querying(Data Munging).
            - Designing Of The Data Model In The BI Environment. 
            - Created A Dynamic Dashboard Using MS Power BI.
            -  [LINK >](https://github.com/pumang03/Data-Analysis-Sales-) 
            """
        )
st.write("##")
with st.container():
     image_column, text_column = st.columns((1, 2))
     with image_column:         #here we have called the image that we have saved in the loading assest comments.
         st.image(img_lottie_animation)
     with text_column:
         st.subheader("Person Count And Smart Lighting(Remote Access)")
         st.write(
            """
            - The Automatic Room Lights using ESP-32 and IR Sensors is a project, where the lights in the room will automatically turn ON                   upon presence of a human and stay turned ON until the person has left.
            - There are two IR sensors which is used to detect weather the person is entering the room or leaving the room using which we                  count the number of people present in the room and control the lights accordingly.
            - While entering the person crosses the first IR sensor which makes the people in the room count increase by 1 and the lights                  are turned ON and if another person enters the count is further increased.
            - While a person leaving the room crosses the second IR sensor which decreases the room person count by 1. Similarly if all the                people leaves the room the lights are turned OFF as the people count is zero.
            -  [LINK >](https://github.com/pumang03/Smart-Lighting-Remote-Access) 
            """
        )
        

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/pathakumang87@gmail.com" method="POST">
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