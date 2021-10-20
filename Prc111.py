from logging import NullHandler
from os import name
import pandas as pd
import plotly_express as px
import plotly.figure_factory as ff
import csv 
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("Prc111.csv")
data=df["reading_time"].tolist()

mean=statistics.mean(data)
stdDeviation=statistics.stdev(data)

print("Mean of population is :",mean)
print("Standard Deviation of population is :",stdDeviation)

def RandomMeans(counter):
    dataSet=[]
    for i in range(0,counter):
        radomIndex = random.randint(0,len(data)-1)
        value = data[radomIndex]
        dataSet.append(value)
    
    mean=statistics.mean(dataSet)
    return mean

meanlist=[]
for i in range(0,100):
    randomMeans=RandomMeans(30)
    meanlist.append(randomMeans)


mean=statistics.mean(meanlist)
stdDeviation=statistics.stdev(meanlist)

print("Mean of sampling distribution is :",mean)
print("Standard Deviation of sampling distribution is :",stdDeviation)

first_std_deviation_start,first_std_deviation_end = mean-stdDeviation,mean+stdDeviation
second_std_deviation_start,second_std_deviation_end=mean-(2*stdDeviation),mean+(2*stdDeviation)
third_std_deviation_start,third_std_deviation_end = mean-(3*stdDeviation),mean+(3*stdDeviation)
print("std1",first_std_deviation_start,first_std_deviation_end)
print("std2",second_std_deviation_start,second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)

fig = ff.create_distplot([meanlist],["Reading Time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="MEAN"))
fig.show()