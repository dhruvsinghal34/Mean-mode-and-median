import csv

with open ("HeightWeight.csv",newline="") as f:
    file=csv.reader(f)
    newList=list(file)
newList.pop(0)
newData=[]
for i in range(len(newList)):
    weights=newList[i][2]
    newData.append(float(weights))

total=0
for i in newData:
    total=total+i

number=len(newData)

mean = total / number

print(mean)
