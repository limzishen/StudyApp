import csv

header = ['start_time ', 'end_time ', 'duration ']

# open the file in the write mode
with open('data.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write a row to the csv file
    writer.writerow(header)

    f.close()