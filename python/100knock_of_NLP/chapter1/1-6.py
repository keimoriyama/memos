def n_gram(text, n):
    return [text[i: i+n]for i in range(len(text)-n+1)]


string = 'paraparaparadise'
string2 = 'paragraph'

X = set(n_gram(string, 2))
Y = set(n_gram(string2, 2))

union = X | Y
inter = X & Y
dif = X - Y

print(union)
print(inter)
print(dif)
