class Drop():

    r = 16  # radius of drop
    x = None
    y = None
    c = None

    def __init__(self):
        global x, y, speed, c
        self.x = random(width)
        self.y = 0
        self.speed = random(1, 5)
        c = color(50, 200, 150)

    def move(self):
        global y, speed
        self.y = self.y + self.speed

    def display(self):
        global x, y, d ,c 
        noStroke()
        for i in range(4):
            noStroke()
            fill(c)
            ellipse(self.x,self.y+i*8,i*8,i*8)
        
    def reachedBottom(self):
        if (self.y > height + self.r*2):
            return True
        else:
            return False
        
    def intersect(self, other):
        global x,y,r
        distance = dist(self.x, self.y, other.x, other.y)
        if (distance < self.r + other.r):
            return True
        else:
            return False
    
    def caught(self):
        global y, speed
        self.speed = 0
        self.y = -40
    
    