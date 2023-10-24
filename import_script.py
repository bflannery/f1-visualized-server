import datetime
from numpy import nan

import requests

import pandas as pd

# reading the csv file
# seasons = pd.read_csv("./data/original_data/formatted_season.csv", usecols=['id', 'year'])
# races = pd.read_csv("./data/original_data/races.csv")
#
# years_list = []
# for i, row in seasons.iterrows():
#     id = row[0]
#     year = row[1]
#     years_list.append({year: id})
#
# for dict_item in years_list:
#     # print(dict_item)
#     races['year'] = races['year'].replace(dict_item)
#
#
# # datetime_str = f"{df['fp1_date']} {df['fp1_time']}Z"
#
#
# # # updating the column value/data
# # df['year'] = df['year'].replace({1960: 11})
#
#
# def test(race):
#     zerod_time = '00:00:00.000000'
#     date = race['date']
#     time = zerod_time if race['time'] == "\\N" else race['time']
#     race["date"] = f"{date} {time}"
#
#     fp1_date = race['fp1_date']
#     fp1_time = race['fp1_time']
#     if fp1_date == "\\N":
#         race["fp1_date"] = nan
#     elif fp1_date and fp1_time == "\\N":
#         race["fp1_date"] = f"{fp1_date} {zerod_time}Z"
#     else:
#         race["fp1_date"] = f"{fp1_date} {fp1_time}Z"
#
#     fp2_date = race['fp2_date']
#     fp2_time = race['fp2_time']
#     if fp2_date == "\\N":
#         race["fp2_date"] = nan
#     elif fp2_date and fp2_time == "\\N":
#         race["fp2_date"] = f"{fp2_date} {zerod_time}"
#     else:
#         race["fp2_date"] = f"{fp2_date} {fp2_time}"
#
#     fp3_date = race['fp3_date']
#     fp3_time = race['fp3_time']
#     if fp3_date == "\\N":
#         race["fp3_date"] = nan
#     elif fp3_date and fp3_time == "\\N":
#         race["fp3_date"] = f"{fp3_date} {zerod_time}"
#     else:
#         race["fp3_date"] = f"{fp3_date} {fp3_time}"
#
#     quali_date = race['quali_date']
#     quali_time = race['quali_time']
#     if quali_date == "\\N":
#         race["quali_date"] = nan
#     elif fp3_date and quali_time == "\\N":
#         race["quali_date"] = f"{quali_date} {zerod_time}"
#     else:
#         race["quali_date"] = f"{quali_date} {quali_time}"
#
#     sprint_date = race['sprint_date']
#     sprint_time = race['sprint_time']
#     if sprint_date == "\\N":
#         race["sprint_date"] = nan
#     elif fp3_date and quali_time == "\\N":
#         race["sprint_date"] = f"{sprint_date} {zerod_time}"
#     else:
#         race["sprint_date"] = f"{sprint_date} {sprint_time}"
#
#     return race
#
#
# new_races = races.apply(test, axis=1)
# # # writing into the file
# new_races.to_csv("./data/db_data/formatted_races.csv", index=False)

races = pd.read_csv("./data/db_data/formatted_races.csv")

formatted_races = []
for i, row in races.iterrows():
    ## id,season_id,round,circuit_id,name,date,fp1_date,fp2_date,fp3_date,qualifying_date,sprint_date,wki_url,
    race = {
        "id": row[0],
        "season_id": row[1],
        "round": row[2],
        "circuit_id": row[3],
        "name": row[4],
        "date": row[5],
        "fp1_date": None,
        "fp2_date": None,
        "fp3_date": None,
        "qualifying_date": None,
        "sprint_date": None,
        "wiki_url": row[11],
    }
    print(race)
    try:
        res = requests.post('http://localhost:8000/races', json=race)
        print(res.json())
    except:
        print(f"Error importing race {race.id}")
# print(races)
#
# for race in races:
#     try:
#         res = requests.post('http://localhost:8000/races', data=race)
#     except:
#         print(f"Error importing race {race.id}")
