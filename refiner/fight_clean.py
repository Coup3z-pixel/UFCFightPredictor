import pandas as pd
import numpy as np

from utils_clean import calc_total_time, split_by_of

def clean_data():
    fight_details = pd.read_csv('../dataset/raw_fight_details.csv')

    cleaned_fight_details = pd.DataFrame(
            index=np.arange(0,len(fight_details)), 
            columns=["date","referee","rounds","total_time","time_format","r_win","r_fighter","b_fighter","r_kd","r_sig_str","r_str_hit","r_sig_str_%","r_str_land","r_str_atmpt","r_str_land_%","r_td_atmp","r_td_succ","r_td-%","r_sub_att","r_rev","r_ctrl","r_head_hit","r_head_land","r_head_accuracy","r_body_hit","r_body_atmpt","r_body_accuracy","r_leg_hit","r_leg_land","r_leg_accuracy","r_distance_hit","r_distance_land","r_distance_accuracy","r_clinch_hit","r_clinch_land","r_clinch_accuracy","r_ground_hit","r_ground_land","r_ground_accuracy","b_sig_str","b_str_hit","b_sig_str_%","b_str_land","b_str_atmpt","b_str_land_%","b_td_atmp","b_td_succ","b_td-%","b_sub_att","b_rev","b_ctrl","b_head_hit","b_head_land","b_head_accuracy","b_body_hit","b_body_atmpt","b_body_accuracy","b_leg_hit","b_leg_land","b_leg_accuracy","b_distance_hit","b_distance_land","b_distance_accuracy","b_clinch_hit","b_clinch_land","b_clinch_accuracy","b_ground_hit","b_ground_land","b_ground_accuracy"]
        )
  
    for index, row in enumerate(fight_details.itertuples(index=False)): 
        print(row)
        r_sig_str_of_hit = split_by_of(row[9])
        r_str_of_total = split_by_of(row[10])
        r_succ_of_td = split_by_of(row[11])
        r_sig_str_of_head = split_by_of(row[15])
        r_sig_str_of_body = split_by_of(row[16])
        r_sig_str_of_leg = split_by_of(row[17])
        r_sig_str_of_distance = split_by_of(row[18])
        r_sig_str_of_clinch = split_by_of(row[19])
        r_sig_str_of_ground = split_by_of(row[20])
        b_sig_str_of_hit = split_by_of(row[23])
        b_str_of_total = split_by_of(row[24])
        b_succ_of_td = split_by_of(row[25])
        b_sig_str_of_head = split_by_of(row[29])
        b_sig_str_of_body = split_by_of(row[30])
        b_sig_str_of_leg = split_by_of(row[31])
        b_sig_str_of_distance = split_by_of(row[32])
        b_sig_str_of_clinch = split_by_of(row[33])
        b_sig_str_of_ground = split_by_of(row[34])
        
        cleaned_fight_details.loc[index] = np.array([
                row[0],
                row[1],
                row[2],
                calc_total_time(row[2], row[4], row[3]),
                row[4][row[4].index('(')+1:-1],
                row[5],
                row[7],
                row[21],
                row[8],
                int(r_sig_str_of_hit[0]),
                int(r_sig_str_of_hit[1]),
                0 if int(r_sig_str_of_hit[1]) == 0 else int(r_sig_str_of_hit[0]) / int(r_sig_str_of_hit[1]),
                r_str_of_total[0],
                r_str_of_total[1],
                0 if int(r_str_of_total[1]) == 0 else int(r_str_of_total[0]) / int(r_str_of_total[1]),
                r_succ_of_td[0],
                r_succ_of_td[1],
                0 if int(r_succ_of_td[1]) == 0 else int(r_succ_of_td[0]) / int(r_succ_of_td[1]),
                int(row[12]),
                int(row[13]),
                0 if row[14] == '--' else int(row[14][:row[14].index(':')]) * 60 + int(row[14][row[14].index(':')+1:]),
                r_sig_str_of_head[0],
                r_sig_str_of_head[1],
                0 if int(r_sig_str_of_head[1]) == 0 else int(r_sig_str_of_head[0]) / int(r_sig_str_of_head[1]),
                r_sig_str_of_body[0],
                r_sig_str_of_body[1],
                0 if int(r_sig_str_of_body[1]) == 0 else int(r_sig_str_of_body[0]) / int(r_sig_str_of_body[1]),
                r_sig_str_of_leg[0],
                r_sig_str_of_leg[1],
                0 if int(r_sig_str_of_leg[1]) == 0 else int(r_sig_str_of_leg[0]) / int(r_sig_str_of_leg[1]),
                r_sig_str_of_distance[0],
                r_sig_str_of_distance[1],
                0 if int(r_sig_str_of_distance[1]) == 0 else int(r_sig_str_of_distance[0]) / int(r_sig_str_of_distance[1]),
                r_sig_str_of_clinch[0],
                r_sig_str_of_clinch[1],
                0 if int(r_sig_str_of_clinch[1]) == 0 else int(r_sig_str_of_clinch[0]) / int(r_sig_str_of_clinch[1]),
                r_sig_str_of_ground[0],
                r_sig_str_of_ground[1],
                0 if int(r_sig_str_of_ground[1]) == 0 else int(r_sig_str_of_ground[0]) / int(r_sig_str_of_ground[1]),
                b_sig_str_of_hit[0],
                b_sig_str_of_hit[1],
                0 if int(b_sig_str_of_hit[1]) == 0 else int(b_sig_str_of_hit[0]) / int(b_sig_str_of_hit[1]),
                b_str_of_total[0],
                b_str_of_total[1],
                0 if int(b_str_of_total[1]) == 0 else int(b_str_of_total[0]) / int(b_str_of_total[1]),
                b_succ_of_td[0],
                b_succ_of_td[1],
                0 if int(b_succ_of_td[1]) == 0 else int(b_succ_of_td[0]) / int(b_succ_of_td[1]),
                int(row[26]),
                int(row[27]),
                0 if row[28] == '--' else int(row[28][:row[28].index(':')]) * 60 + int(row[28][row[28].index(':')+1:]),
                b_sig_str_of_head[0],
                b_sig_str_of_head[1],
                0 if int(b_sig_str_of_head[1]) == 0 else int(b_sig_str_of_head[0]) / int(b_sig_str_of_head[1]),
                b_sig_str_of_body[0],
                b_sig_str_of_body[1],
                0 if int(b_sig_str_of_body[1]) == 0 else int(b_sig_str_of_body[0]) / int(b_sig_str_of_body[1]),
                b_sig_str_of_leg[0],
                b_sig_str_of_leg[1],
                0 if int(b_sig_str_of_leg[1]) == 0 else int(b_sig_str_of_leg[0]) / int(b_sig_str_of_leg[1]),
                b_sig_str_of_distance[0],
                b_sig_str_of_distance[1],
                0 if int(b_sig_str_of_distance[1]) == 0 else int(b_sig_str_of_distance[0]) / int(b_sig_str_of_distance[1]),
                b_sig_str_of_clinch[0],
                b_sig_str_of_clinch[1],
                0 if int(b_sig_str_of_clinch[1]) == 0 else int(b_sig_str_of_clinch[0]) / int(b_sig_str_of_clinch[1]),
                b_sig_str_of_ground[0],
                b_sig_str_of_ground[1],
                0 if int(b_sig_str_of_ground[1]) == 0 else int(b_sig_str_of_ground[0]) / int(b_sig_str_of_ground[1]),
        ], dtype=object)

    cleaned_fight_details["date"] = pd.to_datetime(cleaned_fight_details['date'])
    cleaned_fight_details = cleaned_fight_details.sort_values(by='date')
    cleaned_fight_details.to_csv('../dataset/cleaned_fight_details.csv', index=False)

if __name__ == "__main__":
    clean_data()
