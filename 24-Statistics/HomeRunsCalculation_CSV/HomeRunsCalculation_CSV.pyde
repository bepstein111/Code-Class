import csv

statsFileHandle = open('ortiz.csv')
statsData = csv.reader(statsFileHandle)

homeRunTotal = 0
for row in statsData:
    homeRunTotal += int(row[1])

print homeRunTotal
