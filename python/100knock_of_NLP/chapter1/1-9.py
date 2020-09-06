import random
string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
word_list = string.split(' ')
print(word_list)

for i in range(int(len(word_list))):
    j = random.randint(1, len(word_list)-1)
    k = random.randint(1, len(word_list)-1)
    if ((len(word_list[j]) > 4) and (len(word_list[k]) > 4)):
        tmp = word_list[j]
        word_list[j] = word_list[k]
        word_list[k] = tmp

print(word_list)
