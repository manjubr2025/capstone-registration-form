import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('forms-automation-key.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Capstone Project Registration').sheet1

# Streamlit App
st.title("📋 Capstone Project Registration Form")

# Form Fields
with st.form(key='capstone_form'):
    name = st.text_input("Name")
    reg_no = st.text_input("Registration Number")
    gender = st.radio("Gender", ["Male", "Female"])
    mobile = st.text_input("Mobile")
    email = st.text_input("Email")
    specialization = st.selectbox("Major Specialization", ["Finance", "HR", "Marketing", "Business Analytics"])

    industry_options = [
        "Real Estate - House Price Prediction",
        "BFSI - Life Insurance Sales",
        "E-commerce - Customer Churn Prediction",
        "Sports - Cricket Win Prediction",
        "Healthcare - Life Insurance Cost",
        "HR - Salary Prediction",
        "Social Media - Tourism Adoption Project",
        "Supply Chain - Product Shipment Weight",
        "Banking - Probability of Default"
    ]
    industry_choice = st.selectbox("Preferred Industry/Function", industry_options)
    justification = st.text_area("Justify your preference")

    submit_button = st.form_submit_button(label='Submit')

# Save to Google Sheet on Submission
if submit_button:
    sheet.append_row([name, reg_no, gender, mobile, email, specialization, industry_choice, justification])
    st.success("✅ Response Submitted Successfully!")
