import datetime
import pandas as pd
from numpy import nan, isnan

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


races_results = pd.read_csv("./f1_data/formatted_data/formatted_qualifying_data.csv")


def format_results(result):
    q1_time = result['q1_time']
    q2_time = result['q2_time']
    q3_time = result['q3_time']
    # if not isnan(race_time_ms):
    #     race_time_ms_timedelta = datetime.timedelta(milliseconds=race_time_ms)
    #     split_race_time = str(race_time_ms_timedelta).rsplit(':', 1)
    #     split_race_time_mins_secs = split_race_time[0]
    #     split_race_time_ms = split_race_time[1]
    #     split_race_time_ms_rounded = str(round(float(split_race_time_ms))).zfill(2)
    #     result['time'] = f"{split_race_time_mins_secs}:{split_race_time_ms_rounded}"

    if q1_time and type(q1_time) == str:
        time_obj = datetime.datetime.strptime(q1_time, '%M:%S.%f').time()
        time_obj_min = time_obj.minute * 60000
        time_obj_sec = time_obj.second * 1000
        time_obj_ms = time_obj.microsecond / 1000
        formatted_ms = time_obj_min + time_obj_sec + time_obj_ms
        result['q1_time_ms'] = int(formatted_ms)

    if q2_time and type(q2_time) == str:
        time_obj = datetime.datetime.strptime(q2_time, '%M:%S.%f').time()
        time_obj_min = time_obj.minute * 60000
        time_obj_sec = time_obj.second * 1000
        time_obj_ms = time_obj.microsecond / 1000
        formatted_ms = time_obj_min + time_obj_sec + time_obj_ms
        result['q2_time_ms'] = int(formatted_ms)

    if q3_time and type(q3_time) == str:
        time_obj = datetime.datetime.strptime(q3_time, '%M:%S.%f').time()
        time_obj_min = time_obj.minute * 60000
        time_obj_sec = time_obj.second * 1000
        time_obj_ms = time_obj.microsecond / 1000
        formatted_ms = time_obj_min + time_obj_sec + time_obj_ms
        result['q3_time_ms'] = int(formatted_ms)
    return result


new_race_results = races_results.apply(format_results, axis=1)
new_race_results.to_csv("./f1_data/formatted_data/formatted_qualifying_data.csv", index=False)
