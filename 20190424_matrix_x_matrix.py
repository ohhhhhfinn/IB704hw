a=[[1,2],[3,4],[1,2]]
b=[[5,6,1],[7,8,2]]
def finn(a,b):
    if len(a) == len(b[0]):
        ans = [[0 for i in range(len(a))] for j in range(len(b[0]))]

        for i in range(len(a)):

            for j in range(len(b[0])):
                for k in range(len(b)):


                    ans[i][j] += a[i][k]*b[k][j]

        print (ans)
    else:
        return False
finn([[1,2],[3,4],[1,2]],[[5,6,1],[7,8,2]])
