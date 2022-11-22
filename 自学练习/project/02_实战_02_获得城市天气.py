import requests

while 1:
    city = input('你所在的城市是：')
    url = 'https://v0.yiketianqi.com/api?unescape=1&version=v91&appid=43656176&appsecret=I42og6Lm&ext=&cityid=&city='+city
    r = requests.get(url)
    data = r.json()
    # l = data['location']['name']
    # l = list(data)
    # l = data[0]['name']
    # print(data['data'])
    count = 0
    for i in data['data']:
        # print(i)
        # print(i['date'],':',i['week'],':',i['wea'])
        if '雷阵雨' in i['wea']:
            print(i['date'],'有雷阵雨，不要出门了。')
            count += 1
        if '雨' in i['wea']:
            print('%s,要下雨'%i['date'])
            count += 1
    # print('count的值是：',count)
    if count == 0:
        print('最近七天没有雨！')
       
        