def mean(sequence):
    sum = 0.0
    for element in sequence:
        sum = sum + element
    return sum/len(sequence)

values = [10, 9, 73, 25, 33,76, 52, 1, 35, 86]

print mean(values)

def setup():
    size(200,200)
    for i in range(len(values)):
        rect( i*20, 100-values[i], 20, values[i])
    rect(0, 100-mean(values), 200, 0)
    
    text("Mean = "+str(mean(values)), 100,120)