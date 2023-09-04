import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
#Ignore warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Analysis & Summary",
    page_icon=":clipboard:") 
#Title
st.title('EMPLOYEE PERFORMANCE ANALYSIS')

#Header
st.header('DATA PROCESSING & ANALYSIS')
st.write('The table below represents all employee data that will be used in our analysis to predict employee performance')
#Import dataset
#Read the excel file
data=pd.read_csv('INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.xls.csv', index_col=0)
#Setting the EmpNumber as index to ensure that no rows of data in the table are identical

#Get user input on how many rows to disply
Raw_Data= st.checkbox('Show Raw Data')
if Raw_Data:
    rows=st.slider('How many rows of data would you like to see?',0,20,5)#label of slider. range minis 0 and max is 20. and initial value is 5
    st.dataframe(data.head(rows))#Display data
    

#Convert Labeled data to Numerical Data using Ordinal Encoder
from sklearn.preprocessing import OrdinalEncoder 
cat=data.select_dtypes(include=['object'])
encoder=OrdinalEncoder()
data[cat.columns]=encoder.fit_transform(cat)


st.markdown(''' The given dataset consists of 1200 rows and 28 columns. The 28 features are classified into;
* Quantitative where 11 columns are Numerical data and 8 columns are Ordinal data
* Qualitative where 8 columns are categorical
* EmpNumber which is the unique values, consists of alphanumerical data. It does not play a role as a relevant feature for performance rating thus setting it as the index.''')


#Header
st.header('PROJECT SUMMARY')
st.markdown(''' The Data science project submitted here is an analysis of employee performance data provided. The goal of the project is to find the performance rating of the employees dependant on the features of the data. ''')

st.markdown('''The following insights were realised from the project analysis:

**I.) Department wise performances:**

* Every department employee gives an Excellent performance rating more in number

* **Sales:** The department had majority of employees (373). 87 employees had a performance rating of Good(2), 35 employees-Outstanding(4) an majority of the employees (251) had an Excellent (3) performance rating
* **Development:** The department had the 2nd highest number of employees with 361. 13 employees had a Good performane rating, 44 with Outstanding while the majority of 304 were Exellent
* **Research & Development:** The department had 343 employees. 68% of the employees had an EXcellent performance rating while 12% were Oustanding and 20% Good performance rating
* **Human Resoure:** 54 employees were present in this department. 10 employees had a Good performance rating, 38 had and Excellent performance and 6 employees were Outstanding.
* **Finance:** The department had 499 employees. employees with Excellent performance rating were the majority (30), with 15 having a Good performance rating and 4 being rated Outstanding
* **Data Science:** The department had the least number of employees with 20. Majority of the employees(17) in the department had an Excellent performance while 2 were Outstanding and 1 was rated Good.

Further analysis of the average mean of each department was done. The top performing departments are;

* **Development department;** mean of 3.085873 (17.51%)
* **Data Science department;** mean of 3.050000 (17.31%)
* **Human Resource department;** mean of 2.925926 (16.61%)
* **Research & Development department;** mean of 2.921283 (16.58%)
* **Sales department;** mean of 2.860590 (16.24%)
* **Finance department;** mean of 2.775510 (15.75%)


**II.) Top 3 Important Factors effecting employee performance:**
* Feature selection analysis was also perfomed by using 3 different methods/techniques for comparison. 
 The methods include;

    * Random Feature Importances
    * SelectK Method
    * Mutual_info_Classif

The top 3 most important factors effecting employee performance from the above analysis by the techniques are;

1. **Employee Last Salary Hike**
2. **Employee Environment Satisfaction**
3. **Years Since Last Promotion**


**III.) A trained model which can predict the employee performance based on factors as inputs. (This will be used to hire employees.)**

* The trained model was created using the **Random Forest Classifier** machine learning algorithm;  
    * Test accuracy score- 96% 
    * Train accuray score- 98%


**IV.) Recommendations to improve the employee performance based on insights from analysis.**

* Overall employee performance can be achieved by looking into the Employee last salary hike. The company needs to focus more on increasing the salary hike as this would increase employee motivation and morale to perform well and increase overall well-being financially and pyschologically.
* The Employee environment satisfaction is also key. Top management needs to ensure that all employees are highly and very highly satisfied with their environemnt as this affects overall performance.
* The top management needs to also promote the employees that have stagnated in the last position or role for many years. Years since last promotion plays a big part in employees performance as employees who havent received any promotions tend to have a low morale at the work-place.
* Experience years in current role is also important as the number of years impacts/contributes to better performance due to the skills and experience acquired over time. Therefore,top management should recognize the experience and reward the great performance, as this would in turn increase employee morale
* The top management should consider gender balance for inclusivity, as majority of the employees are male.
* The top management should introduce a rewards, recongnition and incentives system to reinforce overall performance in the company
* Employee's work-life balance is also important as this affets the overall employee performance rating. From the analysis, employees with a Better work-life balance had an Excellent performance rating as compared to the rest. The company should ensure that employees have a work-life balance so as to increase their performance. This could be by introducing flexible working hours
''')
