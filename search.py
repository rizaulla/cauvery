def lsearch(l):
    key=int(input("enter the item:"))
    f=0
    for i in range(0,len(l)):
        if l[i]==key:
            f=1
            break

    if(f==1):
        print("%d is present at list :"%(key),l)
    else:
        print("%d is not present"%(key))
l=[10,55,2,18,23]
print("the list is",l)
lsearch(l)
