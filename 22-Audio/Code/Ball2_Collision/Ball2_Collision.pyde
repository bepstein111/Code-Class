 #from the Ball.py file, import the Ball class
from Ball import Ball  
numBalls = 7
ballList =[]
bounce = -1

def setup():
    background(0)
    size(640,480)
    for i in range(numBalls):    
        ballList.append ( Ball(random(width),random(height),\
                               random(10),random(10),\
                               random(100)+10, random(255),\
                               random(255), random(255) ) )
    
def draw():
    background(0)
    for i in range(len(ballList)):    
        ballList[i].moveBall()
    #test each ball for intersection
    for i in range(len(ballList)-1):
        ballA = ballList[i]
        for j in range(i+1,len(ballList)):
            ballB = ballList[j]
            if (ballA.intersect(ballB)):
                fill(255)
                text('bump ',10,450)
                print('bump '+str(i)+' '+str(j))
                ballA.highlight()
                ballB.highlight()
                ballA.reverse()
                ballB.reverse()
                saveFrame('collide.png')
            ballA.display()
            ballB.display()

def mousePressed():
    saveFrame('collide.png')