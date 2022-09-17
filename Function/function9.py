


def largest_list(l):
    x=max(l)
    return x
l=[]
len = int(input("enter the length of list"))
for i in range(len):
    y = int(input("enter the number "))
    l.append(y)
x=largest_list(l)
print(x)
