n = [10, 11, 12, 13, 14, 17, 18, 19,2,15,9]
i=0
a=[]
b=[]
while i<len(n):
    if n[i]%2==0:
        a.append(n[i])
    else:
        b.append(n[i])
    i+=1
print("even",a)
print("odd",b)
print(n[len(n)//2])
print(n[len(n)//2])

