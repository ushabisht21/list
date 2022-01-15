k=[]
i=100
while i<=400:
    s=str(i)
    if (int (s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        k.append(s)
    i=i+1
print("even number",k)