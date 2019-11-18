planetList = [
    {'name': 'Mercury', 'eqRadiusKm': 2439.64},
    {'name': 'Venus', 'eqRadiusKm': 6051.59},
    {'name': 'Earth', 'eqRadiusKm': 6387.1},
    {'name': 'Mars', 'eqRadiusKm': 3397.0},
]

def setup():
    size(600,150)
    textAlign(LEFT,CENTER)
    
def draw():
    background(0)
    fill(255)
    planetCount = len(planetList)
    for i in range(planetCount):     
        #scale radius to be screen friendly
        planetRadius = planetList[i]['eqRadiusKm'] * 0.01 
        offset = 50 + ((width/planetCount) *i)    
        ellipse(offset,height/2, planetRadius, planetRadius)                         
        text(planetList[i]['name'], 10+offset+(planetRadius/2), height/2)  
