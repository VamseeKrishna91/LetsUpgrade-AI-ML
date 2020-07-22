import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chi2_contingency
from scipy.stats import wilcoxon
from scipy.stats import friedmanchisquare
from scipy.stats import mannwhitneyu
from scipy.stats import kruskal
from scipy.stats import ttest_1samp
from scipy.stats import ttest_rel
from scipy.stats import ttest_ind

df = pd.read_csv('C:/Users/C_M_Prasad/Desktop/Data Science/LetsUpgrade/Assignments/Questions/DAY007/general_data.csv')
df3 = df
df3 = df3.dropna(axis=0)
df.Attrition = df.Attrition.replace(['Yes','No'],[0,1])
df1 = df[['Attrition','Age','DistanceFromHome','Education','JobLevel','MonthlyIncome','PercentSalaryHike','StandardHours','StockOptionLevel','TrainingTimesLastYear','YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager']]
df2 = df1[['Age','DistanceFromHome','Education','JobLevel','MonthlyIncome','PercentSalaryHike','StandardHours','StockOptionLevel','TrainingTimesLastYear','YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager']]
df1.info()

print(df1.info())
print(df2.info())

mean = df2.mean()
print('Mean of different variables are : \n',mean)

median = df2.median()
print('Median of different variables are : \n',median)

mode = df2.mode()
print('Mode of different variables are : \n',mode)

skew = df2.skew()
print('skewness is :',skew)

kur = df2.kurtosis()
print('')


for i in mean:
    for j in median:
        for k in mode:
            if i==j:
                if j==k:
                    print('This is Normal Distribution.. you may want to proceed with any parametric test')
                    dist = 0
else:
    print('This is not normal distribution...Please follow Non parametric test')
    dist = 1

if dist ==1 :
    stats , p = wilcoxon(df1.Attrition,df1.Age)
    print('The Value of p in wilcoxon test is :',p)
    if p <0.05:
        print('There is significant impact of Age on Attrition')
    else:
        print('There is no significant impact of Age on Attrition')
    stats1,p1 = friedmanchisquare(df1.Attrition,df1.Age,df1.DistanceFromHome,df1.MonthlyIncome)
    if p1 <0.05:
        print('There is significant impact of Age,Distance from Home,Monthly Income on Attrition')
    else:
        print('There is no significant impact of Age,Distance from Home,Monthly Income  on Attrition')
    stats2, p2 = mannwhitneyu(df1.Attrition, df1.Education)
    dependecy = df.corr()
    print('Please check the dependency',dependecy)
    if p1 <0.05:
        print('There is significant impact of Education on Attrition')
    else:
        print('There is no significant impact of Education  on Attrition')
    stats3, p3 = kruskal(df1.Attrition, df1.Education,df1.JobLevel)
    if p1 < 0.05:
        print('There is significant impact of Education,JobLevel on Attrition')
    else:
        print('There is no significant impact of Education,JobLevel  on Attrition')
    crosstable = pd.crosstab(df3.Attrition,df3.Department)
    stats4,p4,dof,expected = chi2_contingency(crosstable)
    if p1 < 0.05:
        print('The variables are dependent')
    else:
        print('The variables are not dependent')

