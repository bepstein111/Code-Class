from Catcher import Catcher
from Drop import Drop
catcher = None

totalDrops = 0 #keep track of drops we're using
dropList = [None] * 1000

def setup():
    global catcher
    size(400, 400)
    catcher = Catcher(32)
    smooth()
    
def draw():
    global catcher,totalDrops
    background(0)
    catcher.setLocation(mouseX, mouseY)
    catcher.display()
    dropList[totalDrops] = Drop()
    totalDrops = totalDrops+1
    if (totalDrops >= len(dropList)):
        totalDrops = 0
    for i in range(totalDrops):
        dropList[i].move() #move each drop down
        dropList[i].display()
        if dropList[i].reachedBottom():
            dropList[i] = Drop() 
        if dropList[i].intersect(catcher):
            print('caught drop:'+str(i),10,420)
             