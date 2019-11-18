#http://py.processing.org/reference/loadStrings.html

  
lines = loadStrings("lovesong.txt")
print("there are %i lines" % len(lines))
for line in lines:
    print(line)
    
lines = loadStrings("http://processing.org/about/index.html")
print("there are %i lines" % len(lines))
for line in lines:
    print(line)