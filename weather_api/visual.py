import seaborn as sns
import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
sns.set(style="darkgrid")

# Load the weather data
with open('data.json','r') as f:
    data=json.load(f)

# '20180101'
first_date=data['date'][0]

# '2018-01-01'
d_format='{}-{}-{}'.format(first_date[0:4],first_date[4:6],first_date[6:8])

date = pd.date_range(d_format, freq="D", periods=5)

df1 = pd.DataFrame({"date":date, "temp" : data['low']})
df2 = pd.DataFrame({"date":date, "temp" : data['high']})

plt.rc('font', family='SimHei', size=13)

f, ax = plt.subplots(1, 1)

sns.pointplot(x='date',y='temp',data=df1,markers="o")
sns.pointplot(x='date',y='temp',data=df2,markers="o",color='#FF6347')

#ax.plot_date(data['date'],data['high'],color='#FF6347',label='最高气温',linestyle="-")
#ax.plot_date(data['date'],data['low'],label='最低气温',linestyle="-")

#ax.legend()

#图例
ax.legend(handles=ax.lines[::len(df2)+1], labels=["最低气温","最高气温"])

plt.legend()
plt.xlabel('日期')
plt.ylabel('温度(℃)')



# 显示数值
x_pos = np.arange(len(df1))
for x_pos, y1_pos,y2_pos in zip(x_pos, df1['temp'],df2['temp']):  # 画柱形图上的数字
    plt.text(x=x_pos, y=y1_pos + 1, s=y1_pos, horizontalalignment='center', weight='bold')
    plt.text(x=x_pos, y=y2_pos + 1, s=y2_pos, horizontalalignment='center', weight='bold')


ax.set_xticklabels([t.get_text().split("T")[0] for t in ax.get_xticklabels()])

#调整刻度值的倾斜度
#plt.gcf().autofmt_xdate()

plt.show()