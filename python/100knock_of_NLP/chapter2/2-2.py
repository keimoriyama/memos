path = 'hightemp.txt'

with open(path) as f:
    s = f.read()
    s_space = s.replace('\t', ' ')
    print(s_space)
    f.wirte(s_space)
