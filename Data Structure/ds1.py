#odd even list 
l1=[1,2,3,4,5,6,7,8]
l2=[1,2,3,4,5,6,7,8]
l3=[]
l4=[]
l=len(l1)
for i in range(l):
    if i%2==0:
        l3.append(l1[i])
    else:
        l4.append(l2[i])
print("l1 original ",l1)
print("l1 after ",l3)
print("l2 original ",l2)
print("l2 after",l4)