def rec(n):
    if n:
         
        return n + rec(n-1)
    else:
        return 0
x=int(input("sum of the number "))
y=rec(x)
print(x)
print(y)