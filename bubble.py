def bsort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if l[i]>l[j+1]:
                t=l[j]
                l[j]=l[j+1]
                l[j+1]=t

    return
l=[52,12,36,55,84]
bsort(l)
print("sorted list is ")
for i in range(len(l)):
    print("%d"%l[i],end=" ")
