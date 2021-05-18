import csv
from collections import Counter 
with open ("HeightWeight.csv",newline="") as f:
    file=csv.reader(f)
    newList=list(file)
newList.pop(0)
newData=[]
for i in range(len(newList)):
    weights=newList[i][2]
    newData.append(float(weights))

data = Counter(newData)
modeDataForRange = {
    "50-60":0
    "60-70":0
    "70-80":0
}

for height , occurence in data.items():
    if 50 < float(Weight) <60:
        modeDataForRange["50-60"] += occurence 
    elif 60 < float(Weight) < 70:
        modeDataForRange["60-70"] += occurence
    elif 70 < float(Weight) < 80:
        modeDataForRange["70-80"] += occurence

modeRange,modeOccurence = 0,0
for range , occurence in modeDataForRange.items():
    if occurence  > modeOccurence:
        modeRange , modeOccurence = [int(range.split("-")[0]), int(range.split("-")[2])],occurence
mode = float((modeRange[0] + modeRange[2])/2)
print(f"mode is -> {mode:2f}")
