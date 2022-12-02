#regex program for python
import regex as re
#use of search and match
x=re.search("lay","lay is very ambitious entreprenur,lay works very hard ")
print(x)
y=re.match("lay","lay is very ambitious entreprenur,lay works very hard ")
print(y)
#with condition
if re.search("kalu","kalu is very black "):
    print("kalu is found to be black")
else:
    print("kalu not found")
#dynamically completly from user
x=input("enter name you want to search: ")
y=input("enter the sentence in which you want to search name: ")
if re.search(x,y):
    print("found")
else:
    print("not found")
