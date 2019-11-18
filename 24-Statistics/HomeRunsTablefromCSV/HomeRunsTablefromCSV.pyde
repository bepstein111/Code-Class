import csv
homeRuns = list()

def setup():
    size(480,120)
    statsFileHandle = open('ortiz.csv')
    statsData = csv.reader(statsFileHandle)
    for row in statsData:
        homeRuns.append(int(row[1]))
    print homeRuns

def draw():
    background(204)
    #Draw background grid for data
    stroke(255)
    line(20, 100, 20, 20)
    line(20, 100, 460, 100)
    for i in range(len(homeRuns)):
        x = map(i, 0, len(homeRuns)-1, 20, 460)
        line(x, 20, x, 100)
    #Draw lines based on home run data
    noFill()
    stroke(0)
    beginShape()
    for i in range(len(homeRuns)):
        x = map(i, 0, len(homeRuns)-1, 20,460)
        y = map(homeRuns[i], 0, 60, 100, 20)
        vertex(x,y)
    endShape()