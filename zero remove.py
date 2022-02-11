a=[101,101,1011,110]
b=[]
i=0
while i< len(a):
    h=str(a[i])
    s=""
    j=0
    while j<len(h):
        if h[j] in "0":
            pass
        else:
            s+=h[j]
        j=j+1
    b.append(int(s))
    i=i+1
print(b)

