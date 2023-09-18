import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Creating and file
filename = "sanfrancisco.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # print(header_row)

    """ Using for loop to print column_header
    for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    dates, highs, lows = [], [], []

    for row in reader:
        if len(row) >= 4:  # Ensure the row has at least 4 columns
            try:
                current_date = datetime.strptime(row[1], "%Y-%m-%d")
                high = int(row[2])
                low = int(row[4])
            except ValueError:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Plot data
fig = plt.figure(dpi=130, figsize=(10, 5))
plt.plot(dates, highs, c="blue", alpha=0.5)
plt.plot(dates, lows, c="red", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="red", alpha=0.4)

# format a plot
plt.title("San francisco_weather condition", fontsize=18, c="red")
plt.xlabel("", fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Temperature in {f}", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize="16")

plt.show()













