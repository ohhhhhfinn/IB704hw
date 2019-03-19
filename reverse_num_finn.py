
def finn(number):
    number=str(number)
    list1=list(number)
    if list1[0] == "-":
            list1=list1[1::]
            list1.reverse()
            return(int("-"+("".join(list1))))
    else:

            list1.reverse()
            return(int("".join(list1)))

if __name__ == '__main__':
    assert finn(123) == 321, 'Fail'
    assert finn(-123) == -321, 'Fail'
    assert finn(120) == 21, 'Fail'
    assert finn(1534236469) != 0, 'Fail'
