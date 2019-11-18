import csv

statsFileHandle = open('ortiz.csv')
statsData = csv.reader(statsFileHandle) 
for row in statsData:
    year = row[0]
    homeRuns = row[1]
    rbi = row[2]
    average = row[3]
    print year, homeRuns, rbi, average