# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import numpy as np
import pickle
#import sklearn
#import pandas as pd
#import streamlit as st
#from PIL import Image
pickle_in = open('logistic_regression_model.pkl','rb')
classifier = pickle.load(pickle_in)
def welcome():
    return "Welcome All"

#