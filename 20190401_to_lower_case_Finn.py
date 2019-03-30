
def finnlower(STR):
    dic={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}

    list1=list(STR)
    list2=[]
    for i in range(len(STR)):
        if list1[i] in dic:
            list2.append(dic[list1[i]])
        else:
            list2.append(list1[i])
    return ("".join(list2))




if __name__ == '__main__':
    assert finnlower('SDFSEFSDFSF')=='sdfsefsdfsf' ,'Fail'
    assert finnlower('aaaaAAAAAAAaAAa') == 'aaaaaaaaaaaaaaa', 'Fail'
    assert finnlower('xxxXXXXooooOOOO') == 'xxxxxxxoooooooo', 'Fail'
