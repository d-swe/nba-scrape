import requests
import csv
from unidecode import unidecode
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
    player_name = unidecode(player_name)    
    pos_tag = player_tag.find_next('td', {'data-stat': 'pos'})
    player_pos = pos_tag.get_text() if pos_tag else 'unknown'

    age_tag = player_tag.find_next('td', {'data-stat': 'age'})
    player_age = age_tag.get_text() if age_tag else 0
    
    team_tag = player_tag.find_next('td', {'data-stat': 'team_id'})
    player_team = team_tag.get_text() if team_tag else 'unknown'
    
    games_tag = player_tag.find_next('td', {'data-stat': 'g'})
    player_games = games_tag.get_text() if games_tag else 0
    
    games_start_tag = player_tag.find_next('td', {'data-stat': 'gs'})
    games_started = games_start_tag.get_text() if games_start_tag else 0
    
    minutes_tag = player_tag.find_next('td', {'data-stat': 'mp_per_g'})
    minutes_played = minutes_tag.get_text() if minutes_tag else 0

    field_goal_per_game_tag = player_tag.find_next('td', {'data-stat': 'fg_per_g'})
    field_goal_per_game = field_goal_per_game_tag.get_text() if field_goal_per_game_tag else 0

    field_attempt_tag = player_tag.find_next('td', {'data-stat': 'fga_per_g'})
    field_attempt_per_game = field_attempt_tag.get_text() if field_attempt_tag else 0

    field_percent_tag = player_tag.find_next('td', {'data-stat': 'fg_pct'})
    field_goal_percentage = field_percent_tag.get_text() if field_percent_tag else 0

    three_point_pg_tag = player_tag.find_next('td', {'data-stat': 'fg3_per_g'})
    three_point_pg = three_point_pg_tag.get_text() if three_point_pg_tag else 0

    three_point_attempt_tag = player_tag.find_next('td', {'data-stat': 'fg3a_per_g'})
    three_point_attempt_per_game = three_point_attempt_tag.get_text() if three_point_attempt_tag else 0
    
    three_point_percent_tag = player_tag.find_next('td', {'data-stat': 'fg3_pct'})
    three_point_percent_per_game = three_point_percent_tag.get_text() if three_point_percent_tag else 0

    two_point_pg_tag = player_tag.find_next('td', {'data-stat': 'fg2_per_g'})
    two_point_pg = two_point_pg_tag.get_text() if two_point_pg_tag else 0

    two_point_attempt_tag = player_tag.find_next('td', {'data-stat': 'fg2a_per_g'})
    two_point_attempt_pg = two_point_attempt_tag.get_text() if two_point_attempt_tag else 0

    two_point_percent_tag = player_tag.find_next('td', {'data-stat': 'fg2_pct'})
    two_point_percent = two_point_percent_tag.get_text() if two_point_percent_tag else 0

    effective_fg_percent_tag = player_tag.find_next('td', {'data-stat': 'efg_pct'})
    effective_fg_percent = effective_fg_percent_tag.get_text() if effective_fg_percent_tag else 0

    free_throw_pg_tag = player_tag.find_next('td', {'data-stat': 'ft_per_g'})
    free_throw_pg = free_throw_pg_tag.get_text() if free_throw_pg_tag else 0

    free_throw_attempt_tag = player_tag.find_next('td', {'data-stat': 'fta_per_g'})
    free_throw_attempt = free_throw_attempt_tag.get_text() if free_throw_attempt_tag else 0

    free_throw_percent_tag = player_tag.find_next('td', {'data-stat': 'ft_pct'})
    free_throw_percent = free_throw_percent_tag.get_text() if free_throw_percent_tag else 0

    off_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'orb_per_g'})
    off_reb_pg = off_reb_pg_tag.get_text() if off_reb_pg_tag else 0

    def_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'drb_per_g'})
    def_reb_pg = def_reb_pg_tag.get_text() if def_reb_pg_tag else 0

    tot_reb_pg_tag = player_tag.find_next('td', {'data-stat': 'trb_per_g'})
    tot_reb_pg = tot_reb_pg_tag.get_text() if tot_reb_pg_tag else 0

    ast_pg_tag = player_tag.find_next('td', {'data-stat': 'ast_per_g'})
    ast_pg = ast_pg_tag.get_text() if ast_pg_tag else 0

    stl_per_g_tag = player_tag.find_next('td', {'data-stat': 'stl_per_g'})
    stl_per_g = stl_per_g_tag.get_text() if stl_per_g_tag else 0

    blk_per_g_tag = player_tag.find_next('td', {'data-stat': 'blk_per_g'})
    blk_per_g = blk_per_g_tag.get_text() if blk_per_g_tag else 0

    to_per_g_tag = player_tag.find_next('td', {'data-stat': 'tov_per_g'})
    to_per_g = to_per_g_tag.get_text() if to_per_g_tag else 0

    pf_per_g_tag = player_tag.find_next('td', {'data-stat': 'pf_per_g'})
    pf_per_g = pf_per_g_tag.get_text() if pf_per_g_tag else 0

    points_pg_tag = player_tag.find_next('td', {'data-stat': 'pts_per_g'})
    points_pg = points_pg_tag.get_text() if points_pg_tag else 0

    player_stats = {
        'name': player_name,
        'postion': player_pos,
        'age': player_age,
        'team': player_team,
        'games_playd': player_games,
        'games_started': games_started,
        'minutes_played': minutes_played,
        'field_goal_pg': field_goal_per_game,
        'field_attempt_pg': field_attempt_per_game,
        'field_goal_percent': field_goal_percentage,
        'three_pt_pg': three_point_pg,
        'three_pt_attempt_pg': three_point_attempt_per_game,
        'three_pt_percent': three_point_percent_per_game,
        'two_pt_pg': two_point_pg,
        'two_pt_attempt_pg': two_point_attempt_pg,
        'two_pt_percent': two_point_percent,
        'effective_fg_percent': effective_fg_percent,
        'free_throw_pg': free_throw_pg,
        'free_throw_attempt_pg': free_throw_attempt,
        'free_throw_percent': free_throw_percent,
        'off_reb_pg': off_reb_pg,
        'def_reb_pg': def_reb_pg,
        'tot_reb_pg': tot_reb_pg,
        'ast_pg': ast_pg,
        'stl_pg': stl_per_g,
        'blk_pg': blk_per_g,
        'to_pg': to_per_g,
        'pf_pg': pf_per_g,
        'points_pg': points_pg,

    }

    players.append(player_stats)

df = pd.DataFrame(players)

df.to_csv("player_stats", index=True)
# fieldnames = list(players[0].keys())
# filename = 'player_stats.csv'
#
# with open(filename, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     for player in players:
#         writer.writerow(player)
#
# print("csv file successful", filename)
