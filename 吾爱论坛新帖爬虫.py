import requests
import re
from bs4 import BeautifulSoup
date=[]
number=0
note=""
for num in [1,2,3,4,5]:
    print('第'+str(num)+'页')
    r = requests.get("https://www.52pojie.cn/forum.php?mod=guide&view=newthread&page="+str(num), timeout=30)
    fi = re.finditer(r' <a href="t(.|\n)*?</a>',r.text)
    for i in fi:
        soup=BeautifulSoup(i.group(0),"html.parser")
        print(str(number)+"    "+soup.a.string)
        date.append(soup.find('a').get('href'))
        number+=1
page=input("看哪个？")
if page.isdigit():
    page=int(page)
two = requests.get("https://www.52pojie.cn/"+date[page], timeout=30)

if two.text:
    so=BeautifulSoup(two.text,"html.parser")
    for k in so.find_all(name='div',attrs={"class":"pcb"}):
        note += str(k)
    thrfi = re.finditer(r'>((.|\n)*?)<',note)
    for iss in thrfi:    
       print(iss.group(1))
