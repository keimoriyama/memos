def n_gram(text, n):
    return [text[i: i+n]for i in range(len(text)-n+1)]


string = "I am an NLPer"

print(n_gram(string, 1))
print(n_gram(string, 2))
