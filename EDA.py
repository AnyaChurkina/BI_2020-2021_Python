from matplotlib import pyplot as plt
from pandas import read_csv
import seaborn as sns


# Task 3 EDA (dataset "framingham" about risks of cardio diseases)
url = 'https://raw.githubusercontent.com/TarekDib03/Analytics/' \
      'master/Week3%20-%20Logistic%20Regression/Data/framingham.csv'

cardio = read_csv(url)

#  Data size
print(cardio.shape)

# Data structure
print(cardio.info)

# Types of variables
print(cardio.dtypes)

'''
Male: sex-male or female (factor)
Age: Age of the patient (numeric continuous)
Education: Educational attainment (numeric discrete)
Current Smoker: smoker or not (factor)
Cigs Per Day: number of cigarettes smoked per day (numeric discrete)
BP Meds: taking medications against high blood pressure (factor)
Prevalent Stroke: having a prior stroke (factor)
Prevalent Hyp: presence of hypertension (factor)
Diabetes: presence of diabetes (factor)
Tot Chol: total cholesterol level (numeric continuous)
Sys BP: systolic blood pressure (numeric continuous)
Dia BP: diastolic blood pressure (numeric continuous)
BMI: Body Mass Index (numeric continuous)
Heart Rate: heart rate (numeric continuous)
Glucose: glucose level (numeric continuous)
TenYearCHD: 10 year risk of coronary heart disease (factor)
'''

# Replaced numbers with corresponding words
gender = {1: 'Male', 0: 'Female'}
cardio.male = [gender[item] for item in cardio.male]

risc = {1: 'Yes', 0: 'No'}
cardio.TenYearCHD = [risc[item] for item in cardio.TenYearCHD]

# Rename column "male"
cardio = cardio.rename(columns={'male': 'Sex'})

# Change types of category variables to correct type
cardio[['Sex', 'currentSmoker', 'BPMeds', 'prevalentStroke',
        'prevalentHyp', 'diabetes', 'TenYearCHD']] = \
    cardio[['Sex', 'currentSmoker', 'BPMeds', 'prevalentStroke',
            'prevalentHyp', 'diabetes', 'TenYearCHD']].astype('category')

# General statistics of numeric variables
print(cardio.describe().T)

# Number of NA
print(cardio.isna().sum())

'''
Conclusion:
In variable "glucose" too much NA's - 388
'''

#  Distribution histograms of numeric variables
fig = plt.figure(figsize=(15, 20))
cardio.hist(ax=fig.gca(), color='lightpink')
plt.suptitle("Distribution histograms of numeric variables", fontsize=25)
plt.savefig("Distribution histograms.png")

'''
Conclusion:
Distribution of heartRate, BMI, diaBP looks like normal
'''

# Pairwise scatter plot colored by sex (to view a outliers)
sns.pairplot(cardio[['Sex', 'age', 'BMI', 'heartRate', 'cigsPerDay', 'glucose',
                     'sysBP', 'totChol', 'diaBP']], hue='Sex',
             palette='Set1', height=1.5)
sns.set_style('whitegrid')
plt.savefig("Pairwise scatterplot by sex.png")

'''
Conclusion:
Outliers are observed in variables BMI, sysBP, totalChol
'''

# Correlation plot
plt.figure(figsize=(20, 15), dpi=80)
sns.heatmap(cardio.corr(), xticklabels=cardio.corr().columns,
            yticklabels=cardio.corr().columns, cmap='RdYlGn', center=0,
            annot=True)

plt.title('Correlation plot of numeric variable', fontsize=22)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig("Correlation plot.png")

'''
Conclusion:
Positive correlation is observed between variables:
 - sys- and diaBI(it's logical)
 - sysBI and BMI
 - diaBI and BMI
 - age and sysBP
 - age and diaBP
 - age and totalChol

Positive correlation is observed between variables:
 - age and education
 - age and Cigs Per Day
 - education and BMP
 - education sysBP
'''

# The influence of various factors on the risk of developing cardiac disease
sns.catplot(x="Sex", y="age", col="TenYearCHD", data=cardio, kind="box",
            height=4, aspect=.7)
plt.suptitle('Risk of heart disease by gender and age')
plt.savefig("Risk of heart disease by gender and age.png")

sns.catplot(x="Sex", y="totChol", col="TenYearCHD", data=cardio, kind="box",
            height=4, aspect=.7)
plt.suptitle('Risk of heart disease by gender and total cholesterol')
plt.savefig("Risk of heart disease by gender and totChol.png")

sns.catplot(x="Sex", y="BMI", col="TenYearCHD", data=cardio, kind="box",
            height=4, aspect=.7)
plt.suptitle('Risk of heart disease by gender and BMI')
plt.savefig("Risk of heart disease by gender and BMI.png")

sns.catplot(x="Sex", y="glucose", col="TenYearCHD", data=cardio, kind="box",
            height=4, aspect=.7)
plt.suptitle('Risk of heart disease by gender and glucose')
plt.savefig("Risk of heart disease by gender and glucose.png")

'''
Conclusion:
 - the likelihood of heart disease increases with age
 - other parameters have a large amount of outliers
'''
