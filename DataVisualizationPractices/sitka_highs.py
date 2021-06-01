import csv
import matplotlib.pyplot as plt

from datetime import datetime

#filename = 'files/csv/sitka_weather_07-2018_simple.csv'
filename2 = 'files/csv/sitka_weather_2018_simple.csv'

# with open(filename) as file:
with open(filename2) as file:
	reader = csv.reader(file)
	header_row = next(reader)
	print(header_row)

	dates, highs = [], []

	for index, column_header in enumerate(header_row):
		print(index, column_header)

	highs = []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		high = int(row[5])
		dates.append(current_date)
		highs.append(high)

print(highs)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#plt.title("Daily high temperatures, July 2018", fontsize=20)
plt.title("Daily high temperatures -- 2018", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()