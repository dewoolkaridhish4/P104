import csv
with open("height-weight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    n_num=filedata[i][1]
    newdata.append(float(n_num))

n=len(newdata)
newdata.sort()

if(n%2==0):
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]

print("MEDIAN = " +str(median))

import csv
with open("Internet Users.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    n_num=filedata[i][1]
    newdata.append(float(n_num))

n=len(newdata)
newdata.sort()

if(n%2==0):
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]

print("MEDIAN = " +str(median))