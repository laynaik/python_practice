def even_list(s,e):
    l=[]
    if e>s:
        for i in range(s,e):
            if i%2==0:
                l.append(i)
    return l
l=int(input("start no"))
m=int(input("end no "))
x=even_list(l,m)
print(x)