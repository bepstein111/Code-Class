class Drop():
    
    d = 8 #diameter of drop
    x = None
    y = None

    def __init__(self):
        global x, y,speed,c
        self.x = random(width)
        self.y = 0
        self.speed = random(1,5)
        c = color(50,100, 150)

    def move(self):
        global y,speed
        self.y = self.y + self.speed
                
    def display(self):
        global x,y,d
        noStroke()
        ellipse(self.x,self.y,self.d,self.d)  #'raindrop'
 
        