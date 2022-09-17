l1=[1,2,3,4,5,6,789,121,1,1,2,5,5,2,4,45,2,5,2,8,2225,8564,5,5,55,6,985,85,]
print("original",l1)
count=dict()
for i in l1:
    if i in count:
        count[i] += 1
    else:
        count[i]=1
x=[count]

print("count of each is",x)