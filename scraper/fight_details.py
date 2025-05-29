import pandas as pd
import requests
from lxml import etree

def get_stat_by_xpath(html,xpath):
    element = html.xpath(xpath)[0]

    if len(split_by_of(element.text)) == 2: # no. of no. format
        return split_by_of(element.text)

    if element.tag == 'i':
        text_value = element.xpath('./i[@class="b-fight-details__label"]/following-sibling::text()[1]')

        if len(text_value) >= 1:
            return text_value[0].strip()

    return trim_newline_stat(element.text)

def split_by_of(stat):
    return stat[1:-1].strip().split(" of ")

def trim_newline_stat(stat):
    return stat.strip("\n ")

def get_details_of_fight(html): 
    referee = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[5]/span')
    rounds = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[2]')
    time = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[3]')
    time_format = get_stat_by_xpath(html,'/html/body/section/div/div/div[2]/div[2]/p[1]/i[4]')

    r_sig_str = split_by_of(html.xpath('/html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[1]')[0].text), # sig. str of sig. str
    r_suc_td_of_total = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]') # suc td o
    r_sub_att = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]') 
    r_rev = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[1]')
    r_ctrl = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]')

    b_sig_str = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[2]'), # sig. str of s
    b_suc_td_of_total = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]') # suc td of total td
    b_sub_att = get_stat_by_xpath(html, '/html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]') # sub att
    b_rev = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[2]') # rev
    b_ctrl = get_stat_by_xpath(html,'/html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]') # ctrl

    r_head = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[4]/p[1]')
    r_body = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[5]/p[1]')
    r_leg = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[6]/p[1]')

    r_distance = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[7]/p[1]')
    r_clinch = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[8]/p[1]')
    r_ground = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[9]/p[1]')

    b_head = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[4]/p[1]')
    b_body = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[5]/p[1]')
    b_leg = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[6]/p[1]')

    b_distance = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[7]/p[1]')
    b_clinch = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[8]/p[1]')
    b_ground = get_stat_by_xpath(html,'/html/body/section/div/div/table/tbody/tr/td[9]/p[1]')

    return [
        referee,
        rounds,
        time,
        time_format,
        r_sig_str,
        r_suc_td_of_total,
        r_sub_att,
        r_rev,
        r_ctrl,
        b_sig_str,
        b_suc_td_of_total,
        b_sub_att,
        b_rev,
        b_ctrl,
        r_head,
        r_body,
        r_leg,
        r_distance,
        r_clinch,
        r_ground,
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
        "time_format": [],
        "referee": [],
        "r_fighter": [],
        "r_kd": [],
        "r_Sig. str": [],
        "r_Sig. str. %": [],
        "r_Total str. ": [],
        "r_Td ": [],
        "r_Td ": [],
        "r_Sub. att": [],
        "r_Rev.": [],
        "r_Ctrl": [],
        "b_Sig. str.": [],
        "b_Sig. str. ": [],
        "b_Total str. ": [],
        "b_Td ": [],
        "b_Td ": [],
        "b_Sub. att": [],
        "b_Rev.": [],
        "b_Ctrl": [],
        "r_Head": [],
        "r_Body": [],
        "r_Leg": [],
        "r_Distance": [],
        "r_Clinch": [],
        "r_Ground": [],
        "b_Head": [],
        "b_Body": [],
        "b_Leg": [],
        "b_Distance": [],
        "b_Clinch": [],
        "b_Ground": []
    })

    with open('../files/fight_links.txt', 'r') as fight_file:
        for fight_detail_url in fight_file:
            date = ""

            if fight_detail_url[:5] != "https": # not a website hence a date
                date = fight_detail_url

            fight_detail_page = requests.get(fight_detail_url[:-1]).content

            html_page = etree.HTML(fight_detail_page)
            fight_details = get_details_of_fight(html_page).insert(0, date)
            print(fight_details)
            fight_detail_df[len(fight_detail_df)] = fight_details
            
if __name__ == "__main__":
    fight_detail()
