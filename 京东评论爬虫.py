import requests
import json
import time

ID=input("id")
ID=int(ID)
page=input("page")
f = open('./%d.txt'%(ID), 'a')
for temp in range(int(page)):
    time.sleep(5)
    r = requests.get("https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv206&productId=%d&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&rid=0&fold=1"%(ID,temp))
    s=json.loads(r.text[25: -2])
    for i in range(10):
        f.write(s["comments"][i]["content"]+'\n')

f.close()
