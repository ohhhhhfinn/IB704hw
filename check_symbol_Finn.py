


def check(c):
    c=str(c)
    c=list(c)
    find1 = '('
    find2 = ')'
    find3 = '{'
    find4 = '}'
    find5 = '['
    find6 = ']'

    if (len(c) % 2) == 0:

        if find1 and find2 in c: #確認()
            check1 = c.index(find1) - c.index(find2)

            if (check1 % 2) == 1:
                print("True")

            else:
                print("Fail")


        elif find3 and find4 in c: #確認{}

            check2 = c.index(find3) - c.index(find4)
            if (check2 % 2) == 1:
                print("True")
            else:
                print("Fail")
        elif find4 and find5 in c: #確認[]
            check3 = c.index(find5) - c.index(find6)
            if (check3 %2) ==1:
                print("True")
        else:
                print("Fail")




    else:
            print("Fail")

  

check("()")
check("{}()")
check("({})")
check("({)}")
check("(")
check("())")
# if __name__ == '__main__':
#     assert check("()") == 'True', 'Fail'
#     assert check("{}()") == 'True', 'Fail'
#     assert check("({})") == 'True', 'Fail'
#     assert check("({)}") != 'True', 'Fail'
#     assert check("(") != 'True', 'Fail'
#     assert check("())") != 'True', 'Fail'
