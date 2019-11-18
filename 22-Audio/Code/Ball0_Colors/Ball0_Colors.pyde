 #from the Ball.py file, import the Ball class
from Ball import Ball  
numBalls = 200
ballList =[]
for i in range(numBalls):    
    ballList.append ( Ball(random(10),random(10),\
                        random(10),random(10),\
                        random(100), random(255),\
                        random(255), random(255) ) )

def setup():
    background(0)
    size(640,480)
    
def draw():
    background(0)
    for i in range(len(ballList)):    
        ballList[i].moveBall()
