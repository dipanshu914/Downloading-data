import csv

from datetime import datetime

from matplotlib import  pyplot as plt

filename = "sitka_rainfall_2015.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # print(header_row)

    """ for index, column_header in enumerate(header_row):
        print(index, column_header) """

    dates, rainfall = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = float(row[19])
        except ValueError:
            print(current_date, "data not found")
        else:
            dates.append(current_date)
            rainfall.append(rain)

# plot a graph
fig = plt.figure(dpi=128, figsize=(10, 5))
plt.plot(dates, rainfall, c="red", alpha=1)
plt.fill_between(dates, rainfall, facecolor="red", alpha=0.5)


# label a figure
plt.title("Rainfall of sitka - 2015:")
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature in {f}", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize="16")

plt.show()
