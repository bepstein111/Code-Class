x = 215 
def setup(): 
    size(480, 120) 

def draw(): 
    global x 
    if keyPressed and key == CODED: # If it's a coded key 
        if keyCode == LEFT: # If it's the left arrow 
            x -= 1 
        elif keyCode == RIGHT: # If it's the right arrow 
            x += 1 
    rect(x, 45, 50, 50)