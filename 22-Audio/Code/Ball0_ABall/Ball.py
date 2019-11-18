class Ball():
    # A ball template
    def __init__(self,ballX,ballY,ballVX,ballVY,ballDiam, ballR,ballG,ballB):
        #variables each ball will be initiaized with
        self.ballX = ballX
        self.ballY = ballY
        self.ballVX = ballVX
        self.ballVY = ballVY
        self.ballDiam = ballDiam
        self.ballCol = color(ballR,ballG,ballB)
 
    def moveBall(self):
        # a function for the ball position 
        #based on X, Y Position, VX, VY
        fill(self.ballCol)
             
        #bounce when we hit the wals
        if (self.ballX>width):  #right side
            self.ballVX = -1 * 5 
        elif (self.ballX<0):    #left side
            self.ballVX = 5
        if (self.ballY>height): #bottom
            self.ballVY = -1 * 5 
        elif (self.ballY<0):    #top
            self.ballVY = 5
        
        #update position
        self.ballX = self.ballX + self.ballVX
        self.ballY = self.ballY + self.ballVY
        ellipse(self.ballX,self.ballY,self.ballDiam,self.ballDiam)