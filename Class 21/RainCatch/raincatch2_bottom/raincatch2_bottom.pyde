from Catcher import Catcher
from Drop import Drop
from Timer import Timer
catcher = None
timer = None
totalDrops = 0 #keep track of drops we're using
dropList = [None] * 1000
bgColor = 255
time = 300
catch = 0
def setup():
    global catcher,timer,time,bgColor
    size(640, 360)
    catcher = Catcher(32)
    catcher.setLocation(mouseX,mouseY)
    smooth()
    timer = Timer(time)
    timer.start()
    background(bgColor)
    textSize(24)
    
def draw():
    global catcher,totalDrops, timer,bgColor
    global dropList,  catch
    background(bgColor)
    catcher.setLocation(mouseX, mouseY)
    catcher.display()
    
    if timer.isFinished() or totalDrops==0:
        dropList[totalDrops] = Drop()
        totalDrops += 1
        if totalDrops >= len(dropList):
            totalDrops = 0
        timer.start()

    for i in range(totalDrops):
        dropList[i].move() #move each drop down
        dropList[i].display()
        if catcher.intersect(dropList[i]):
            dropList[i].caught()
            catch += 1
        if dropList[i].reachedBottom():
            dropList[i].caught()
            
    fill(125,125,255)
    text('caught '+ str(catch),width-120,30)

             