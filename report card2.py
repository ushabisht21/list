marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
while i<len (marks):
    k=0
    sum=0
    while k<len(marks[i]):
        sum=sum+marks[i][k]
        k=k+1
    b=sum//len(marks[i])
    print(b)
    i=i+1