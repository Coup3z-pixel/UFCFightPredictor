import requests
import string
import pandas as pd
from lxml import etree


def scrape_fighter():
    fighter_details_df = pd.DataFrame(columns=['name','weight', 'reach', 'stance'])

    try:
        for character in string.ascii_lowercase:
            event_page = requests.get(f'http://ufcstats.com/statistics/fighters?char={character}&page=all').content
            html_page = etree.HTML(event_page)

            tr = html_page.xpath('//tr')
            for row in tr:
                fighter_details_df.loc[len(fighter_details_df)] = [
                        row.xpath('td[1]/a')
                ]
                print(row.xpath('td[1]/a'))


    finally:
        fighter_details_df.to_csv('../dataset/fighter_details.csv')

    

scrape_fighter()
