import pandas as pd

def fighter_clean():
    fighter_df = pd.read_csv('../dataset/fighter_details.csv')

    print(fighter_df)

fighter_clean()
