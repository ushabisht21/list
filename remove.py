k=[5, 6, [], 3, [], [], 9]
i=0
a=[]
while i<len(k):
    a.append(k[i])
    i=i+1
a.remove([])
a.remove([])
a.remove([])
print(a)
   