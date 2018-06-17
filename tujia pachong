import requests
import json
import re

formdata =json.dumps( {"conditions":[{"label":"厦门","specialLabel":"null","type":42,"value":"33","gType":0,"percentageUser":"null","pingYin":"null","hot":"null","labelDesc":"null","isSelected":"false","selected":"false","hotRecommend":"null"},{"label":"","specialLabel":"null","type":47,"value":"2018-06-17,2018-06-18","gType":0,"percentageUser":"null","pingYin":"null","hot":"null","labelDesc":"null","isSelected":"false","selected":"false","hotRecommend":"null"},{"gType":1,"label":"0-200","value":"0,200","type":21}],"pageIndex":1,"pageSize":30,"returnAllConditions":"false","returnRedPacketInfo":"true","callCenter":"false"})

url = "https://www.tujia.com/bingo/pc/search/searchUnit"

headers={ "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Referer":"https://www.tujia.com/unitlist?startDate=2018-06-17&endDate=2018-06-18&cityId=33&ssr=off",
    "Content-Type": "application/json;charset=UTF-8"
    }

response = requests.post(url, data = formdata, headers = headers)

page = re.search(r'"totalUnitCount":.*?,',response.text)
page=int(page.group()[17:-1])//30+1

for everypage in range(page):
    formdata = json.dumps({"conditions": [
        {"label": "厦门", "specialLabel": "null", "type": 42, "value": "33", "gType": 0, "percentageUser": "null",
         "pingYin": "null", "hot": "null", "labelDesc": "null", "isSelected": "false", "selected": "false",
         "hotRecommend": "null"},
        {"label": "", "specialLabel": "null", "type": 47, "value": "2018-06-17,2018-06-18", "gType": 0,
         "percentageUser": "null", "pingYin": "null", "hot": "null", "labelDesc": "null", "isSelected": "false",
         "selected": "false", "hotRecommend": "null"}, {"gType": 1, "label": "0-200", "value": "0,200", "type": 21}],
                           "pageIndex": everypage, "pageSize": 30, "returnAllConditions": "false",
                           "returnRedPacketInfo": "true", "callCenter": "false"})

    response = requests.post(url, data = formdata, headers = headers)
    first = re.finditer(r'{"pictureCount".*?}',response.text)
    for everyone in first :
        name = re.search(r'"unitName":".*?"',everyone.group(0))
        print(name.group()[12:-1],end="")
        money = re.search(r'"finalPrice":.*?,',everyone.group(0))
        print(money.group()[13:-1])
