import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

class Winrate(object):
    def __init__(self):
        self.url1='https://www.dotabuff.com/heroes/winning'
        self.url2='https://www.dotabuff.com/heroes/winning/?date=week'
        self.header={'User-Agent':'BOT'}
        self.resp1=requests.get(self.url1,headers=self.header)
        self.resp2=requests.get(self.url2,headers=self.header)

    def month(self):
        if self.resp1.status_code==200: 
            print('Success!\n')
        else:
            print('An error has occured:',self.resp1)
        self.soup=BeautifulSoup(self.resp1.text,'html.parser')
        self.table=self.soup.find('table')
        self.df=pd.read_html(str(self.table))[0]
        print(self.df.drop('Hero',1).head(10),'\n')

    def week(self):
        if self.resp2.status_code==200: 
            print('Success!\n')
        else:
            print('An error has occured:',self.resp2)
        self.soup=BeautifulSoup(self.resp2.text,'html.parser')
        self.table=self.soup.find('table')
        self.df=pd.read_html(str(self.table))[0]
        print(self.df.drop('Hero',1).head(10),'\n')

class Heroes(object):
    def __init__(self):
        self.hero=input("Search Dota 2 Heroes: ")
        for i in range(0, len(self.hero), 1):
            if (self.hero[i] == ' '):
                self.hero = self.hero.replace(self.hero[i], '-')
        self.url='https://www.dotabuff.com/heroes/%s' % self.hero
        self.header={'User-Agent':'BOT'}
        self.resp=requests.get(self.url,headers=self.header)

    def stat(self):
        if self.resp.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured', self.resp)
        self.soup=BeautifulSoup(self.resp.text,'html.parser')
        self.table=self.soup.find_all('table')
        self.title1=self.soup.find_all('header')[0].text
        print(self.title1)
        self.df1=pd.read_html(str(self.table))[1]
        print(self.df1,'\n')
        self.title2=self.soup.find_all('header')[3].text
        print(self.title2)
        self.df2=pd.read_html(str(self.table))[2]
        print(self.df2.drop('Item',1),'\n')
        self.title3=self.soup.find_all('header')[4].text
        print(self.title3)
        self.df3=pd.read_html(str(self.table))[3]
        print(self.df3.drop('Hero',1),'\n')
        self.title4=self.soup.find_all('header')[5].text
        print(self.title4)
        self.df4=pd.read_html(str(self.table))[4]
        print(self.df4.drop('Hero',1), '\n')      

if __name__=='__main__':
    winrate=Winrate()
    try:
        arg=sys.argv[1]

        if arg == "month":
            winrate.month()
        elif arg == "week":
            winrate.week()
        elif arg == "hero":
            heroes=Heroes()
            heroes.stat()
        else:
            print("Usage: winrate.py [OPTION]\nmonth or week or hero\n")
    except KeyboardInterrupt:
        print("exit")
    finally:
        print("Done")
    