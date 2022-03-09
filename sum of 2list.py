# a=[3,4,5,6,7,8,9]
# b=[2,4,7,8,9,6,7]
# i=0
# while i<len(a):
#     s=(a[i]+b[i])
#     print(s,end=" ")
#     i=i+1  


a=[2,3,4,5,6,6]
b=[4,5,6,6,7,8]
i=0
c=[]
while i<len(a):
    c.append(a[i])
    c.append(b[i])
    i+=1
print(c)

