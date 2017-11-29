class Drop():

    r = 8  # radus of drop
    x = None
    y = None

    def __init__(self):
        global x, y, speed, c
        self.x = random(width)
        self.y = 0
        self.speed = random(1, 5)
        c = color(50, 100, 150)

    def move(self):
        global y, speed
        self.y = self.y + self.speed

    def display(self):
        global x, y, d
        noStroke()
        ellipse(self.x, self.y, self.r, self.r)  # 'raindrop'

    def reachedBottom(self):
        if (self.y > height + self.r):
            return True
        else:
            return False
        
    def intersect(self, other):
        distance = dist(self.x, self.y, other.x, other.y)
        if (distance < self.r + other.r):
            return True
        else:
            return False