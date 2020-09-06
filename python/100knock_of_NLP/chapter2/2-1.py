path = 'hightemp.txt'

with open(path) as f:
    print(f)
    s = f.readlines()
    print(s)
    print('length of file is ' + str(len(s)))
