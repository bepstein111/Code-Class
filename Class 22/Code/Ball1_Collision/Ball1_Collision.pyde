 #from the Ball.py file, import the Ball class
from Ball import Ball  
numBalls = 5
ballList =[]
for i in range(numBalls):    
    #ballX,ballY,ballVX,ballVY,ballDiam, ballR,ballG,ballB
    ballList.append ( Ball(random(600)+10,random(400)+10,\
                        random(10),random(10),\
                        random(100), random(255),\
                        random(255), random(255) ) )

def setup():
    background(0)
    size(640,480)
    textSize(24)
    
def draw():
    background(0)
    for i in range(len(ballList)):    
        ballList[i].moveBall()
        
    #loop over every ball testing against all balls
    #note that this loop is inefficient
    for i in range(len(ballList)):
        for j in range(len(ballList)):
            if ballList[i]!=ballList[j]:
                if (ballList[i].intersect(ballList[j])):
                    text('bump ',10,460)
                    print('bump '+str(i)+str(j))