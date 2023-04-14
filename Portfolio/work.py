import streamlit as st

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


with st.container():
    left, right = st.columns(2)
    with right:
        st.subheader("Hi, I am Mayank Goswami :wave:")
        st.title("Data Scientist from India")
        st.write("I am learning Machine Learning and advanced Python library to keep me updated on regualar basis")
        st.write("[Learn More >](https://www.linkedin.com/in/mayank-goswami-8909961b9/)")
    with left:
        st.image("Portfolio/Images/1.png", width = 800)


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            :boy: I am college student pursuing my Bachelor in Computer Science Engineering.

            :eyes: My interest is in the field of Data Science and Machine Learning.

            :computer: Currently making project in the field of computer vision along with mediapipe.
            
            :seat: I also do competitive programming on various platform using python and C++.

            :ok_hand: If this sound interesting to you, you can follow me on.

            :link: [Github](https://github.com/hacker-4-good)
            
            """
        )
    with right_column:
        st.image("Portfolio/Images/2.png", width = 800)



with st.container():
    st.write("---")
    st.header("Profile")
    left_profile, right_profile = st.columns(2)
    with left_profile:
        st.image("Portfolio/Images/3.png", width = 300)
    with right_profile:
        st.write('''I want to join as a Data Scientist adept in bringing forth expertise in building analytical software. Equipped with a diverse and promising skill-set.
        Proficient in various programming language and databases. Able to efficiently self-manage during independent projects as well as collaborate as a part of a
        productive team.''')



with st.container():
    st.write("---")
    st.header("Projects")
    left_side, middle_side, right_side = st.columns(3)
    with left_side:
        st.image("Portfolio/Images/Ai.png", width = 300)
        st.write("AI - GYM Trainer ↪ [Click here](https://github.com/hacker-4-good/Internship-Projects)")
    with middle_side:
        st.image("Portfolio/Images/cars.png", width = 300)
        st.write("Vehicle Parking Detection ↪ [Click here](https://github.com/hacker-4-good/OS-project-vehicle-detection-parking)")
    with right_side:
        st.image("Portfolio/Images/jarvis.png", width = 300)
        st.write("Jarvis ↪ [Click here](https://github.com/hacker-4-good/Jarvis)")



with st.container():
    st.write("---")   
    st.header("Internships")    
    left_internship,right_internship = st.columns(2)
    with right_internship:
        st.text("Company name: Awiros") 
        st.text("Position: Computer Vision Intern")
        st.text("Duration: 1 month (Aug 2022 - Sep 2022)")
        st.text('''About Internship: 
        i)   Created a hand tracking python program using OpenCV and Mediapipe
             library and later convert it into module.
        ii)  Created a volume control system using hand gesture project using
             own created hand tracking module.
        iii) Created a finger recognition system using OpenCV and Mediapipe 
             which count number of finger in front of a camera in real time.
        iv)  Worked on main project, created a AI-GYM Trainer using OpenCV, 
             Mediapipe.''')
    with left_internship:
        st.image("Portfolio/Images/intern.png", width = 300)



with st.container():
    st.write("---")
    st.header("Contact Me")
    left_contact, right_contact = st.columns(2)
    with left_contact:
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Anything to share :)")
        if st.button("Submit"):
            st.balloons()
            import pymongo as mongo
            URI = mongo.MongoClient("mongodb+srv://Mayank:mayank580@user.f0aak7o.mongodb.net/test")
            db = URI["Contact_Information"]
            contact = db["Contact"]
            db.contact.insert_one({'Name':name, 'Email':email, 'Message':message})
