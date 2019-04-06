



def finn_longest_common_prefix(string):
    a=list(string[0])
    b=list(string[1])
    c=list(string[2])
    len_min=(min(map(len,string)))
    result=[]
    for i in range(len_min):

        if a[i] == b[i] == c[i]:
            result.append(a[i])

        else:
            return ("".join(result))
            break


if __name__ == '__main__':
    assert finn_longest_common_prefix(['flower','flow','flight'])=='fl','Fail'
    assert finn_longest_common_prefix(['dog','racecar','car'])=='','Fail'


