import pandas as pd
from pandas._config import display
import requests
from lxml import etree
from data_clean_utils import clean_stat, split_by_of, trim_newline_stat, page_data_refining

def get_stat_by_xpath(html,xpath):
    returning_val = []
    element = html.xpath(xpath)[0]

    if element.tag == 'i':
        text_value = element.xpath('./i[@class="b-fight-details__label"]/following-sibling::text()[1]')

        if len(text_value) >= 1:
            returning_val = text_value[0].strip()
    else:
        returning_val = trim_newline_stat(element.text)

    return clean_stat(returning_val)

def get_details_of_fight(html): 
    referee = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[5]/span')
    rounds = int(get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[2]'))
    time = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[3]')
    time_format = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[4]')
    r_win = trim_newline_stat(html.xpath('/html/body/section/div/div/div[1]/div[1]/i')[0].text)
    b_win = trim_newline_stat(html.xpath('/html/body/section/div/div/div[1]/div[2]/i')[0].text)

    r_fighter = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[1]/p[1]/a')
    r_kd = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[1]')
    r_sig_str = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[1]') # sig. str of sig. str
    r_total_str = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]') # suc td o
    r_td = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]') # suc td o
    r_sub_att = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]') 
    r_rev = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[1]')
    r_ctrl = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[1]')

    b_fighter = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[1]/p[2]/a')
    b_kd = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[2]')
    b_sig_str = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[2]') # sig. str of s
    b_total_str = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]') # suc td of total td
    b_td = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]') # suc td o
    b_sub_att = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]') # sub att
    b_rev = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[2]') # rev
    b_ctrl = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[10]/p[2]') # ctrl

    r_head = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[4]/p[1]')
    r_body = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[5]/p[1]')
    r_leg = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[6]/p[1]')
    r_distance = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[7]/p[1]')
    r_clinch = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[8]/p[1]')
    r_ground = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[9]/p[1]')

    b_head = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[4]/p[2]')
    b_body = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[5]/p[2]')
    b_leg = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[6]/p[2]')
    b_distance = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[7]/p[2]')
    b_clinch = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[8]/p[2]')
    b_ground = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[9]/p[2]')

    return [
        referee,
        rounds,
        time,
        time_format,
        r_win,
        b_win,
        r_fighter,
        r_kd,
        r_sig_str,
        r_total_str,
        r_td,
        r_sub_att,
        r_rev,
        r_ctrl,
        r_head,
        r_body,
        r_leg,
        r_distance,
        r_clinch,
        r_ground,
        b_fighter,
        b_kd,
        b_sig_str,
        b_total_str,
        b_td,
        b_sub_att,
        b_rev,
        b_ctrl,
        b_head,
        b_body,
        b_leg,
        b_distance,
        b_clinch,
        b_ground,
    ]

def fight_detail():
    fight_detail_df = pd.DataFrame({ 
        "date": [],
        "referee": [],
        "rounds": [],
        "time": [],
        "time_format": [],
        "r_win": [],
        "b_win": [],
        "r_fighter": [],
        "r_kd": [],
        "r_sig_str": [],
        "r_total_str": [],
        "r_td": [],
        "r_sub_att": [],
        "r_rev": [],
        "r_ctrl": [],
        "r_head": [],
        "r_body": [],
        "r_leg": [],
        "r_distance": [],
        "r_clinch": [],
        "r_ground": [],
        "b_fighter": [],
        "b_kd": [],
        "b_sig_str": [],
        "b_total_str": [],
        "b_td": [],
        "b_sub_att": [],
        "b_rev": [],
        "b_ctrl": [],
        "b_head": [],
        "b_body": [],
        "b_leg": [],
        "b_distance": [],
        "b_clinch": [],
        "b_ground": [],
    })

    try:
        with open('../files/fight_links.txt', 'r') as fight_file:
            date = ""
            for fight_index, fight_detail_url in enumerate(fight_file):
                print(f"{fight_index}\n")
                if fight_detail_url[:4] != "http": # not a website hence a date
                    date = fight_detail_url
                    print(f"Date changed to {date}")
                else:
                    print(fight_detail_url)
                    fight_detail_page = requests.get(fight_detail_url[:-1]).content

                    html_page = etree.HTML(fight_detail_page)
                    fight_details = get_details_of_fight(html_page)
                    fight_details.insert(0, date[:-1])
                    print(fight_details)
                    fight_detail_df.loc[len(fight_detail_df)] = fight_details
    finally:
        fight_detail_df.to_csv('../dataset/raw_fight_details.csv', sep=',', index=False)
            
if __name__ == "__main__":
    fight_detail()
