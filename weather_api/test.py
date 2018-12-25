import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sns.set(style="darkgrid")
date = pd.date_range("2017-03", freq="M", periods=15)
count = np.random.rand(15,4)
df1 = pd.DataFrame({"date":date, "count" : count[:,0]})
df2 = pd.DataFrame({"date":date, "count" : count[:,1]+0.7})
df3 = pd.DataFrame({"date":date, "count" : count[:,2]+2})

f, ax = plt.subplots(1, 1)
x_col='date'
y_col = 'count'

sns.pointplot(ax=ax,x=x_col,y=y_col,data=df1,color='blue')
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df2,color='green')
sns.pointplot(ax=ax,x=x_col,y=y_col,data=df3,color='red')

ax.legend(handles=ax.lines[::len(df1)+1], labels=["A","B","C"])

ax.set_xticklabels([t.get_text().split("T")[0] for t in ax.get_xticklabels()])
plt.gcf().autofmt_xdate()

plt.show()