import csv
with open("hw.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    n_num=filedata[i][1]
    newdata.append(float(n_num))

n=len(newdata)
total=0

for x in newdata:
    total+=x

mean=total/n
print("Mean = " +str(mean))

