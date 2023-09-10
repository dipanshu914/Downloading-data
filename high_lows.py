import csv

from datetime import datetime

from matplotlib import pyplot as plt


# Get date and high temperatures from file.
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    """for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

    # print(highs)

# plot data
fig = plt.figure(dpi=130, figsize=(10, 5))
plt.plot(dates, highs, c="blue")

# format the plot.
plt.title("Daily high Temperature, of 2014 july:", fontsize=18, c="red")
plt.xlabel("", fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature in (f)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize="16")

plt.show()









