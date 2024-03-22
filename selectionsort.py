def selectionsort(li):
    for i in range(5):
        minposition=i
        for j in range(i,6):
            if li[j]<li[minposition]:
                minposition=j
        temp=li[i]
        li[i]=li[minposition]
        li[minposition]=temp

        print(li)

li=list(map(int,input().split()))
selectionsort(li)
print(li)
