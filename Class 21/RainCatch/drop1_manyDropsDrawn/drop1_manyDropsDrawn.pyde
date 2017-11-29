#use the draw function to create drops
from Drop import Drop
totalDrops = 0 #keep track of drops we're using
dropList = [None] * 1000
def setup():
    frameRate(10)
    size(400,400)
    smooth()
    background(0)

def draw():
    global totalDrops
    background(0)
    dropList[totalDrops] = Drop()  #create a new drop
    totalDrops = totalDrops+1  #increase the drop list
    if (totalDrops >= len(dropList)): #start over
        totalDrops = 0

    for i in range(totalDrops):
        dropList[i].move() #move each drop down
        dropList[i].display()
        if dropList[i].reachedBottom():
            dropList[i] = Drop()
    
    