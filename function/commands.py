# -------------------------------- MODUL BASIC COMMANDS ----------------------------------------

# function separate(sentence : string) -> array
# { Menerima masukan berupa string dan akan memberikan output pemenggalan mark}
# { Alternatif fungsi .split() }

# function count(data: array) -> integer
# { Menerima input array dan memberikan output banyaknya data di array tersebut }

def separate(sentence, mark=" "):
    split_value = []
    tmp = ''
    for c in sentence:
        if c == mark:
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
