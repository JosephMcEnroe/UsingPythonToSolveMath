index = 0;
rangeNum = 0
emptyList = []
num1 = 0
num2 = 1
rangeNum = int(input("Positive Integers Only!:"))
 
 #important, makes sure the correct amount is outputted correctly
rangeNum +=1 


#fibonacci Sequence 
#f(n) = f(n-1) + f(n-2) tip: use n as index
for index in range(rangeNum):
    if index == 0:
        emptyList.append(index)
        if rangeNum == 0:
            print(emptyList)
    if index == 1: 
        emptyList.append(index)
            
    if index >= 2:
        emptyList.append(num1 + num2)
        num1 = emptyList[-2]
        num2 = emptyList[-1]


print(emptyList)
