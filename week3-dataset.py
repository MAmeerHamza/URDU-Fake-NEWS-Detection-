from bs4 import BeautifulSoup
import requests
import pandas as pd


news_list = {}
count = 0
url = 'https://urdu.geo.tv/latest/242216-'
for x in range(2,10):
    response = requests.get(url).text
    soup  =BeautifulSoup(response, 'lxml')
    news = soup.find_all('article',{'class':'post'})
   
    for data in news:
        print('data fetche', i)
        soup = BeautifulSoup(page.content , 'html.parser')
        image = data.find('div',{'class':'entry-thumbnail'}).a.img.get("src")
        link = data.h2.a.get("href")
        date = author[1].text.replace('\n'," ")
        article = soup.find(attrs ={'class': 'content-area'}).text.replace('\n'," ")
        news_list[count] = [url,author,publish,article]
        count+=1
    x = str(x)
    url = 'https://urdu.geo.tv/latest/242216-'/page/"+x
 
    df = pd.DataFrame.from_dict(news_list,orient='index', columns=['URL','author','article'])
    df.to_csv('pandas.csv', mode='a',header=False,index=False)


