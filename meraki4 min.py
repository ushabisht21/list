a=[2,3,4,5,6,7,8]
print(a)
minval=min(a)
print("min value in the list is :",minval)
a.remove(minval)
simin=min(a)
print("second min value in the list =",simin)





a=[1,2,3,4,5,6]
i=0
min_value=a[i]
while i<len(a):
    if a[i]<min_value:
        min_value=a[i]
    i=i+1
print(min_value) 
