savedTime= None
totalTime = 5000

def setup():
    global savedTime
    size(200,200)
    background(0)
    savedTime = millis()

def draw():    
    global savedTime,totalTime
    passedTime = millis() - savedTime

    if (passedTime > totalTime):
        background(random(255), 0, 0)
        savedTime = millis()
        