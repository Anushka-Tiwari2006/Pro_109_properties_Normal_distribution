import statistics
from turtle import st
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go


df = pd.read_csv("StudentsPerformance.csv")
data_list = df["reading_score"].to_list()

mean = statistics.mean(data_list)
median = statistics.median(data_list)
mode = statistics.mode(data_list)
std_dev = statistics.stdev(data_list)

first_std_dev_start,first_std_dev_end = mean - std_dev,mean + std_dev
second_std_dev_start,second_std_dev_end = mean - (2*std_dev),mean + (2*std_dev)
third_std_dev_start,third_std_dev_end = mean-(3*std_dev),mean + (3*std_dev)

list_1 = [result for result in data_list if result >first_std_dev_start and result <first_std_dev_end]
list_2 = [result for result in data_list if result >second_std_dev_start and result <second_std_dev_end]
list_3 = [result for result in data_list if result >third_std_dev_start and result <third_std_dev_end]

print(len(list_1)*100/len(data_list))
print(len(list_2)*100/len(data_list))
print(len(list_3)*100/len(data_list))

fig = ff.create_distplot([data_list],["reading_score"],show_hist = False)
fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.20],mode = "lines",name = "St_dev_1"))
fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end], y = [0,0.20],mode = "lines",name = "St_dev_2"))
fig.add_trace(go.Scatter(x = [third_std_dev_end,third_std_dev_end], y = [0,0.20],mode = "lines",name = "St_dev_3"))
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20],mode = "lines",name = "Mean"))
fig.show()