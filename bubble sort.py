list=[8,4, 7, 5, 3, 9, 6, 2, 1]
print(list) 
i=0
while i<len(list):
    j=0
    while j<i:
        if list[i]>list[j]:
            p=list[i]
            list[i]=list[j]
            list[j]=p
        j=j+1
    i=i+1
print(list)