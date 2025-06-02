import pandas as pd
import numpy as np

def processing_data():
    fight_df = pd.read_csv('../dataset/cleaned_fight_details.csv')

    combined_fighters = pd.concat([fight_df['r_fighter'], fight_df['b_fighter']], ignore_index=True)
    unique_fighter_list = combined_fighters.unique()

    fighter_df = pd.DataFrame(
            index=np.arange(0, len(unique_fighter_list)),
            columns=["name","fight_no","elo","win_streak","lose_streak","wins","loss","draw","kd","sig_str","str_hit","sig_str_%","str_land","str_atmpt","str_land_%","td_atmp","td_succ","td-%","sub_att","rev","ctrl","head_hit","head_land","head_accuracy","body_hit","body_atmpt","body_accuracy","leg_hit","leg_land","leg_accuracy","distance_hit","distance_land","distance_accuracy","clinch_hit","clinch_land","clinch_accuracy","ground_hit","ground_land","ground_accuracy"]
        )

    for index, fighter in enumerate(unique_fighter_list):
        fighter_df.loc[index] = np.array([fighter, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    fighter_df.set_index('name', inplace=True) 

    train_df = pd.DataFrame(
            index=np.arange(0, len(fight_df)),
            columns=["r_wins", "r_fight_no","r_elo","r_win_streak","r_lose_streak","r_wins","r_loss","r_draw","r_kd","r_sig_str","r_str_hit","r_sig_str_%","r_str_land","r_str_atmpt","r_str_land_%","r_td_atmp","r_td_succ","r_td-%","r_sub_att","r_rev","r_ctrl","r_head_hit","r_head_land","r_head_accuracy","r_body_hit","r_body_atmpt","r_body_accuracy","r_leg_hit","r_leg_land","r_leg_accuracy","r_distance_hit","r_distance_land","r_distance_accuracy","r_clinch_hit","r_clinch_land","r_clinch_accuracy","r_ground_hit","r_ground_land","r_ground_accuracy", "b_fight_no","b_elo","b_win_streak","b_lose_streak","b_wins","b_loss","b_draw","b_kd","b_sig_str","b_str_hit","b_sig_str_%","b_str_land","b_str_atmpt","b_str_land_%","b_td_atmp","b_td_succ","b_td-%","b_sub_att","b_rev","b_ctrl","b_head_hit","b_head_land","b_head_accuracy","b_body_hit","b_body_atmpt","b_body_accuracy","b_leg_hit","b_leg_land","b_leg_accuracy","b_distance_hit","b_distance_land","b_distance_accuracy","b_clinch_hit","b_clinch_land","b_clinch_accuracy","b_ground_hit","b_ground_land","b_ground_accuracy"]
        )

    try:
        # go through fight_df chronologically
        for index, row in enumerate(fight_df.itertuples()):
            # compute the stat for each fighter
            

            # combine the results of each fighter into the train data


            # append the result row onto train_df


            print(row)

    finally: 
        train_df.to_csv('../dataset/train.csv')

if __name__ == "__main__":
    processing_data()
