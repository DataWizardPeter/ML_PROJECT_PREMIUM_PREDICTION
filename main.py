import streamlit as st
from prediction_helper import predict
import base64

# Function to encode image to base64 for background
def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Set page configuration with title, icon, and layout
st.set_page_config(page_title='Health Insurance Cost Predictor', page_icon='🩺', layout='wide')

# Get base64 of the image for the background
img_base64 = get_base64_of_image(r"61802.jpg")

# Apply CSS for the background image with 80% transparency
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.8;
        }}
        h1, h2 {{
            color: #00008B !important;
        }}
        h3 {{
            color: #00008B !important;
        }}
        /* Change the color of the expander titles to black */
        .stExpander > div > h3 {{
            color: black !important;
        }}
        /* Target the inputs to make their text color white */
        div[data-baseweb="select"] > div {{
            color: white !important;
        }}
        label {{
            color: black !important;
            font-weight: bold !important;
        }}
        .stNumberInput > div {{
            color: black !important;
        }}
        /* Style buttons */
        .stButton > button {{
            background-color: #006400 !important;
            color: white !important;
            border-radius: 8px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
        }}
        /* Style expanders */
        .stExpander {{
            background-color: rgba(70, 130, 180, 0.8) !important;
            border: 2px solid #020101;
        }}
        .stExpander h3 {{
            color: #020101 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<h1>🩺 Health Insurance Cost Predictor</h1>', unsafe_allow_html=True)
st.markdown('<h2>Enter the details below to get an estimate of your insurance premium:</h2>', unsafe_allow_html=True)

# Define dropdown options
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Input sections with individual background and text color styling
with st.expander("Basic Information", expanded=True):
    row1 = st.columns(3)
    with row1[0]:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
    with row1[1]:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
    with row1[2]:
        income_lakhs = st.number_input('Income in Lakhs Per Annum', step=1, min_value=0, max_value=200)

with st.expander("Health & Lifestyle Information", expanded=False):
    row2 = st.columns(3)
    with row2[0]:
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
    with row2[1]:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
    with row2[2]:
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])

with st.expander("Insurance Plan & History", expanded=False):
    row3 = st.columns(3)
    with row3[0]:
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
    with row3[1]:
        employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])
    with row3[2]:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

with st.expander("Personal & Regional Information", expanded=False):
    row4 = st.columns(3)
    with row4[0]:
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with row4[1]:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
    with row4[2]:
        region = st.selectbox('Region', categorical_options['Region'])

# Collect input into a dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# Button to make prediction
st.markdown("<br>", unsafe_allow_html=True)
center_button = st.columns([3, 3, 1])
with center_button[1]:
    if st.button('💡 Predict Insurance Cost'):
        prediction = predict(input_dict)

        # Pop-up balloons
        st.balloons()

        st.markdown(f"""
    <div style="text-align: center; font-size: 28px; color: black; font-weight: bold; margin-left: -500px;">
        💰 Predicted Health Insurance Cost: ₹{prediction:,.2f}
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown(""" 
    <hr style="height:2px;border-width:0;color:gray;background-color:gray">
    <footer style="text-align: center; font-family: 'Arial'; font-size: small; color: black;">
        © 2024 YourCompany | Privacy | Terms & Conditions
    </footer>
""", unsafe_allow_html=True)

