import json 
import csv

with open('precipitation.json') as file:
    contents_rain = json.load(file)

with open('stations.csv') as file1:
    stations = list(csv.DictReader(file1))

station_codes = []
for item in stations:
    station_codes.append(item['Station'])

observations_per_station = []
for element in contents_rain:
    for item in station_codes:
        observations_
        if element['Station'] == item:
            



print(rain_in_stations)

# # station_code = []
# # for item in contents_rain:
# #     if item['station'] not in station_code:
# #         station_code.append(item['station'])

# for item in station_codes:


# # total monthly precipitation

# total_precipitation = 0

# months =[]
# for element in rain_seattle:
#     month = int(element['date'].split('-')[1])
#     if month not in months:
#         months.append(month)

# sum_of_month = []


# for month in range(1, 13):
#     total_precipitation = 0
#     for element in rain_seattle:
#         if int(element['date'].split('-')[1]) == month:
#             total_precipitation = total_precipitation + element['value']
#     sum_of_month.append(total_precipitation) 
    

# # total yearly precipitation
# total_yearly_precipitation = sum(sum_of_month)

# # relative mothly precipitation

# relative_monthly_list = []

# for item in sum_of_month:
#     relative_monthly_precipitation = item / total_yearly_precipitation
#     relative_monthly_list.append(relative_monthly_precipitation)


# # putting everything in results.json

# data = {
#     "Seattle": { 
#         "station": "GHCND:US1WAKG0038",
#         "state": "WA",
#         "total_monthly_precipitation": sum_of_month,
#         "total_yearly_precipitation": total_yearly_precipitation,
#         "relative_monthly_precipitation": relative_monthly_list,
#         "relative_yearly_precipitation": "lol"
#     }
# }
    

# with open('results.json', 'w') as file:
#     json.dump(data, file, indent=4)
   
