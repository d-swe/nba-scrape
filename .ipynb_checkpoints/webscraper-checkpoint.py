import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

soup_str = str(soup)

# with open('pased_html.txt', 'w', encoding='utf-8') as file:
#     file.write(soup_str)

players = []

for player_tag in soup.find_all('td', {'data-stat': 'player'}):
    player_name = player_tag.get_text()
    
    pos_tag = player_tag.find_next('td', {'data-stat': 'pos'})
    player_pos = pos_tag.get_text() if pos_tag else 'unknown'

    age_tag = player_tag.find_next('td', {'data-stat': 'age'})
    player_age = age_tag.get_text() if age_tag else 'unknown'
    
    team_tag = player_tag.find_next('td', {'data-stat': 'team_id'})
    player_team = team_tag.get_text() if team_tag else 'unknown'
    
    games_tag = player_tag.find_next('td', {'data-stat': 'g'})
    player_games = games_tag.get_text() if games_tag else 'unknown'
    
    games_start_tag = player_tag.find_next('td', {'data-stat': 'gs'})
    games_started = games_start_tag.get_text() if games_start_tag else 'unknown'
    
    minutes_tag = player_tag.find_next('td', {'data-stat': 'mp_per_g'})
    minutes_played = minutes_tag.get_text() if minutes_tag else 'unknown'

    field_goal_per_game_tag = player_tag.find_next('td', {'data-stat': 'fg_per_g'})
    field_goal_per_game = field_goal_per_game_tag.get_text() if field_goal_per_game_tag else 'unknown'

    field_attempt_tag = player_tag.find_next('td', {'data-stat': 'fga_per_g'})
    field_attempt_per_game = field_attempt_tag.get_text() if field_attempt_tag else 'unknown'

    field_percent_tag = player_tag.find_next('td', {'data-stat': 'fg_pct'})
    field_goal_percentage = field_percent_tag.get_text() if field_percent_tag else 'unknown'

    three_point_pg_tag = player_tag.find_next('td', {'data-stat': 'fg3_per_g'})
    three_point_pg = three_point_pg_tag.get_text() if three_point_pg_tag else 'unknown'

    three_point_attempt_tag = player_tag.find_next('td', {'data-stat': 'fg3a_per_g'})
    three_point_attempt_per_game = three_point_attempt_tag.get_text() if three_point_attempt_tag else 'unknown'
    
    three_point_percent_tag = player_tag.find_next('td', {'data-stat': 'fg3_pct'})
    three_point_percent_per_game = three_point_percent_tag.get_text() if three_point_percent_tag else 'unknown'

    two_point_pg_tag = player_tag.find_next('td', {'data-stat': 'fg2_per_g'})
    two_point_pg = two_point_pg_tag.get_text() if two_point_pg_tag else 'unknown'

    two_point_attempt_tag = player_tag.find_next('td', {'data-stat': 'fg2a_per_g'})
    two_point_attempt_pg = two_point_attempt_tag.get_text() if two_point_attempt_tag else 'unknown'

    two_point_percent_tag = player_tag.find_next('td', {'data-stat': 'fg2_pct'})
    two_point_percent = two_point_percent_tag.get_text() if two_point_percent_tag else 'unknown'

    effective_fg_percent_tag = player_tag.find_next('td', {'data-stat': 'efg_pct'})
    effective_fg_percent = effective_fg_percent_tag.get_text() if effective_fg_percent_tag else 'unknown'

    free_throw_pg_tag = player_tag.find_next('td', {'data-stat': 'ft_per_g'})
    free_throw_pg = free_throw_pg_tag.get_text() if free_throw_pg_tag else 'unknown'

    free_throw_attempt_tag = player_tag.find_next('td', {'data-stat': 'fta_per_g'})
    free_throw_attempt = free_throw_attempt_tag.get_text() if free_throw_attempt_tag else 'unknown'

    free_throw_percent_tag = player_tag.find_next('td', {'data-stat': 'ft_pct'})
    free_throw_percent = free_throw_percent_tag.get_text() if free_throw_percent_tag else 'unknown'

    off_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'orb_per_g'})
    off_reb_pg = off_reb_pg_tag.get_text() if off_reb_pg_tag else 'unknown'

    def_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'drb_per_g'})
    def_reb_pg = def_reb_pg_tag.get_text() if def_reb_pg_tag else 'unknown'

    tot_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'trb_per_g'})
    tot_reb_pg = tot_reb_pg_tag.get_text() if tot_reb_pg_tag else 'unknown'

    ast_pg_tag = player_tag.find_next('td', {'data-stat': 'ast_per_g'})
    ast_pg = ast_pg_tag.get_text() if ast_pg_tag else 'unknown'

    stl_per_g_tag = player_tag.find_next('td', {'data-stat': 'stl_per_g'})
    stl_per_g = stl_per_g_tag.get_text() if stl_per_g_tag else 'unknown'

    blk_per_g_tag = player_tag.find_next('td', {'data-stat': 'blk_per_g'})
    blk_per_g = blk_per_g_tag.get_text() if blk_per_g_tag else 'unknown'

    to_per_g_tag = player_tag.find_next('td', {'data-stat': 'tov_per_g'})
    to_per_g = to_per_g_tag.get_text() if to_per_g_tag else 'unknown'

    pf_per_g_tag = player_tag.find_next('td', {'data-stat': 'pf_per_g'})
    pf_per_g = pf_per_g_tag.get_text() if pf_per_g_tag else 'unknown'

    points_pg_tag = player_tag.find_next('td', {'data-stat': 'pts_per_g'})
    points_pg = points_pg_tag.get_text() if points_pg_tag else 'unknown'

    player_stats = {
        'Name': player_name,
        'Position': player_pos,
        'Age': player_age,
        'Team': player_team,
        'Games Played': player_games,
        'Games Started': games_started,
        'Minutes Played Per Game': minutes_played,
        'Field Goals Per Game': field_goal_per_game,
        'Field Goal Attempts Per Game': field_attempt_per_game,
        'Field Goal Percentage': field_goal_percentage,
        '3-Point Field Goals Per Game': three_point_pg,
        '3-Point Field Goal Attempts Per Game': three_point_attempt_per_game,
        '3-Point Field Goal Percentage': three_point_percent_per_game,
        '2-Point Field Goals Per Game': two_point_pg,
        '2-Point Field Goal Attempts Per Game': two_point_attempt_pg,
        '2-Point Field Goal Percentage': two_point_percent,
        'Effective Field Goal Percentage': effective_fg_percent,
        'Free Throws Per Game': free_throw_pg,
        'Free Throw Attempts Per Game': free_throw_attempt,
        'Free Throw Percentage': free_throw_percent,
        'Offensive Rebounds Per Game': off_reb_pg,
        'Defensive Rebounds Per Game': def_reb_pg,
        'Total Rebounds Per Game': tot_reb_pg,
        'Assists Per Game': ast_pg,
        'Steals Per Game': stl_per_g,
        'Blocks Per Game': blk_per_g,
        'Turnovers Per Game': to_per_g,
        'Personal Fouls Per Game': pf_per_g,
        'Points Per Game': points_pg,

    }

    players.append(player_stats)

df = pd.DataFrame(players)

df.to_csv('data.csv', index=False)
