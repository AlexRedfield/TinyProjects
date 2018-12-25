import urllib.parse
import urllib.request
import json

city = u'沙坪坝'  # 待查询城市
city = urllib.parse.quote(city)  # 这一句很关键....坑太大
weather_url = 'http://www.sojson.com/open/api/weather/json.shtml?city=%s' % city

# 抓取网页信息
req = urllib.request.urlopen(weather_url)
rs = req.read().decode()  # 采用utf-8解码


# 获取当天数据，格式如下
# {"date":"04日星期四","sunrise":"07:50","high":"高温 7.0℃","low":"低温 5.0℃",
# "sunset":"18:08","aqi":24.0,"fx":"无持续风向","fl":"<3级","type":"小雨",
# "notice":"下雨了不要紧，撑伞挡挡就行"}
#print(rs)
weather_info = json.loads(rs)['data']

#print(weather_info)

year_month = json.loads(rs)['date'][-8:-2]
print(weather_info['forecast'])

date, low, high = [], [], []
for i in weather_info['forecast']:
    date.append(year_month+i['date'][:2])
    low.append(float(i['low'][3:][:-1]))
    high.append(float(i['high'][3:][:-1]))

#data=zip(date,low,high)
data={'date':date, 'low':low, 'high': high}

with open('data.json', 'w') as f:
    json.dump(data, f)
#print(weather_info['forecast'])
