#subset
fs={23,42,65,57,78,83,29}
ss={57,83,29,67,73,43,48,23,42,65,57,78,83,29}
x=fs.issubset(ss)
if x==True:
    fs.clear()
y=ss.issubset(fs)
if y==True:
    ss.clear
print(x)
print(y)
print(ss)
print(fs)
