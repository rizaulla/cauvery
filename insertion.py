def insertionsort(l):
    for i in range(len(l)):
        key=l[i]
        j=i-1
        while j>0 and key<l[j]:
            l[j+1]=l[j]
            j=1
        l[j+1]=key
l=[85,44,10,2,49]
print("list is=",l)
insertionsort(l)

print("The sorted list is")
for i in range (len(l)):
    print(l[i])
