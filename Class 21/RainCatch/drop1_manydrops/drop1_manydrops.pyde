from Drop import Drop
global drop
dropList = []
numDrops = 1000  #but they appear all at once
def setup():
    frameRate(10)
    global numDrops, dropList
    size(400,400)
    background(0)
    for i in range(numDrops):
        dropList.append( Drop())

def draw():
    global x,y,drop
    background(0)
    for i in range(numDrops):
        dropList[i].move() #move down
        dropList[i].display()
        if dropList[i].reachedBottom():
            dropList[i] = Drop()
 