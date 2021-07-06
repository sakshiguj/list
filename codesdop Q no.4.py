# n=int(input("enter the number"))
i=10
a=[]
while i>0:
  p=int(input("enter the nubmber"))
  a.append(p)
  i=i-1
n=int(input("enter the number"))
i=9
count=0
while i>=0:
  if n==a[i]:
    print("yes")
    count=count+1
  i=i-1
if count==0:
  print("No")
if n in a:
  print("Yes")
else:
  print("No")

