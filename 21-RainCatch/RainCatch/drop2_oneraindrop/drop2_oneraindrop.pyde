background(255)
size(100,100)
for i in range(5):
    noStroke()
    fill(0)
    ellipse(width/2,height/2+i*8,i*4,i*4)
    
#iteratively draw a sequence of circles, vertically
#getting wider a they move down.
            