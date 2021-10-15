from collections import Counter
import csv

with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    n_num=filedata[i][1]
    newdata.append(float(n_num))

data=Counter(newdata)
modeforrange= {
    "50-60":0,
    "60-70":0,
    "70-80":0
}

for height,occurence in data.items():
    if 50<float(height)<60:
        modeforrange["50-60"]+=occurence
    elif 60<float(height)<70:
        modeforrange["60-70"]+=occurence
    elif 70<float(height)<80:
        modeforrange["70-80"]+=occurence

moderange,modeoccurence=0,0
for range,occurence in modeforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]),int(range.split("-")[0])],occurence

mode=float((moderange[0]+moderange[1])/2)
print("MODE = "+str(mode))