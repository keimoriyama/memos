path = 'hightemp.txt'

col = []

with open(path, mode = 'r')as f:
    for file in f:
        col.append(file.split())

for i in range(len(col)):
    for j in range(len(col)):
        if col [i][2] > col[j][2]:
            tmp = col[i]
            col[i] = col[j]
            col[j] = tmp

for i in range(len(col)):
    print(col[i])
