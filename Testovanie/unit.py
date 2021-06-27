def upper_space(string):
    if type(string) not in [str]:
        return None

    str_ = str()
    for i in string:
        if i.isupper():
            str_ += f' {i}'
        else:
            str_ += i
    return str_


def highest_rank(arr):
    if type(arr) not in [list]:
        return None

    dic = dict()
    highest = 0
    key = 0
    for i in arr:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    for i in dic.keys():
        if dic[i] > highest:
            highest = dic[i]
            key = i
        elif dic[i] == highest:
            if key > i:
                pass
            else:
                key = i
    return key
