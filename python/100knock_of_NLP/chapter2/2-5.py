import sys

args = sys.argv

path = 'hightemp.txt'
col = []

print(args[1])
arg = int(args[1])

with open(path, mode = 'r') as f:
    for file_list in f:
        col.append(file_list.split())


for i in range(len(col)):
    for j in reversed(range(arg,len(col[0]))):
        print(col[i][j] + " ",end="")
    print('\n')
