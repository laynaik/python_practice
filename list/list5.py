def swap(list,pos1,pos2):
    temp1=list[pos1]
    temp=list[pos2]
    list[pos1]=temp
    list[pos2]=temp1
    return list

n=int(input("enter the size of list "))
list=[]
for i in range(n):
    l=int(input("enter the {} element of list ".format(i)))
    list.append(l)
pos1=int(input("enter position 1 of swap "))
pos2=int(input("enter position 2 of swap "))
print("actual list is {}".format(list))
a=swap(list,pos1,pos2)
print("\n the swapped list is {}".format(a))