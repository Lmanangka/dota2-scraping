#!/usr/bin/python3
'''
Created : 21/06/2021
Revision: 28/03/2022
Author  : Leo Manangka
'''
import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

class color:
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    END = '\033[0m'

def stat_code(url):
    '''check status code'''

    if url.status_code==200:
        print(color.GREEN + 'Success!\n' + color.END)
    else:
        print(color.RED + 'An error has occured:' + color.END,url)

def help_text():
    '''display help text'''

    print(color.CYAN + '''Usage: dota_stat.py [OPTION]\n
-wm\t\tHighest Win Rate This Month
-ww\t\tHighest Win Rate This Week
-H | --hero\tChoose Heroes And Display Laning Presence, Most Item Used, Versus And Worst Versus
-iw\t\tMost Game Impact This Week
-im\t\tMost Game Impact This Month
-h | --help\tShow This Text\n''' + color.END)

class Winrate:
    '''winrate class scraping dotabuff winning rate weekly and monthly'''

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

        stat_code(self.resp_month)
        title_monthly=color.BOLD + self.soup_monthly.find_all('header')[0].text + color.END
        table_monthly=self.soup_monthly.find('table')
        month_table=pd.read_html(str(table_monthly))[0].drop('Hero',axis=1)
        print(title_monthly.center(50))
        print(month_table.head(10),'\n')

    def week(self):
        """weekly winrate"""

        stat_code(self.resp_week)
        title_weekly=color.BOLD + self.soup_weekly.find_all('header')[0].text + color.END
        table2=self.soup_weekly.find('table')
        week_table=pd.read_html(str(table2))[0].drop('Hero',axis=1)
        print(title_weekly.center(50))
        print(week_table.head(10),'\n')

class Heroes:
    '''heroes class scraping dotabuff for every hero'''

    def __init__(self):
        hero_name=input(color.BOLD + "Search Dota 2 Heroes: " + color.END)
        for i in range(0, len(hero_name), 1):
            if hero_name[i] == ' ':
                hero_name=hero_name.replace(hero_name[i], '-')
        self.heroes_stat='https://www.dotabuff.com/heroes/%s' % hero_name
        self.header={'User-Agent':'BOT'}
        self.resp_stat=requests.get(self.heroes_stat,headers=self.header)
        self.soup_status=BeautifulSoup(self.resp_stat.text,'html.parser')

    def stat(self):
        '''heroes stat'''

        stat_code(self.resp_stat)
        table=self.soup_status.find_all('table')
        laning_presence=pd.read_html(str(table))[1]
        most_item_used=pd.read_html(str(table))[2]
        best_versus=pd.read_html(str(table))[3]
        worst_versus=pd.read_html(str(table))[4]
        print(color.BOLD + "Lane Presence".center(50) + color.END)
        print(laning_presence,'\n')
        print(color.BOLD + "Most Used Items This Week".center(50) + color.END)
        print(most_item_used.drop('Item',axis=1),'\n')
        print(color.BOLD + "Best Versus This Week".center(50) + color.END)
        print(best_versus.drop('Hero',axis=1),'\n')
        print(color.BOLD + "Worst Versus This Week".center(50) + color.END)
        print(worst_versus.drop('Hero',axis=1), '\n')

class GameImpact:
    '''most game impact class scraping dotabuff for most game impact
    weekly and monthly'''

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

        stat_code(self.resp_impact_month)
        title_monthly=color.BOLD + self.soup_impact_monthly.find_all('header')[0].text + color.END
        table_monthly=self.soup_impact_monthly.find('table')
        month_table=pd.read_html(str(table_monthly))[0].drop('Hero',axis=1)
        print(title_monthly.center(50))
        print(month_table.head(10),'\n')

    def game_impact_week(self):
        '''game impact this week'''

        stat_code(self.resp_impact_week)
        title_weekly=color.BOLD + self.soup_impact_weekly.find_all('header')[0].text + color.END
        table_weekly=self.soup_impact_weekly.find('table')
        month_table=pd.read_html(str(table_weekly))[0].drop('Hero',axis=1)
        print(title_weekly.center(50))
        print(month_table.head(10),'\n')

if __name__=='__main__':
    winrate=Winrate()
    try:
        # make empty argument rum default program
        if len(sys.argv)<2:
            help_text()
            sys.exit()

        # make option in program
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
        print(color.RED + "exit" + color.END)
    finally:
        print(color.GREEN + "Done" + color.END)
