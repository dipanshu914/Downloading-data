import csv

from datetime import datetime

from matplotlib import pyplot as plt


def get_weather_data(filename, dates, highs, lows):
    # get highs and lows from weather data.

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])

            except ValueError:
                print(current_date, "data not found")

            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


# Get weather data from sitka.
dates, highs, lows = [], [], []
get_weather_data("sitka_weather_2014.csv", dates, highs, lows)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="green", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="green", alpha=0.4)

# Get weather from death valley
dates, highs, lows = [], [], []
get_weather_data("death_valley_2014.csv", dates, highs, lows)
plt.plot(dates, highs, c="blue", alpha=0.5)
plt.plot(dates, lows, c="yellow", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="yellow", alpha=0.4)


# label a graph
title = "sitka-death_valley weather"
title += "comparison 2014"
plt.title(title)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature in f:", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()


