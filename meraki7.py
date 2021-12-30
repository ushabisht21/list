elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43,90,78,89]
even_number=0
odd_number=0
k=[]
j=[]
i=1
while i<len(elements):
    if elements[i]%2==0:
        k.append(elements[i])
        even_number+=1

    elif elements[i]%2!=0:
        j.append(elements[i])
        odd_number+=1
    i=i+1
print(k,"even_number")
print(j,"odd_number")   