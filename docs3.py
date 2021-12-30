a =  [1, 2, 2, 5, 8, 4, 4, 8]
i=0
count=[]
while i<len(a):
    l=a[i] 
    count.append(l)
    i=i+1
count.remove(2)
count.remove(4)
count.remove(8)
print(i,len(count))











