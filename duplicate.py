a=[2,3,4,5,6,6,7]
i=0
k=[]
while i<len(a):
  if a[i] not in k:
    k.append(a[i])
  i=i+1
print(k)