import numpy as np
import pandas as pd
from numpy import NaN
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('C:/Users/C_M_Prasad/Desktop/Data Science/LetsUpgrade/Assignments/Questions/DAY007/general_data.csv')
df= df.dropna(axis=0)
print(df.info())


df = df.drop_duplicates('EmployeeID')

print(df.info())

df.Attrition =df.Attrition.replace(['Yes','No'],[1,0])
df1 = df.select_dtypes(include=['integer'])


print(df1.head(5))

stats,p = pearsonr(df1.Attrition,df1.Age)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a slight negative correlation . Also this a correlation between Categorical and Continuous variables. Hence this is Parial correlation')
print('p Value here indicates that Age has no impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')


import numpy as np
import pandas as pd
from numpy import NaN
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('C:/Users/C_M_Prasad/Desktop/Data Science/LetsUpgrade/Assignments/Questions/DAY007/general_data.csv')
df= df.dropna(axis=0)
print(df.info())


df = df.drop_duplicates('EmployeeID')

print(df.info())

df.Attrition =df.Attrition.replace(['Yes','No'],[1,0])
df1 = df.select_dtypes(include=['integer'])


print(df1.head(5))

stats,p = pearsonr(df1.Attrition,df1.Age)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a slight negative correlation . Also this a correlation between Categorical and Continuous variables. Hence this is Parial correlation')
print('p Value here indicates that Age has no impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')


stats,p = pearsonr(df1.Attrition,df1.Education)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation . Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that  Education has significant impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')

stats,p = pearsonr(df1.Attrition,df1.JobLevel)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation . Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Job level has significant impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')

stats,p = pearsonr(df1.Attrition,df1.MonthlyIncome)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Monthly Income has no  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')


stats,p = pearsonr(df1.Attrition,df1.PercentSalaryHike)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low positive correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Percentage Salary Hike has no  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')

stats,p = pearsonr(df1.Attrition,df1.StockOptionLevel)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Stock Option level has significant  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')


stats,p = pearsonr(df1.Attrition,df1.TrainingTimesLastYear)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Training times last year has no  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')


stats,p = pearsonr(df1.Attrition,df1.YearsAtCompany)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Years at company has no  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')

stats,p = pearsonr(df1.Attrition,df1.YearsSinceLastPromotion)
print('r Value is :',stats,'p Value is :',p)
print('Here we can see there is a very low negative correlation .We can consider that these variables have no correlation. Also this a correlation between Categorical and Continuous variables. Hence this can be considered as  Parial correlation')
print('p Value here indicates that Years since last promotion has no  impact on Attrition Rate')
print('-----------------------------------------------------------------------------------------')












