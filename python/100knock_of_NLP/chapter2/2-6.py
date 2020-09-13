import sys

args = sys.argv

N = int(args[1])

path = 'hightemp.txt'
col = []

with open(path, mode = 'r')as f:
    for file in f:
        col.append(file.split())

n = len(col[1])
j = 0

if N < n:
    for i in range(len(col)):
        while j < n:
            if j > 0 and j % N == 0:
                print("|",end = " ")
            print(col[i][j], end=" ")
            j+=1
        print()
        j = 0
