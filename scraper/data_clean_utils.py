
"""

    data: [
        referee,
        rounds,
        time,
        time_format,
        r_fighter,
        b_fighter,
        r_win,
        b_win,
        r_sig_str_of_total,
        r_suc_td_of_total,
        r_sub_att,
        r_rev,
        r_ctrl,
        b_sig_str_of_total,
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

    @ensures: [
        "referee"
        "date"
        "time_format"  
        "r_win"
        "r_fighter"
        "b_fighter"
        "r_kd"
        "r_Sig. str"
        "r_str_landed"
        "r_str_attempt"
        "r_Sig. str. %"
        "r_Total str. "
        "r_Td "
        "r_Td "
        "r_Sub. att"
        "r_Rev."
        "r_Ctrl"
        "b_Sig. str."
        "b_Sig. str. "
        "b_Total str. "
        "b_Td "
        "b_Td "
        "b_Sub. att"
        "b_Rev."
        "b_Ctrl"
        "r_Head"
        "r_Body"
        "r_Leg"
        "r_Distance"
        "r_Clinch"
        "r_Ground"
        "b_Head"
        "b_Body"
        "b_Leg"
        "b_Distance"
        "b_Clinch"
        "b_Ground"
    ]


    ['October 26, 2024', 'Vitor Ribeiro', '3', '5:00', '3 Rnd (5-5-5)', 'Mateusz Rebecki', 'Myktybek Orolbai', 'W', 'L', [71, 146], [93, 174],
 [3, 4], '75%', '0', ([61, 135],), [85, 162], [2, 5], '40%', '0', [52, 123], [10, 11], [9, 12], [54, 126], [5, 6], [12, 14], [46, 114], [6
, 11], [9, 10], [60, 133], [0, 1], [1, 1]]

"""

def calc_total_time(time_split, rounds, final_round_time):
    total_match_time = 0
    round_index = 0

    while round_index < int(rounds) - 1:
        total_match_time = time_split[round_index] * 60
        round_index += 1

    return total_match_time + int(final_round_time[:1]) * 60 + int(final_round_time[-2:])


def page_data_refining(data):

    total_match_time = calc_total_time(
            time_split=data[4][6:-1].split("-"), 
            rounds=data[1], 
            final_round_time=data[2]
        )

    return [
            data[0],
            data[1],
            data[2],
            data[3],
            total_match_time,
            data[5],
            data[6],
            data[7],
            data[8],
            data[9][0],
            data[9][1],
            data[9][0] / data[9][1],
    ]

def split_by_of(stat):
    return stat.strip("\n ").split(" of ")

def trim_newline_stat(stat):
    return stat.strip("\n ")

def clean_stat(stat):
    if stat == "---":
        return -1
    return stat

