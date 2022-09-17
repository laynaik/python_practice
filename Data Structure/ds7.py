#intersection between elements 
fs={23,42,65,57,78,83,29}
ls={57,83,29,67,73,43,48}
print(ls)
print(fs)
x=fs.intersection(ls)
for i in x:
    fs.remove(i)
    ls.remove(i)
print(ls)
print(fs)