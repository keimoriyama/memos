def chipter(text):
    word = ''
    for i in range(len(text)):
        if text[i].isalpha() == 1:
            word += chr(219 - ord(text[i]))
        else:
            word += str(text[i])
    return word


string = "1kie221lldjf"
print(chipter(string))
