import numpy as np
import pandas as pd
import streamlit as st
import datetime
import pickle

df = pd.read_csv('./Jamboree_Admission.csv')

st.write(
    """
    # Jamboree Candidate Data
    """
)

st.dataframe(df.head())

col1, col2, col3, col4 = st.columns(4)

# Input fields in each column
with col1:
    gre_score = st.number_input('GRE Score', format="%.2f")

with col2:
    toefl_score = st.number_input('TOEFL Score', format="%.2f")

with col3:
    cgpa = st.number_input('CGPA', format="%.2f")

with col4:
    research_exp = st.selectbox('Research Experience', [0, 1])

total_score = (gre_score*10/340) + (toefl_score*10/120)

# input_features = [4,cgpa,research_exp,total_score,6.5]
def model_pred(cgpa,research_exp,total_score):

    # loading the model
    with open('LR_model','rb') as file:
        reg_model = pickle.load(file)
        input_features = np.array([4,cgpa, research_exp, total_score,6.5])
        input_features = input_features.reshape(1, -1)
    return reg_model.predict(input_features)
if st.button('Calculate Chances'):
    chances = model_pred(cgpa,research_exp,total_score)

    st.text(f'The Chances of Getting Admission in the IVY Leagues are {(chances[0]*100).round(2)}%')
