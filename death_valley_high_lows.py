import csv

from datetime import datetime

from matplotlib import pyplot as plt


# Get date, high and low temperatures  from file.
filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    """for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot data.
fig = plt.figure(dpi=130, figsize=(10, 5))
plt.plot(dates, highs, c="blue", alpha=0.5)
plt.plot(dates, lows, c="green", alpha=0.8)
plt.fill_between(dates, highs, lows, facecolor="red", alpha=0.4)

# format the plot.
plt.title("Daily high & low Temperature of 2014 :", fontsize=18, c="red")
plt.xlabel("", fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Temperature in (f)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize="16")

plt.show()









