path = 'hightemp.txt'
col1_txt = 'col1.txt'
col2_txt = 'col2.txt'
col1, col2 = [], []

with open(path, mode='r') as f:
    for file_list in f:
        col1.append(file_list.split()[0])
        col2.append(file_list.split()[1])

with open(col1_txt, mode='w') as fw:
    fw.write('\n'.join(col1))

with open(col2_txt, mode='w') as fw:
    fw.write('\n'.join(col2))
