
a=[1,2,3,4,5,6]
i=0
max_value=0
while i<len(a):
    n=a[i]
    if n>max_value:
        max_value=n
    i=i+1
print(max_value) 





num=[50,30,40,30,60]
i=num[0]
a=0
while a<len(num):
    if num [a]>i:
        i=num[a]
    a=a+1
print(i)        
b=i



a=[23,342,56,78,340,67,89,98,43]
print(a)
k=max(a)
print("max value in the list:",k)
a.remove(k)
b=max(a)
print(" second max value in the list:",b)
a.remove(b)
s=max(a)
print("thard max value in the list:",s)