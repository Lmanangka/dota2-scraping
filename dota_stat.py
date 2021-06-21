'''system module'''
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

class Winrate:
    '''winrate class'''

    def __init__(self):
        self.url1='https://www.dotabuff.com/heroes/winning'
        self.url2='https://www.dotabuff.com/heroes/winning/?date=week'
        self.header={'User-Agent':'BOT'}
        self.resp1=requests.get(self.url1,headers=self.header)
        self.resp2=requests.get(self.url2,headers=self.header)
        self.soup_monthly=BeautifulSoup(self.resp1.text,'html.parser')
        self.soup_weekly=BeautifulSoup(self.resp2.text,'html.parser')

    def month(self):
        """monthly winrate"""

        if self.resp1.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured:',self.resp1)
        title_monthly=self.soup_monthly.find_all('header')[0].text
        table1=self.soup_monthly.find('table')
        month_table=pd.read_html(str(table1))[0].drop('Hero',1)
        print(title_monthly)
        print(month_table.head(10),'\n')

    def week(self):
        """weekly winrate"""

        if self.resp2.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured:',self.resp2)
        title_weekly=self.soup_weekly.find_all('header')[0].text
        table2=self.soup_weekly.find('table')
        week_table=pd.read_html(str(table2))[0].drop('Hero',1)
        print(title_weekly)
        print(week_table.head(10),'\n')

class Heroes:
    '''heroes class'''

    def __init__(self):
        hero_name=input("Search Dota 2 Heroes: ")
        for i in range(0, len(hero_name), 1):
            if hero_name[i] == ' ':
                hero_name=hero_name.replace(hero_name[i], '-')
        self.url='https://www.dotabuff.com/heroes/%s' % hero_name
        self.header={'User-Agent':'BOT'}
        self.resp=requests.get(self.url,headers=self.header)
        self.soup=BeautifulSoup(self.resp.text,'html.parser')

    def stat(self):
        '''heroes stat'''

        if self.resp.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured', self.resp)
        table=self.soup.find_all('table')
        title1=self.soup.find_all('header')[0].text
        title2=self.soup.find_all('header')[3].text
        title3=self.soup.find_all('header')[4].text
        title4=self.soup.find_all('header')[5].text
        laning_presence=pd.read_html(str(table))[1]
        most_item_used=pd.read_html(str(table))[2]
        best_versus=pd.read_html(str(table))[3]
        worst_versus=pd.read_html(str(table))[4]
        print(title1)
        print(laning_presence,'\n')
        print(title2)
        print(most_item_used.drop('Item',1),'\n')
        print(title3)
        print(best_versus.drop('Hero',1),'\n')
        print(title4)
        print(worst_versus.drop('Hero',1), '\n')

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
