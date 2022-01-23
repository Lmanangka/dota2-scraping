'''
Created : 21/06/2021
Revision: 23/01/2022
Author  : Leo Manangka
'''
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

class Winrate:
    '''winrate class'''

    def __init__(self):
        self.winning_month='https://www.dotabuff.com/heroes/winning'
        self.winning_week='https://www.dotabuff.com/heroes/winning/?date=week'
        self.header={'User-Agent':'BOT'}
        self.resp_month=requests.get(self.winning_month,headers=self.header)
        self.resp_week=requests.get(self.winning_week,headers=self.header)
        self.soup_monthly=BeautifulSoup(self.resp_month.text,'html.parser')
        self.soup_weekly=BeautifulSoup(self.resp_week.text,'html.parser')

    def month(self):
        """monthly winrate"""

        if self.resp_month.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured:',self.resp_month)
        title_monthly=self.soup_monthly.find_all('header')[0].text
        table_monthly=self.soup_monthly.find('table')
        month_table=pd.read_html(str(table_monthly))[0].drop('Hero',1)
        print(title_monthly.center(50))
        print(month_table.head(10),'\n')

    def week(self):
        """weekly winrate"""

        if self.resp_week.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured:',self.resp_week)
        title_weekly=self.soup_weekly.find_all('header')[0].text
        table2=self.soup_weekly.find('table')
        week_table=pd.read_html(str(table2))[0].drop('Hero',1)
        print(title_weekly.center(50))
        print(week_table.head(10),'\n')

class Heroes:
    '''heroes class'''

    def __init__(self):
        hero_name=input("Search Dota 2 Heroes: ")
        for i in range(0, len(hero_name), 1):
            if hero_name[i] == ' ':
                hero_name=hero_name.replace(hero_name[i], '-')
        self.heroes_stat='https://www.dotabuff.com/heroes/%s' % hero_name
        self.header={'User-Agent':'BOT'}
        self.resp_stat=requests.get(self.heroes_stat,headers=self.header)
        self.soup_status=BeautifulSoup(self.resp_stat.text,'html.parser')

    def stat(self):
        '''heroes stat'''

        if self.resp_stat.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured', self.resp_stat)
        table=self.soup_status.find_all('table')
        laning_presence=pd.read_html(str(table))[1]
        most_item_used=pd.read_html(str(table))[2]
        best_versus=pd.read_html(str(table))[3]
        worst_versus=pd.read_html(str(table))[4]
        print("Lane Presence".center(50))
        print(laning_presence,'\n')
        print("Most Used Items This Week".center(50))
        print(most_item_used.drop('Item',1),'\n')
        print("Best Versus This Week".center(50))
        print(best_versus.drop('Hero',1),'\n')
        print("Worst Versus This Week".center(50))
        print(worst_versus.drop('Hero',1), '\n')


class GameImpact:
    '''most game impact class'''

    def __init__(self):
        self.impact_month='https://www.dotabuff.com/heroes/impact'
        self.impact_week='https://www.dotabuff.com/heroes/impact?date=week'
        self.header={'User-Agent':'BOT'}
        self.resp_impact_month=requests.get(self.impact_month,headers=
                self.header)
        self.resp_impact_week=requests.get(self.impact_week,headers=
                self.header)
        self.soup_impact_monthly=BeautifulSoup(self.resp_impact_month.text,
                'html.parser')
        self.soup_impact_weekly=BeautifulSoup(self.resp_impact_week.text,
                'html.parser')

    def game_impact_month(self):
        '''game impact this month'''
        if self.resp_impact_month.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured', self.resp_impact_month)
        title_monthly=self.soup_impact_monthly.find_all('header')[0].text
        table_monthly=self.soup_impact_monthly.find('table')
        month_table=pd.read_html(str(table_monthly))[0].drop('Hero',1)
        print(title_monthly.center(50))
        print(month_table.head(10),'\n')

    def game_impact_week(self):
        '''game impact this week'''
        if self.resp_impact_month.status_code==200:
            print('Success!\n')
        else:
            print('An error has occured', self.resp_impact_month)
        title_weekly=self.soup_impact_weekly.find_all('header')[0].text
        table_weekly=self.soup_impact_weekly.find('table')
        month_table=pd.read_html(str(table_weekly))[0].drop('Hero',1)
        print(title_weekly.center(50))
        print(month_table.head(10),'\n')

def help_text():
    '''display help text'''
    print('''Usage: dota_stat.py [OPTION]\n
-wm\t\tHighest Win Rate This Month
-ww\t\tHighest Win Rate This Week
-H | --hero\tChoose Heroes And Display Laning Presence, Most Item Used, Versus And Worst Versus
-iw\t\tMost Game Impact This Week
-im\t\tMost Game Impact This Month
-h | --help\tShow This Text\n''')

if __name__=='__main__':
    winrate=Winrate()
    try:

        if len(sys.argv)<2:
            help_text()
            sys.exit()

        arg=sys.argv[1]

        if arg == "-wm":
            winrate.month()
        elif arg == "-ww":
            winrate.week()
        elif arg in {"-H","--hero"}:
            heroes=Heroes()
            heroes.stat()
        elif arg == "-iw":
            gameimpact=GameImpact()
            gameimpact.game_impact_week()
        elif arg == "-im":
            gameimpact=GameImpact()
            gameimpact.game_impact_month()
        elif arg in {"-h","--help"}:
            help_text()
        else:
            help_text()

    except KeyboardInterrupt:
        print("exit")
    finally:
        print("Done")
