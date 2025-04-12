import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\Machine-learning\\Machine-learning\\05-Seaborn\\StudentsPerformance.csv")
sns.catplot(data=df,x='gender',y='math score',kind='box',row='lunch')
plt.show()