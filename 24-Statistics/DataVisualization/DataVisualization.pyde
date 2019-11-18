values = [10, 9, 73, 25, 33, 76, 52, 9, 35, 86]

def mean(sequence):
    sum = 0.0
    for element in sequence:
        sum = sum + element
    return sum/len(sequence)

def median(seq):
    seq.sort()
    half = len(seq)/2
    if (len(seq)%2 == 0):
        return list([seq[half-1],seq[half]])
    else:
        return seq[half]
    
def mode(s):
    counted = []
    frequent = []
    for num in s:
        counted.append( s.count(num))
    print counted
    maximum_occurrences = max(counted)
    print maximum_occurrences
    for ind in range(len(counted)):
        if counted[ind] == maximum_occurrences:
            if s[ind] not in frequent:
                frequent.append(s[ind])
    return frequent

### Color palette
pal = { "avgcol": color(150,40,90),
       "medcol": color(30,30,100),
       "modcol": color(100,100,155) }

### Visualizing the Data
def setup():
    size(300,300)
    #Calculate the results
    avg = mean(values)
    mod = mode(values)
    med = median(values)
    #Draw each data point
    for i in range(len(values)):
        if (values[i] in mod):
            fill(pal["modcol"])
        elif (values[i] == round(avg)):
            fill(pal["avgcol"])
        elif (values[i] in med):
            fill(pal["medcol"])
        else:
            fill(255)
        rect( i * 30, height/2-values[i], 30, values[i] )
    #write the text
    textSize(16)
    fill(pal["avgcol"])
    stroke(2)
    rect(0, height/2-avg, 300, 0)
    text("Mean = "+ str(avg), 100, 170)
    fill(pal["modcol"])
    text("Mode = "+ str(mod), 100,200)
    fill(pal["medcol"])
    text("Median ="+str(med),100,230)
    print values 
