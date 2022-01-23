# Web Scraping

Collecting data from [Dotabuff](https://www.dotabuff.com)
such as Highest Winrate (monthly and weekly)
Hero stat like lane presence, items mostly used, worst versus and best versus

## Need to Install
* pandas
```shell
pip install pandas
```
* request
```shell
pip install request
```
* BeautifulSoup
```shell
pip install beautifulsoup4
```
## How to Use
Usage: dota_stat.py [OPTION]
-wm             Highest Win Rate This Month
-ww             Highest Win Rate This Week
-H | --hero     Choose Heroes And Display Laning Presence, Most Item Used,
                Versus And Worst Versus
-iw             Most Game Impact This Week
-im             Most Game Impact This Month\n
-h | --help     Show This Text
