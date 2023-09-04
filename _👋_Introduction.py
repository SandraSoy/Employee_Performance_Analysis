import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
#Ignore warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Introduction",
    page_icon="👋") 
#Title
st.title('EMPLOYEE PERFORMANCE ANALYSIS')
#st.sidebar.success('Select a page above')

#Data Description
st.header('INX Future Inc Employee Performance Project')
st.subheader('Project Brief')

st.markdown(''' INX Future Inc , (referred as INX ) , is one of the leading data analytics and automation solutions provider with over 15 years of global business presence. INX is consistently rated as top 20 best employers past 5 years. INX human resource policies are considered as employee friendly and widely perceived as best practices in the industry.''')

st.markdown(''' However, in the recent years, the employee performance indexes have not been good and this has become a concern to top management. The CEO knows the issues but is hesitant to take any actions in penalizing non-performing employees, fearing it would affect the employee morale and further reducing performance. He decided to initiate a project that would analyze the current employee data. His expectation is that the findings of this project will help take the right course of actions.''')

st.markdown(''' This is a Data Science project using the dataset from INX Future to analyse the current employee data and find the core underlying causes of the performance decline. The goal and expected insights of the project are:
1. Department-wise performance
2. Top 3 important factors effecting employee performance
3. Trained model that can predict the employee performance based on factors as inouts. This will be used to hire employees
4. Recommendations to improve the employee performance based on insights from analysis.
''')










