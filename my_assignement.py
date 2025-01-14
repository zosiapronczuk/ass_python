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

months =[]
for element in rain_seattle:
    month = int(element['date'].split('-')[1])
    if month not in months:
        months.append(month)

print(months)


for month in months:
    for element in rain_seattle:
        if element['date'].startswith(f'2010-{month}'):
            total_precipitation = total_precipitation + element['value']
            sum_of_month.append(total_precipitation) 



print(sum_of_month)    











with open('results.json', 'w') as file:
    json.dump(rain_seattle, file, indent=4)



    