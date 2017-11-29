#from the Ball.py file, import the Ball class
from Ball import Ball  
numBalls = 200

def setup():
    global ball #make ball available elsewhere
    background(0)
    size(640,480)
    ball =  Ball(random(10),random(10),random(10),
                 random(10),random(100), random(255),
                 random(255), random(255))

def draw():
    global ball  #get variable named ball from setup
    background(0)
    ball.moveBall()