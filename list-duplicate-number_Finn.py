



def list_duplicate_number_finn(a):
    b=[]
    for i in a:
        if i not in b :

            b.append(i)


        else:

            return(len(b)-a.index(i)-1)





if __name__ == '__main__':
    assert list_duplicate_number_finn([1,2,3,1]) == 2, 'Fail'
    assert list_duplicate_number_finn([1,2,3,4,5,2]) == 3, 'Fail'
    assert list_duplicate_number_finn([1,2,3,1,5]) == 2, 'Fail'
    assert list_duplicate_number_finn([1, 2, 3, 1,2, 5]) == 2, 'Fail'
