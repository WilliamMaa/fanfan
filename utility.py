def findSemiColon(str, num):
    count = 0
    index = 0
    for i in str:
        if i == ";":
            count += 1
        if count == num:
            return index
        index += 1

def listToStringWithComma(L):
    result = ""
    for i in L:
        result += i + ","

    result = result[:-1]
    return result

def isSame(l1, l2):
    if len(l1) != len(l2):
        return False

    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            return False

    return True