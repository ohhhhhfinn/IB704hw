


def climbing_stairs(num):
    stage1=1
    stage2=2
    if num  == 1 :
        return stage1
    elif num ==2:
        return stage2
    elif num  >0 :
        for i in range(2,num):

            stage = stage1 + stage2
            stage1=stage2
            stage2=stage





            num-=num

        return  stage


if __name__ == '__main__':
    assert climbing_stairs(1) == 1 , 'Fail'
    assert climbing_stairs(2) == 2 , 'Fail'
    assert climbing_stairs(3) == 3 , 'Fail'
    assert climbing_stairs(4) == 5 , 'Fail'
    assert climbing_stairs(5) == 8 , 'Fail'
    assert climbing_stairs(6) == 13 , 'Fail'
    assert climbing_stairs(45) == 1836311903 , 'Fail'




