import csv

import matplotlib.pyplot as plt


# Get high temperatures from file.
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    """for index, column_header in enumerate(header_row):
        print(index, column_header)"""

    highs = []
    for row in reader:
        highs.append(row[1])

    # print(highs)

# plot data
fig = plt.Figure(dpi=128, figsize=(100, 50))
plt.plot(highs, c="blue")

# format the plot.
plt.title("Daily high Temperature of 2014 july:", fontsize=18)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature in (f)", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize="16")

plt.show()









