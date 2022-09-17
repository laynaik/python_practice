#function with variable length 
def fun1(*var):
    for i in var:
        print(i)
fun1(100,200,300)