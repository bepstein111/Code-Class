x = 0
def setup():
   

    size(600,600)
    background(127)
    
def draw():
    global x
    rect(x, 100, 100, 400)
    x = x + 1
    
#Need to use th globl keyword for any kind of assignment 
#before using it, otherwise you get the err
# x "referenced before assignment"