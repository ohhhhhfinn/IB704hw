



def list_duplicate_number_finn(a):
    b=[]
    for i in a:
        if i not in b :

            b.append(i)


        else:

            return(len(b)+1)





if __name__ == '__main__':
    assert list_duplicate_number_finn([1,2,3,1]) == 4, 'Fail'
    assert list_duplicate_number_finn([1,2,3,4,5,4,1,5]) == 6, 'Fail'
    assert list_duplicate_number_finn([1,2,0,0,2,0]) == 4, 'Fail'