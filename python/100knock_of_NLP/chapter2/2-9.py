path = 'hightemp.txt'

col = []
with open(path, mode = 'r')as f:
    for file in f:
        col.append(file.split())


