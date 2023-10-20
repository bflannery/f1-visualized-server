import datetime
from numpy import nan

import pandas as pd

# reading the csv file
seasons = pd.read_csv("./data/formatted_season.csv", usecols=['id', 'year'])
races = pd.read_csv("./data/races.csv")

years_list = []
for i, row in seasons.iterrows():
    id = row[0]
    year = row[1]
    years_list.append({year: id})

for dict_item in years_list:
    # print(dict_item)
    races['year'] = races['year'].replace(dict_item)


# datetime_str = f"{df['fp1_date']} {df['fp1_time']}Z"


# # updating the column value/data
# df['year'] = df['year'].replace({1960: 11})


def test(race):
    zerod_time = '00:00:00'
    date = race['date']
    time = zerod_time if race['time'] == "\\N" else race['time']
    race["date"] = f"{date} {time}Z"

    fp1_date = race['fp1_date']
    fp1_time = race['fp1_time']
    if fp1_date == "\\N":
        race["fp1_date"] = nan
    elif fp1_date and fp1_time == "\\N":
        race["fp1_date"] = f"{fp1_date} {zerod_time}Z"
    else:
        race["fp1_date"] = f"{fp1_date} {fp1_time}Z"

    fp2_date = race['fp2_date']
    fp2_time = race['fp2_time']
    if fp2_date == "\\N":
        race["fp2_date"] = nan
    elif fp2_date and fp2_time == "\\N":
        race["fp2_date"] = f"{fp2_date} {zerod_time}Z"
    else:
        race["fp2_date"] = f"{fp2_date} {fp2_time}Z"

    fp3_date = race['fp3_date']
    fp3_time = race['fp3_time']
    if fp3_date == "\\N":
        race["fp3_date"] = nan
    elif fp3_date and fp3_time == "\\N":
        race["fp3_date"] = f"{fp3_date} {zerod_time}Z"
    else:
        race["fp3_date"] = f"{fp3_date} {fp3_time}Z"

    quali_date = race['quali_date']
    quali_time = race['quali_time']
    if quali_date == "\\N":
        race["quali_date"] = nan
    elif fp3_date and quali_time == "\\N":
        race["quali_date"] = f"{quali_date} {zerod_time}Z"
    else:
        race["quali_date"] = f"{quali_date} {quali_time}Z"

    sprint_date = race['sprint_date']
    sprint_time = race['sprint_time']
    if sprint_date == "\\N":
        race["sprint_date"] = nan
    elif fp3_date and quali_time == "\\N":
        race["sprint_date"] = f"{sprint_date} {zerod_time}Z"
    else:
        race["sprint_date"] = f"{sprint_date} {sprint_time}Z"

    return race


new_races = races.apply(test, axis=1)
# # writing into the file
new_races.to_csv("./data/formatted_races.csv", index=False)
