class Ball():
    visible = False
    def __init__(self,ballX,ballY,ballVX,ballVY,ballDiam, ballR,ballG,ballB):
        global visible
        self.ballX = ballX
        self.ballY = ballY
        self.ballVX = ballVX
        self.ballVY = ballVY
        self.ballDiam = ballDiam
        self.ballCol = color(ballR,ballG,ballB)
        self.visible = True
 
    def moveBall(self):
        global visible
        if self.visible:
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
        
    def display(self):
        global visible
        if self.visible:
            stroke(0)
            noStroke()
            fill(self.ballCol)
            ellipse(self.ballX,self.ballY,self.ballDiam,self.ballDiam)
        
    def highlight(self):
        strokeWeight(12)
        stroke(255)
        fill(self.ballCol)
        ellipse(self.ballX,self.ballY,self.ballDiam,self.ballDiam)
        
    def intersect(self, other):
        distance = dist(self.ballX, self.ballY, other.ballX, other.ballY)
        if (distance < self.ballDiam/2 + other.ballDiam/2):
            return True
        else:
            return False  
    
    #very simple bouncing reaction
    def reverse(self):
        self.ballVX *= -1
        self.ballVY *= -1
    
    def disappear(self):
        global visible
        self.ballX = -3000
        self.ballY = -3000
        self.ballVX = 0.0
        self.ballVY = 0.0
        self.Diam = 5
        self.ballCol = 255
        self.visible = False
        
    def isVisible(self):
        global visible
        return self.visible
            