import csv


# Creating and file
filename = "sanfrancisco.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # print(header_row)

    """ Using for loop to print column_header
    for index, column_header in enumerate(header_row):
        print(index, column_header)"""
















