import csv

with open ("HeightWeight.csv",newline="") as f:
    file=csv.reader(f)
    newList=list(file)
newList.pop(0)
newData=[]
for i in range(len(newList)):
    weights=newList[i][2]
    newData.append(float(weights))

n = len(newData)
newData.sort()

if n % 2 == 0 :
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])
    median = (median1+median2)/2

else:
    median = newData[n/2]
    print(n)
    print("Median is : " + str(median))

