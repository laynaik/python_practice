def calc(a,b):
    def add(a,b):
        x=a+b
        return x
    y=add(a,b)
    z=y+5
    return z
x=calc(2,3)
print(x)