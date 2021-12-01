import statistics 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import pandas as pd 
import random 

df = pd.read_csv("c111_dataframe.csv")
data = df["claps"].tolist()

population_mean=statistics.mean(data)
print("mean of population data=",population_mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(1,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    sample_mean=statistics.mean(dataset)
    return sample_mean

mean_list=[]
for i in range(0,100):
   set_of_means=random_set_of_mean(30)
   mean_list.append(set_of_means)

mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

new_mean_list=[]
for i in range(0,100):
   set_of_means2=random_set_of_mean(30)
   new_mean_list.append(set_of_means2)

new_sample_mean=statistics.mean(new_mean_list)

fig = ff.create_distplot([mean_list], ["no of claps for articles"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.add_trace(go.Scatter(x=[new_sample_mean,new_sample_mean],y=[0,0.17] , mode="lines" , name= " new sample mean"))

fig.show()


z_score=(new_sample_mean-mean)/std_deviation
print("z score:",z_score)


