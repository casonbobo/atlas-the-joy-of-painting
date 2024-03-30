import csv

# Open the input CSV file
with open('temp.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Append 'COL' to the front of each index of an array in the second column
for row_index in range(len(data)):
    # Assuming the second column is the one you want to modify
    # Adjust the index if your CSV structure is different
    second_column_index = 1 # Indexing starts at 0, so 1 is the second column
    data[row_index][second_column_index] = 'COL' + data[row_index][second_column_index]

# Open the output CSV file
with open('temp.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(data)
