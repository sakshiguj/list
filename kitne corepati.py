paisa = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
corepati=0
lakhpati=0
dilwale=0
while i<len(paisa):
    if paisa[i]>=10000000:
        print("corepati=",paisa[i])
    elif paisa[i]>=100000:
        print("lakhpati=",paisa[i])
    else:
        print("dilwale=",paisa[i])
    i=i+1

