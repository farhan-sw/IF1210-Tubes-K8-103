def load(filename, data):

    print(filename)
    file=open(filename, "r")

    return data

def separate(sentence):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == ' ':
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_value.append(tmp)
    return split_value

def count(data):
    counter = 0
    for i in data:
        counter += 1
    return counter

def cariIndeks(username, data_username):
    for i in range(count(data_username)):
        if(data_username[i][0] == username):
            return i
    return (-999)