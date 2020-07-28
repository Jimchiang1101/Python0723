import requests
import json

def getYoubikes() -> list:
    limit = 500
    path = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=%d'
    path = path % limit
    data = requests.get(path).text  # 取得網路原始字串資料
    dict = json.loads(data)  # 將 json 字串轉成 python 可用的物件
    youbikes = dict.get('result').get('records')
    return youbikes


def getYoubikeByName(sna, youbikes=None) -> dict:
    if youbikes is None:
        youbikes = getYoubikes()

    for youbike in youbikes:
        if str(youbike.get('sna')).__contains__(sna):
            return youbike

if __name__ == '__main__':
    youbikes = getYoubikes()
    youbike = getYoubikeByName('桃園火車站(前站)', youbikes)
    print(youbike)