import math

file = open("h1q1.csv", "w")
def fun(input):
    # Output tuple of arrays, first array has is, second array has !is, third array has !i x is, last number is the sum. 
    sum = 0
    output = [[],[],[],0]
    i = 1
    while i <= input:
        output[0].append(i)
        output[1].append(math.factorial(i))
        output[2].append(math.factorial(i)*i)
        sum += math.factorial(i)*i
        i+=1
    output[3] = sum
    return output

for i in range(1,20):
    functionOutput = (fun(i))
    line = ""
    for i in range(0, 3):
        line+=str(functionOutput[i]).replace(",", "") + ","
    line+=str(functionOutput[3])
    line+="\n"  
    file.write(line)
file.close()