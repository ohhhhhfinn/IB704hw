
num=[]
for x in range(10):
        a=2**x
        num.append(a)
        for y in range(10):
            b=3**y

            num.append(a*b)
            num.append(b)

            for z in range(10):
                c=5**z
                num.append(a*b*c)
                num.append(a*c)
                num.append(b*c)
a=list(set(num))
a.sort()

if __name__ == '__main__':
    assert a[0] == 1 , 'Fail'
    assert a[4] == 5, 'Fail'
    assert a[9] == 12, 'Fail'
    assert a[12] == 18, 'Fail'
    assert a[51] == 256, 'Fail'
