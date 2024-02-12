import os
from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players
from datetime import datetime
import pandas as pd
import time
import requests

def get_nba_player_stats(season='2023-24', max_retries=5):
    # Get list of all NBA players
    nba_players = players.get_players()

    # Get players that are active
    active_nba_players = [player for player in nba_players if player['is_active'] == True]

    # Get a list of the player IDs for active players
    active_nba_player_ids = [player['id'] for player in active_nba_players]

    while max_retries > 0:
        try:
            df_all = pd.DataFrame()
            count_iteration = 0
            # Create a dataframe by iterating through each active player ID for the specified season
            for player_id in active_nba_player_ids:
                df = PlayerCareerStats(player_id=player_id, per_mode36='PerGame').get_data_frames()[0]
                df2 = df[df['SEASON_ID'] == season]
                # If a player has been on multiple teams in the same season, there will be more than one row in df2
                if df2.shape[0] > 1:
                    # Grab only the last row - this will always be the player's total stats for all teams played on
                    df2 = df2.tail(1)
                df_all = df_all.append(df2, ignore_index=True)
                count_iteration += 1
                print(f'{count_iteration} of {len(active_nba_player_ids)}')

            # If the loop completes without errors, break out of the retry loop
            break

        except requests.exceptions.ReadTimeout as e:
            max_retries -= 1
            print(f"ReadTimeoutError: {e}")
            if max_retries > 0:
                print(f"Retrying... {max_retries} attempts remaining.")
            else:
                print("Max retries reached. Script failed.")
                break

    if max_retries > 0:
        player_name_and_id = pd.DataFrame(active_nba_players)
        player_name_and_id_df = player_name_and_id[['id', 'full_name']]

        df_complete = df_all.merge(player_name_and_id_df, left_on='PLAYER_ID', right_on='id')
        df_complete.rename(columns={'full_name': 'FULL_NAME', 'TEAM_ABBREVIATION': 'TM'}, inplace=True)

        df_clean = df_complete[['PLAYER_ID',
                                'FULL_NAME',
                                'TM',
                                'PTS',
                                'AST',
                                'REB',
                                'GS',
                                'GP',
                                'MIN']]

        current_directory = os.getcwd()
        file_path = f'{current_directory}/log_outputs/'
        file_name = datetime.today().strftime("%Y%m%d") + '_' + datetime.today().strftime('%H%M') + '.csv'

        full_output_path = file_path + file_name

        df_clean.to_csv(full_output_path, index=False)

# Call the function with the desired season and maximum retries
get_nba_player_stats()