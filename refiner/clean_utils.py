def calc_total_time(rounds, round_format, final_round_time):

        round_index = 0
        round_format_arr = round_format[round_format.index('(')+1:-1].split('-')
        total_time = 0

        while round_index < rounds - 1: 
            total_time += int(round_format_arr[round_index]) * 60
            round_index += 1

        return total_time + int(final_round_time[:final_round_time.index(':')]) * 60 + int(final_round_time[final_round_time.index(':')+1:])

