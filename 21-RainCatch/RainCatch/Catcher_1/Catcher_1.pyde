from Catcher import Catcher
catcher = None

def setup():
    global catcher
    size(400, 400)
    catcher = Catcher(32)
    smooth()
    
def draw():
    global catcher
    background(255)
    catcher.setLocation(mouseX, mouseY)
    catcher.display()
