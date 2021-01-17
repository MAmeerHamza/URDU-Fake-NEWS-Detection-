from bs4 import BeautifulSoup
import requests
import pandas as pd


news_list = {}
count = 0
url = "https://www.pakistantoday.com.pk/national"
for x in range(2,10):
    response = requests.get(url).text
    soup  =BeautifulSoup(response, 'lxml')
    news = soup.find_all('article',{'class':'post'})
   
    for data in news:
        title = data.h2.text
        text = data.p.text
        image = data.find('div',{'class':'entry-thumbnail'}).a.img.get("src")
        link = data.h2.a.get("href")
        source = "PakistanToday"
        news_list[count] = [title,text,image,link,source]
        count+=1
    x = str(x)
    url = "https://www.pakistantoday.com.pk/national/page/"+x
 
    df = pd.DataFrame.from_dict(news_list,orient='index', columns=['title','text','image','link','source'])
    df.to_csv('pandas.csv', mode='a',header=False,index=False)


