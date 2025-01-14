import json 

with open('precipitation.json') as file:
    contents_rain = json.load(file)

# filter out only seattle
rain_seattle = []
for item in contents_rain:
    if item['station'] == 'GHCND:US1WAKG0038':
        rain_seattle.append(item)

# total monthly precipitation

total_precipitation = 0

# months =[]
# for element in rain_seattle:
#     month = int(element['date'].split('-')[1])
#     if month not in months:
#         months.append(month)

sum_of_month = []


for month in range(1, 13):
    total_precipitation = 0
    for element in rain_seattle:
        if int(element['date'].split('-')[1]) == month:
            total_precipitation = total_precipitation + element['value']
    sum_of_month.append(total_precipitation) 
    

# total yearly precipitation
total_yearly_precipitation = sum(sum_of_month)

# relative mothly precipitation

relative_monthly_list = []

for item in sum_of_month:
    relative_monthly_precipitation = item / total_yearly_precipitation
    relative_monthly_list.append(relative_monthly_precipitation)


# putting everything in results.json

data = {
    "Seattle": {
        "station" : "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": sum_of_month,
        "total_yearly_precipitation": total_yearly_precipitation,
        "relative_monthly_precipitation": relative_monthly_list
    }
}
    

with open('results.json', 'w') as file:
    json.dump(data, file, indent=4)
    
   
