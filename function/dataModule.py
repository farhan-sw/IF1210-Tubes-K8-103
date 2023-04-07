

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

def cariRole(username, data_username):
    for i in range(count(data_username)):
        if(data_username[i][0] == username):
            return (data_username[i][2])
    return ("Unknown")

def printInfo(username, data_username):
    indeks = cariIndeks(username, data_username)
    for j in range(count(data_username[indeks])):
        if (j == 0) : print("Username: ", end="")
        elif(j == 1): print("Password: ", end="")
        elif(j==2)  : print("Role: ", end="")
        print(data_username[indeks][j], end="  ||  ")

        if(j==(count(data_username[indeks])-1)): print("")