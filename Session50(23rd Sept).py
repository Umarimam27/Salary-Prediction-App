import streamlit as st
import pickle
import numpy as np
import requests
import base64

# Load the pickled model
model = pickle.load(open(r"C:\Users\umari\OneDrive\Desktop\FSDS DATASETs\linear_regression_model.pkl", 'rb'))

# Function to set random Unsplash background
def set_bg_from_unsplash(query="finance,money,data,analytics"):
    url = f"https://source.unsplash.com/1600x900/?{query}"
    response = requests.get(url)
    encoded = base64.b64encode(response.content).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
set_bg_from_unsplash()

# Title & Description
st.markdown("<h1 style='text-align:center; color:#FFD700;'>💰 Salary Prediction App 💼</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Predict salaries based on years of experience using Machine Learning</p>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar info
st.sidebar.title("📊 About This App")
st.sidebar.info("This app uses a **Linear Regression Model** trained on Salary Data to predict salaries based on experience.")
st.sidebar.success("Made with ❤️ using Streamlit By UMAR IMAM")

# Input widget
years_experience = st.number_input("🧑‍💻 Enter Years of Experience:", min_value=0.0, max_value=50.0, value=1.0, step=0.5)

# Predict button
if st.button("🔮 Predict Salary"):
    experience_input = np.array([[years_experience]])
    prediction = model.predict(experience_input)

    # Styled result box
    st.markdown(
        f"""
        <div style="background-color:rgba(30,144,255,0.9); padding:20px; border-radius:15px; text-align:center;">
            <h2 style="color:white;">📈 Predicted Salary</h2>
            <h1 style="color:#FFD700;">${prediction[0]:,.2f}</h1>
            <p style="color:white;">for <b>{years_experience}</b> years of experience</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Dashboard-style metrics
    st.metric(label="Years of Experience Entered", value=f"{years_experience} yrs")
    st.metric(label="Estimated Salary Range", value=f"${prediction[0]-2000:,.2f} - ${prediction[0]+2000:,.2f}")
