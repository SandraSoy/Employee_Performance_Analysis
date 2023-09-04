import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
#Ignore warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="ML_Model", page_icon=":fireworks:")


st.header('Model Deployment')
#Import dataset
#Read the excel file
data=pd.read_excel('INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.xls', index_col=0)
#Setting the EmpNumber as index to ensure that no rows of data in the table are identical

#Get user input on how many rows to disply
#rows=st.slider('How many rows of data would you like to see?',0,20,5)#label of slider. range minis 0 and max is 20. and initial value is 5

#Display data
#st.dataframe(data.head(rows))

#Convert Labeled data to Numerical Data using Ordinal Encoder
from sklearn.preprocessing import OrdinalEncoder 
cat=data.select_dtypes(include=['object'])
encoder=OrdinalEncoder()
data[cat.columns]=encoder.fit_transform(cat)


#1. Create my features and the target variables (target=type)
y=data['PerformanceRating']
#select only the numeric columns(features)
X=data.drop('PerformanceRating', axis=1)
# import my ML model
from sklearn.ensemble import RandomForestClassifier
# instantiate my model
rf = RandomForestClassifier()
# fit my model
rf.fit(X, y)

#Show progress bar for model training
import time 
with st.spinner('Training Model...'):
    time.sleep(5)#should not run until 5 secs are over.code sleeps for 5mins b4 continuing
    st.success('Done')
    st.balloons()

#Print model accuracy
st.subheader('Model Accuracy')
st.write(f'Model Accuracy: {rf.score(X, y)}')

# get user input
Age=st.number_input('Age')
Gender= st.selectbox('Gender: 0-Female, 1-Male', ('0,1'))
EducationBackground= st.selectbox('EducationBackground: 0-Human Resources, 1-Life Sciences, 2-Marketing, 3-Medical, 4-Other, 5-Technical Degree',('0', '1','2','3', '4','5'))
MaritalStatus= st.selectbox('MaritalStatus: 0-Divorced, 1-Married, 2-Single',('0','1','2'))
EmpDepartment= st.selectbox('Empdepartment: 0-Data Science, 1-Development, 2-Finance, 3-Human Resources, 4-Research & Development, 5-Sales',('0','1','2','3','4','5'))
EmpJobRole= st.selectbox('EmpJobRole: 0-Business Analyst, 1-Data Scientist, 2-Delivery Manager, 3-Developer,4-Finance Manger, 5-Human Resources, 6-HealthCare Representative, 7-Laboratory Technician, 8-Manager, 9-Maneger R&D, 10-Manufacturing Director, 11-Research Director, 12-Research Scientist, 13-Sales Executive, 14-Sales Representative, 15-Senior Developer, 16-Senior Manager R&D, 17-Technical Architect, 18-Technical Lead', ('0','1','2','3','4','5','6','7','8','9','10','11','12','13', '14','15','16','17','18'))
BusinessTravelFrequency= st.selectbox('BusinessTravelFrequency: 0-Travel_Frequently, 1-Travel_Rarely, 2-Non-Travel',('0','1','2'))
DistanceFromHome=st.number_input('DistanceFromHome')
EmpEducationLevel=st.selectbox('EmpEducationLevel: 1-Below College, 2-College, 3-Bachelor, 4-Master, 5-Doctor',('1','2','3','4','5'))
EmpEnvironmentSatisfaction=st.selectbox('EmpEnvironmentSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High', ('1','2','3','4'))
EmpHourlyRate=st.number_input('EmpHourlyRate')
EmpJobInvolvement=st.selectbox('EmpJobInvolvement: 1-Low, 2-Medium, 3-High, 4-Very High', ('1','2','3','4'))
EmpJobLevel=st.number_input('EmpJobLevel')
EmpJobSatisfaction=st.selectbox('EmpJobSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High', ('1','2','3','4'))
NumCompaniesWorked=st.number_input('NumCompaniesWorked')
OverTime=st.selectbox('OverTime: 0-No, 1-Yes',('0','1'))
EmpLastSalaryHikePercent=st.number_input('EmpLastSalaryHikePercent')
EmpRelationshipSatisfaction=st.selectbox('EmpRelationshipSatisfaction: 1-Low, 2-Medium, 3-High, 4-Very High', ('1','2','3','4'))
TotalWorkExperienceInYears=st.number_input('TotalWorkExperienceInYears')
TrainingTimesLastYear=st.number_input('TrainingTimesLastYear')
EmpWorkLifeBalance=st.selectbox('EmpWorkLifeBalance: 1-Bad, 2-Good, 3-Better, 4-Best', ('1','2','3','4'))
ExperienceYearsAtThisCompany=st.number_input('ExperienceYearsAtThisCompany')
ExperienceYearsInCurrentRole=st.number_input('ExperienceYearsInCurrentRole')
YearsSinceLastPromotion=st.number_input('YearsSinceLastPromotion')
YearsWithCurrManager=st.number_input('YearsWithCurrManager')
Attrition=st.selectbox('Attrition: 0-No, 1-Yes', ('0','1'))


# create a new dataframe 
X_new = pd.DataFrame({'Age': Age,
                      'Gender': Gender,
                      'EducationBackground': EducationBackground,
                      'MaritalStatus': MaritalStatus,
                      'EmpDepartment': EmpDepartment,
                      'EmpJobRole': EmpJobRole,
                      'BusinessTravelFrequency': BusinessTravelFrequency,
                      'DistanceFromHome': DistanceFromHome,
                      'EmpEducationLevel': EmpEducationLevel,
                      'EmpEnvironmentSatisfaction': EmpEnvironmentSatisfaction,
                      'EmpHourlyRate':EmpHourlyRate,
                      'EmpJobInvolvement': EmpJobInvolvement,
                      'EmpJobLevel': EmpJobLevel,
                      'EmpJobSatisfaction': EmpJobSatisfaction,
                      'NumCompaniesWorked': NumCompaniesWorked,
                      'OverTime': OverTime,
                      'EmpLastSalaryHikePercent': EmpLastSalaryHikePercent,
                      'EmpRelationshipSatisfaction': EmpRelationshipSatisfaction,
                      'TotalWorkExperienceInYears': TotalWorkExperienceInYears,
                      'TrainingTimesLastYear': TrainingTimesLastYear,
                      'EmpWorkLifeBalance': EmpWorkLifeBalance,
                      'ExperienceYearsAtThisCompany': ExperienceYearsAtThisCompany,
                      'ExperienceYearsInCurrentRole': ExperienceYearsInCurrentRole,
                      'YearsSinceLastPromotion': YearsSinceLastPromotion,
                      'YearsWithCurrManager': YearsWithCurrManager,
                      'Attrition': Attrition}, 
                      index=[0])

#Print the user inout
st.subheader('User Input')
st.dataframe(X_new)

#Make predictions and print them
prediction=rf.predict(X_new)
st.subheader('Prediction Done')
st.write(f'PerformanceRating: {prediction}')