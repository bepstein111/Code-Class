class Drop():

    d = 8  # diameter of drop
    x = None
    y = None

    def __init__(self):
        global x, d, y, speed, c
        self.x = random(width)
        self.y = self.d * -2 #start a little above
        self.speed = random(1, 5)
        c = color(50, 100, 150)

    def move(self):
        global y, speed
        self.y = self.y + self.speed

    def display(self):
        global x, y, d
        noStroke()
        ellipse(self.x, self.y, self.d, self.d)  # 'raindrop'

    def reachedBottom(self):
        if (self.y > height + self.d):
            return True
        else:
            return False