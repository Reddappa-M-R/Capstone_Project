# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
pickle_in = open('logistic_regression_model.pkl','rb')
classifier = pickle.load(pickle_in)
def welcome():
    return "Welcome All"

def predict_charn_telecom(gender, SeniorCitizen, Partner, Dependents, tenure,
       PhoneService, MultipleLines, InternetService, OnlineSecurity,
       OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
       StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
       MonthlyCharges, TotalCharges):
    prediction=classifier.predict([[gender, SeniorCitizen, Partner, Dependents, tenure,
           PhoneService, MultipleLines, InternetService, OnlineSecurity,
           OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
           StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
           MonthlyCharges, TotalCharges]])
    print(prediction)
    return prediction

def main():
    st.title("Telecom_Charn")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Telecom Charn ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.text_input("gender","Type Here")
    skewness = st.text_input("skewness","Type Here")
    Partner = st.text_input("Partner","Type Here")
    Dependents = st.text_input("Dependents","Type Here")
    tenure = st.text_input("gender","Type Here")
    PhoneService = st.text_input("PhoneService","Type Here")
    MultipleLines = st.text_input("MultipleLines","Type Here")
    InternetService = st.text_input("InternetService","Type Here")
    OnlineSecurity = st.text_input("OnlineSecurity","Type Here")
    OnlineBackup = st.text_input("OnlineBackup","Type Here")
    DeviceProtection = st.text_input("DeviceProtection","Type Here")
    TechSupport = st.text_input("TechSupport","Type Here")
    StreamingTV = st.text_input("StreamingTV","Type Here")
    StreamingMovies = st.text_input("StreamingMovies","Type Here")
    Contract = st.text_input("Contract","Type Here")
    PaperlessBilling = st.text_input("PaperlessBilling","Type Here")
    PaymentMethod = st.text_input("PaymentMethod","Type Here")
    MonthlyCharges = st.text_input("MonthlyCharges","Type Here")
    TotalCharges = st.text_input("TotalCharges","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(gender, SeniorCitizen, Partner, Dependents, tenure,
               PhoneService, MultipleLines, InternetService, OnlineSecurity,
               OnlineBackup, DeviceProtection, TechSupport, StreamingTV,
               StreamingMovies, Contract, PaperlessBilling, PaymentMethod,
               MonthlyCharges, TotalCharges)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()