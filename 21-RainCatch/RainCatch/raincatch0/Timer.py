class Timer():
    #savedTime= None
    #totalTime = 5000
    
    def __init__(self,tempTotalTime):
        self.totalTime = tempTotalTime
        
    def start(self):
        self.savedTime = millis()
    
    def isFinished(self):
        self.passedTime = millis() - self.savedTime
        if (self.passedTime > self.totalTime):
            return True
        else:
            return False