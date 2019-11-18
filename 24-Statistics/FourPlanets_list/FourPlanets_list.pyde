mercuryInfo = {
    "name": "Mercury",
    "knownMoons": 0,
    "eqRadiusKm": 2439.64,
}
venusInfo = {
    "name": "Venus",
    "knownMoons": 0,
    "eqRadiusKm": 6051.59,
}
earthInfo = {
    "name": "Earth",
    "knownMoons": 1,
    "eqRadiusKm": 6387.1,
}
marsInfo = {
    "name": "Mars",
    "knownMoons": 2,
    "eqRadiusKm": 3397.0
}
planetList = [mercuryInfo,venusInfo,earthInfo,marsInfo]
print planetList[2]['name']
print planetList[3]['knownMoons']

radiusSum = 0
for i in range(len(planetList)):
    radiusSum += planetList[i]['eqRadiusKm']
print radiusSum / len(planetList)

# or use the iterator syntax special to python
radiusSum = 0
for p in planetList:
    radiusSum += p['eqRadiusKm']
print radiusSum / len(planetList)

    