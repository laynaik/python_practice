#every no in list to its square 
list=[]
l=int(input("eneter the no of elements in list "))
for i in range(l):
    x=int(input("eneter the no in list "))
    list.append(x)
fl=[]
for i in list:
    z=i**2
    fl.append(z)
print(list)
print(fl)


    