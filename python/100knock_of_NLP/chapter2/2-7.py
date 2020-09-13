path = 'hightemp.txt'

with open(path, mode = 'r') as f:
    str = f.readlines()

print(str[0])

str = str[0]
res = []

for i in range(len(str)):
    if str[i] not in res:
        res.append(str[i])

print(res)
