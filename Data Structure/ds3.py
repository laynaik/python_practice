l1=[11,45,8,23,14,12,78,45,89]

l2=l1[:3]

l3=l1[3:6]

l4=l1[6:]

print("original",l1)
print("first",l2)
print("first reversed",list(reversed(l2)))
print("second",l3)
print("second reversed",list(reversed(l3)))
print("third",l4)
print("third reversed",list(reversed(l4)))