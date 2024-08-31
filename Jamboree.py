import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('./Jamboree_Admission.csv')

# Display the dataframe
st.write(
    """
    # Jamboree Candidate Data
    """
)

st.dataframe(df.head())

# Input fields in each column
col1, col2, col3 = st.columns(3)

with col1:
    uni_rating = st.number_input('University Rating', format="%.2f")

with col2:
    gre_score = st.number_input('GRE Score', format="%.2f")

with col3:
    toefl_score = st.number_input('TOEFL Score', format="%.2f")

# Second row of input fields
col4, col5, col6 = st.columns(3)

with col4:
    cgpa = st.number_input('CGPA', format="%.2f")

with col5:
    research_exp = st.selectbox('Research Experience', [0, 1])

with col6:
    lor = st.number_input('Letter of Recommendation (LOR)', format="%.2f")

# Third row for SOP
sop = st.number_input('Statement of Purpose (SOP)', format="%.2f")

# Calculate the total score
total_score = (gre_score * 10 / 340) + (toefl_score * 10 / 120)
sop_lor = lor + sop

# Prediction function
def model_pred(uni_rating, cgpa, research_exp, total_score, sop_lor):
    # Load the trained model
    with open('LR_model', 'rb') as file:
        reg_model = pickle.load(file)

    # Input features
    input_features = np.array([uni_rating, cgpa, research_exp, total_score, sop_lor]).reshape(1, -1)

    # Standardize the input features (commented out for now)
    # scaler = StandardScaler()
    # input_features_standardized = scaler.fit_transform(input_features)

    # Predict the chances of admission
    return reg_model.predict(input_features)

# Button to calculate chances of admission
if st.button('Calculate Chances'):
    chances = model_pred(uni_rating, cgpa, research_exp, total_score, sop_lor)
    st.text(f'The Chances of Getting Admission in the IVY Leagues are {(chances[0] * 100).round(2)}%')

