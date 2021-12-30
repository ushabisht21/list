a=["python is very easy"]
i=0
while i<len(a):
    j=0
    count=1
    while j<len(a[i]):
        if a[i][j]==" ":
            count=count+1
        j=j+1
    i=i+1
print(count)

