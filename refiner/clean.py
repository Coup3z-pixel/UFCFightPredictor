import pandas as pd
import numpy as np

from clean_utils import calc_total_time

def clean_data():
    fight_details = pd.read_csv('../dataset/fight_details.csv')

    cleaned_fight_details = pd.DataFrame(
            index=np.arange(0,len(fight_details)), 
            columns=["date", "referee","rounds","total_time","time_format","r_fighter","b_fighter","winner","r_total_sig_str","r_str_hit","r_attempt_td","r_succ_td","r_rev","r_ctrl","r_head_attempt","r_head_hit","r_body_attempt","r_body_hit","r_leg_attempt","r_leg_hit","r_distance_attempt","r_distance_hit","r_clinch_attempt","r_clinch_hit","r_ground_attempt","r_ground_hit","b_total_sig_str","b_str_hit","b_attempt_td","b_succ_td","b_rev","b_ctrl","b_head_attempt","b_head_hit","b_body_attempt","b_body_hit","b_leg_attempt","b_leg_hit","b_distance_attempt","b_distance_hit","b_clinch_attempt","b_clinch_hit","b_ground_attempt","b_ground_hit",]
        )
 
    for index, row in enumerate(fight_details.itertuples(index=False)):
        cleaned_fight_details.loc[index] = [
                row[0],
                row[1],
                row[2],
                calc_total_time(row[2], row[4], row[3]),
                row[4][row[4].index('(')+1:-1],
                row[5],
                row[6],"winner","r_total_sig_str","r_str_hit","r_attempt_td","r_succ_td","r_rev","r_ctrl","r_head_attempt","r_head_hit","r_body_attempt","r_body_hit","r_leg_attempt","r_leg_hit","r_distance_attempt","r_distance_hit","r_clinch_attempt","r_clinch_hit","r_ground_attempt","r_ground_hit","b_total_sig_str","b_str_hit","b_attempt_td","b_succ_td","b_rev","b_ctrl","b_head_attempt","b_head_hit","b_body_attempt","b_body_hit","b_leg_attempt","b_leg_hit","b_distance_attempt","b_distance_hit","b_clinch_attempt","b_clinch_hit","b_ground_attempt","b_ground_hit",]

    print("Clean data")
    print(fight_details)
    print(cleaned_fight_details)
    cleaned_fight_details.to_csv('../dataset/cleaned_fight_details.csv')

if __name__ == "__main__":
    clean_data()
