x = 0
direction = 1
def setup():
    size(600,600)
    background(127)
    
def draw():
    global x
    global direction
    rect(x, 100, 100, 400)
    x = x + direction * 5
    if x>=480:
        direction = -1
    if x<=0:
        direction = 1
    
    
    
#Need to use th globl keyword for any kind of assignment 
#before using it, otherwise you get the err
# x "referenced before assignment"