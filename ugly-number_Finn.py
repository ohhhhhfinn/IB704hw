



def ugly_number_finn(x):

    start=1
    if abs(x) < 2147483648 :
        while start >0 :
           if x % 2 ==0 :
               x = x//2


           elif x %3 ==0:
                x=x//3



           elif x%5==0:
                x=x//5


           else:
               start=start-1

        if x !=1:
             return False
        else:
             return True
    else:
        return False

if __name__ == '__main__':
         assert ugly_number_finn(14) is False, 'Fail'
         assert ugly_number_finn(1024) is True, 'Fail'
         assert ugly_number_finn(21474836484648)is False, 'Fail'










