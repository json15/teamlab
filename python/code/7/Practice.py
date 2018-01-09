import csv
comand_data = []

with open('comand_data.cvs', 'r') as csv_file:
    spamreader = csv.reader(csv_file, del)