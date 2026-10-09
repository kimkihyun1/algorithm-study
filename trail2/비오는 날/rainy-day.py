n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Weather_Info:
    def __init__(self, date="", day="", weather=""):
        self.date = date
        self.day = day
        self.weather = weather

total = []

for i in range(n):
    total.append(Weather_Info(date[i], day[i], weather[i]))

rain_day = []

for i in range(n):
    if total[i].weather == "Rain":
        rain_day.append(total[i])

date_idx = 0
for i, info in enumerate(rain_day):
    if info.date < rain_day[date_idx].date:
        date_idx = i

print(rain_day[date_idx].date, rain_day[date_idx].day, rain_day[date_idx].weather)