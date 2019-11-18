class Ball():

    def __init__(self, tempR, newColor):
        global r, x, y, xspeed, yspeed, myColor
        self.r = tempR
        self.x = random(width)
        self.y = random(height)
        self.xspeed = random(-5, 5)
        self.yspeed = random(-5, 5)
        self.myColor = newColor
        #print 'ball ', self.x, self.y, self.xspeed, self.yspeed, self.myColor

    def move(self):
        #global x,y,xspeed,yspeed
        self.x += self.xspeed
        self.y += self.yspeed

        if (self.x > width or self.x < 0):
            self.xspeed *= -1
        if (self.y > height or self.y < 0):
            self.yspeed *= -1

    def display(self):
        stroke(0)
        noStroke()
        fill(self.myColor)
        ellipse(self.x, self.y, self.r * 2, self.r * 2)

    def highlight(self):
        strokeWeight(12)
        stroke(127)
        fill('#0000FF')
        ellipse(self.x, self.y, self.r * 2, self.r * 2)

    def intersect(self, other):
        distance = dist(self.x, self.y, other.x, other.y)
        if (distance < self.r + other.r):
            return True
        else:
            return False