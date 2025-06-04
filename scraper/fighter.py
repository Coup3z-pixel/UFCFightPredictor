import requests
import string
import pandas as pd
from lxml import etree


def scrape_fighter():
    fighter_details_df = pd.DataFrame(columns=['name','height','weight', 'reach', 'stance'])

    try:
        for character in string.ascii_lowercase:
            event_page = requests.get(f'http://ufcstats.com/statistics/fighters?char={character}&page=all').content
            html_page = etree.HTML(event_page)

            tr = html_page.xpath('//tr')
            for row in tr:
                if not row.xpath('td[1]/a'):
                    continue

                height = row.xpath('td[4]')[0].text.strip('\n ')

                fighter_details_df.loc[len(fighter_details_df)] = [
                        f"{row.xpath('td[1]/a')[0].text} {row.xpath('td[2]/a')[0].text}",
                        -1 if height == '--' else int(height[0]) * 12 + int(height[height.index(' '):height.index('"')]),
                        row.xpath('td[5]')[0].text.strip('\n lbs')[:3],
                        row.xpath('td[6]')[0].text.strip('\n ')[:2],
                        row.xpath('td[7]')[0].text.strip('\n ')
                       ]
    finally:
        fighter_details_df.to_csv('../dataset/fighter_details.csv')

    

scrape_fighter()
