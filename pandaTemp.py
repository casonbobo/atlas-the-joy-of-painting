import csv

# Open the input CSV file
with open('temp.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Replace the first column with iterating count starting at 1 and prefixed with 'EID'
for row_index in range(1, len(data)):
    # Replace the first column with 'EID' followed by the row index plus 1
    data[row_index][0] = f'EID{row_index + 1}'

# Open the output CSV file
with open('temp.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(data)
