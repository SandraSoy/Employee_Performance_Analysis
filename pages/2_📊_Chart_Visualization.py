import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
#Ignore warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(page_title="Chart Visualizations", page_icon="📊")

st.title('DATA INSIGHTS')
#Read the excel file
data=pd.read_csv('INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.csv', index_col=0)
#Setting the EmpNumber as index to ensure that no rows of data in the table are identical

st.header('1. Employee Departments Analysis')


#Creating a pie chart for employee department analysis
percent_1=[]
for i in data['EmpDepartment'].value_counts():
    percent_1.append(i)
    
wedgeprops = {"linewidth": 0.1, 'width':1, "edgecolor":"w"}
plt.figure(figsize = (10,15))
color = ["red","pink","lightblue","orange","green","yellow"]

plt.pie(percent_1,labels = ['Sales', 'Development',"Research & Development",'Human Resources',
       'Finance','Data Science'],explode = [0,0,0.08,0.1,0.1,0.2], autopct = "%0.2f%%", startangle =46,shadow = True,
        pctdistance = 0.85,wedgeprops = wedgeprops,textprops = {"fontsize":13,"fontweight":"bold"},rotatelabels=False,
        colors = color) 
plt.title("Employee Department in Percentage",fontsize=18,fontweight='bold')
plt.tight_layout(pad=6)
st.pyplot()

st.markdown('''**From the above chart, we see that:**
* The Sales Department made up majority of the Employee workforce with 31.08% (373) while the Data Science department was the least with 1.67%,had a few employees (20)
''')

st.header('2. Department-wise Performance')

st.subheader('a.) Total count of each department by the Performance rating')
plt.figure(figsize = (30,20))
sns.countplot(data = data, x ='EmpDepartment', hue ='PerformanceRating' )
st.pyplot()

st.markdown(''' **From the above plot, we get the following insights:**

* Every department employee gives an Excellent performance rating more in number
* Sales Department: 87 employees had a performance rating of Good(2), 35 employees-Outstanding(4) an majority of the employees (251) had an Excellent (3) performance rating
* Human Resource Department: 10 employees had a Good performance rating, 38 had and Excellent performance and 6 employees were Outstanding.
* Development Department: 13 employees had a Good performane rating, 44 with Outstanding while the majority of 304 were Exellent
* Data Science Department: Majority of the employees(17) in the department had an Excellent performance while 2 were Outstanding and 1 was rated Good.
* Research & Development department: 68% of the employees had an EXcellent performance rating while 12% were Oustanding and 20% Good performance rating
* Finance Department:employees with Excellent performance rating were the majority (30), with 15 having a Good performance rating and 4 being rated Outstanding''')

st.subheader('b.) Checking the Overall percentage Departmental Average Performance')
data.groupby('EmpDepartment')['PerformanceRating'].mean().plot(kind='pie',
                                                           figsize=(30,15),
                                                           colors=['#8FBC8F','#FFFF00','#87CEEB','pink','red','orange'],
                                                           explode=[0,0.07,0,0,0,0],
                                                           autopct="%1.2f%%"
                                                           )
plt.title('Departmental Average Performance')
st.pyplot()

st.markdown(''' From the above charts, we see the best performing departments:

* Development department; mean of 3.085873 (17.51%)
* Data Science department; mean of 3.050000 (17.31%)
* Human Resource department; mean of 2.925926 (16.61%)
* Research & Development department; mean of 2.921283 (16.58%)
* Sales department; mean of 2.860590 (16.24%)
* Finance department; mean of 2.775510 (15.75%) ''')

st.header('3. Satisfaction Levels with Performance')
#Setting th style for the plots
sns.set(rc={"font.size":20,"axes.titlesize":20,"axes.labelsize":25,"xtick.labelsize":25,"ytick.labelsize":25,
            "legend.fontsize":15})

#Creating a figure for the plots
fig,ax=plt.subplots(2,3, figsize=(40,30))
fig.suptitle('Performance rating of the Ordinal Columns data types', fontsize=40,color='red')

#Plotting the Distribution plots of the Numerical columns
sns.countplot(data=data,x='EmpEducationLevel',ax=ax[0,0],hue=data['PerformanceRating'])
ax[0,0].set_title('EmpEducationLevel')

sns.countplot(data=data,x='EmpEnvironmentSatisfaction',ax=ax[0,1],hue=data['PerformanceRating'])
ax[0,1].set_title('EmpEnvironmentSatisfaction')

sns.countplot(data=data,x='EmpJobInvolvement',ax=ax[0,2],hue=data['PerformanceRating'])
ax[0,2].set_title('EmpJobInvolvement')

sns.countplot(data=data,x='EmpJobSatisfaction',ax=ax[1,0],hue=data['PerformanceRating'])
ax[1,0].set_title('EmpJobSatisfaction')

sns.countplot(data=data,x='EmpRelationshipSatisfaction',ax=ax[1,1],hue=data['PerformanceRating'])
ax[1,1].set_title('EmpRelationshipSatisfaction')

sns.countplot(data=data,x='EmpWorkLifeBalance',ax=ax[1,2],hue=data['PerformanceRating'])
ax[1,2].set_title('EmpWorkLifeBalance')
st.pyplot()

st.markdown('''From the above plots, we get the following insights:

* Most of the employees with a Bachelors(rating=3) have an excellent score(3) than the rest
* The employees who had a High (rating=3) environment satisfaction performed better in the company
* Majority of the employees who had a High (rating=3) Job involvement had an excellent score(3)
* Employees who had a Very High(4) Job satisfaction performed excellently and were the most
* Most Employees with a Better(3) Work-life balance had an excellent performance compared to the rest
''')

st.header('4. Gender Analysis by Employee Department')

plt.figure(figsize=(20,15))
#countplot for gender vs Employee department
ax = sns.countplot(x= data["EmpDepartment"],hue=data['Gender'],palette="Accent")
plt.title("Gender distribution across Employee Department",fontweight="bold",fontsize=20)
plt.xlabel("Employee Department")
plt.ylabel("Count")
legend = plt.legend(prop={"size":10})
legend.set_title("Gender",prop={"size":15,"weight":"bold"})
plt.setp(legend.get_texts(), color='black')
legend.draw_frame(False)

plt.tight_layout(pad=2)
st.pyplot()

st.markdown('''From the analysis above, we get insights that:

* Male employees make up 60% of the workforce, while female 40%
* The male employees are more in each department with both the male and female employees being more in the sales department compared to the other departments.
''')


st.header('5. Employee Education Background Analysis')

#set the figure
sns.set(rc={"font.size":12,"axes.titlesize":18,"axes.labelsize":18,"xtick.labelsize":14,"ytick.labelsize":14,
            "legend.fontsize":12,'axes.grid' : False,'axes.facecolor': 'white'})

#pie chart for employees education background
percent_1=[]
for i in data['EducationBackground'].value_counts():
    percent_1.append(i)
    
wedgeprops = {"linewidth": 0.1, 'width':1, "edgecolor":"w"}
color = ["#61ffff","#cd853f","#00ff00","#ffff66","#ff6e4a","royalblue"]

plt.figure(figsize = (20,8))

plt.subplot(1,2,1)

#countplot chart for employees education background by department analysis
ax = sns.countplot(x=data['EducationBackground'],hue= data["EmpDepartment"],palette="tab10")
plt.title("\nEmployees Education Background analysis with Department\n",fontweight="bold",fontsize=19)
plt.xlabel("\nEmployees Education Background")
plt.xticks(ticks=[0,1,2,3,4,5],labels=["Marketing","Life Science","HR","Medical","Other","Technical Degree"],
           color="black")
plt.ylabel("Count\n")
legend = plt.legend()
legend.set_title("Employee Department\n",prop={"size":15,"weight":"bold"})
plt.setp(legend.get_texts(), color='black')
legend.draw_frame(False)

plt.tight_layout(pad=2)
st.pyplot()

plt.subplot(1,2,2)
plt.pie(percent_1,labels = ["Life Sciences","Medical","Marketing","Technical Degree","Other","Human Resorces"],
        explode = [0,0,0.08,0.1,0.1,0.2], autopct = "%0.2f%%", startangle =46,
        pctdistance = 0.85,wedgeprops = wedgeprops,textprops = {"fontsize":13,"fontweight":"bold"},rotatelabels=False,
        colors = color) 
plt.title("Employees Education Background in Percentage\n",fontsize=18,fontweight='bold',)
plt.tight_layout(pad=7)
plt.axis('equal')
st.pyplot()

#Countplot chart for Employee Education Background by Gender
fig = plt.figure(figsize=(20,10))
data.groupby(['EducationBackground'])['Gender'].value_counts().unstack(level=1).plot(kind='bar')
plt.title('Departmental Performance per Gender',fontsize=10)


st.pyplot()

st.markdown('''From the above charts, we see that:

* 41% of the employees have a Education background in the Life Sciences and the least number-1.75% of employees with a HR background
* Majority of the male and female employees have an Education background in the Life Sciences followed by a Medical background.
''')
