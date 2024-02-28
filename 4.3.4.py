from bs4 import BeautifulSoup as bs
import requests
import matplotlib.pyplot as plt
from tqdm import tqdm
def assessment_of_dynamics(yn,y1,n):
    dy=(yn-y1)/(n-1)
    Tp=(yn/y1)**(1/(n-1))
    return dy,Tp
def pars(url,s1=70,e1=76,s2=70,e2=80):
    pric=[]
    date=[]
    r=requests.get(url)
    html=bs(r.content,'html.parser')
    table=html.find(class_="result_table").select('td')
    for el in table:
        for i in el:
            if 'USD' in i:
                pric.append(float(i[s1:e1].replace(' ','')))
            else:
                date.append(i[s1:e2])
    pric.reverse()
    date.reverse()
    return pric,date

dates1=[]
price1=[]
price2=[]
dates2=[]
price3=[]
dates3=[]
for mounth in tqdm(range(1,13)):
    # date=[]
    # pric=[]
    if mounth<10:mounth_=f'0{mounth}'
    else:mounth_=mounth
    # r1=requests.get(f'https://ru.allstockstoday.com/AAPL-istoriya-kotirovok-aktsiy-za-2021-{mounth_}.html')
    # r2=requests.get(f'https://ru.allstockstoday.com/MSFT-istoriya-kotirovok-aktsiy-za-2021-{mounth_}.html')
    # html1=bs(r1.content,'html.parser')
    # html2=bs(r2.content,'html.parser')
    # table1=html1.find(class_="result_table").select('td')
    # table2=html2.find(class_="result_table").select('td')
    # for el in table1:
    #     for i in el:
    #         if 'USD' in i:
    #             pric.append(float(i[70:76]))
    #         else:
    #             date.append(i[70:80])
    # date.reverse()
    # pric.reverse()
    plt.xticks(rotation=90)
    plt.rc('xtick',labelsize=1)
    pric,date=pars(f'https://ru.allstockstoday.com/AAPL-istoriya-kotirovok-aktsiy-za-2021-{mounth_}.html')
    dates1+=date
    price1+=pric
    pric,date=pars(f'https://ru.allstockstoday.com/MSFT-istoriya-kotirovok-aktsiy-za-2021-{mounth_}.html')
    dates2+=date
    price2+=pric
    pric, date = pars(f'https://ru.allstockstoday.com/GOOGL-istoriya-kotirovok-aktsiy-za-2021-{mounth_}.html',s1=70,e1=79)
    dates3 += date
    price3 += pric
dy,Tp=assessment_of_dynamics(price1[-1],price1[0],12)
print(f'Средний темп прироста акций Apple - {Tp}%')
print(f'Средний абсолютный прирост акций Apple - {dy}')
dy,Tp=assessment_of_dynamics(price2[-1],price2[0],12)
print(f'Средний темп прироста акций Microsoft - {Tp}%')
print(f'Средний абсолютный прирост акций Microsoft - {dy}')
dy,Tp=assessment_of_dynamics(price3[-1],price3[0],12)
print(f'Средний темп прироста акций Google - {Tp}%')
print(f'Средний абсолютный прирост акций Google - {dy}')
plt.plot(dates1,price1)
plt.plot(dates2,price2)
plt.plot(dates3,price3)
plt.show()