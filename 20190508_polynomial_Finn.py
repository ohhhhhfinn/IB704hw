


a=[[2,1000],[4,3],[4,2],[1,0]]
b=[[1,4],[10,3],[3,2],[1,0]]
def polynomial(a,b):
    ans=[]
    for i in range(len(a)):
        for j in range(len(b)):
            c=a[i][0]*b[j][0]
            d=a[i][1]+b[j][1]
            ans.append([c,d])



    ans.sort(key=lambda x: (x[1]))
    print(ans)

polynomial(a,b)