class Ball():
    def __init__(self,ballX,ballY,ballVX,ballVY,ballDiam, ballR,ballG,ballB):
        self.ballX = ballX
        self.ballY = ballY
        self.ballVX = ballVX
        self.ballVY = ballVY
        self.ballDiam = ballDiam
        self.ballCol = color(ballR,ballG,ballB)
 
    def moveBall(self):
        fill(self.ballCol)
             
        if (self.ballX>width):
            self.ballVX = -1 * 5 
        elif (self.ballX<0):
            self.ballVX = 5
        if (self.ballY>height):
            self.ballVY = -1 * 5 
        elif (self.ballY<0):
            self.ballVY = 5
        self.ballX = self.ballX + self.ballVX
        self.ballY = self.ballY + self.ballVY
        ellipse(self.ballX,self.ballY,self.ballDiam,self.ballDiam)
        
    def intersect(self, other):
        distance = dist(self.ballX, self.ballY, other.ballX, other.ballY)
        if (distance < self.ballDiam/2 + other.ballDiam/2):
            return True
        else:
            return False  