from Ball import Ball  
numBalls = 6
ballList =[]
bounce = -1

#make diameters bigger
def setup():
    background(0)
    size(640,480)
    for i in range(numBalls):    
        ballList.append ( Ball(random(width),random(height),\
                               random(5),random(5),\
                               random(50)+100, random(255),\
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
                ballA.highlight()
                ballB.highlight()
                ballA.reverse()
                ballB.reverse()
            else:
                text('    ',10,450)
            ballA.display()
            ballB.display()
        
def mouseClicked():
    clickX = mouseX
    clickY = mouseY
    for i in range(numBalls):
        if inBall(clickX,clickY,ballList[i]):
            ballList[i].disappear()
            print 'bye '+str(i)
            
def inBall(tempX,tempY,tempBall):
    distance = dist(tempX,tempY,tempBall.ballX,tempBall.ballY)
    if distance < tempBall.ballDiam/2 :
        return  True #clicked the Ball
    else:
        return  False  #missed

        
    