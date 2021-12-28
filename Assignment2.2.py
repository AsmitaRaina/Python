#1)
x=(1,2,3)
x=list(x)
x[0]=5
x=tuple(x)
print(x)

#2)
""" String methods """
a="Hello"
print(a)
print(a[0])
for i in a:
    print(i,end="")
print("\n")
print(len(a))
if "e" in a:
    print("Yes e in a")
print(a[0:2])
print(a[-5:-2])
print(a.upper())
print(a.lower())
a=" Hello "
print(a.strip())
a="Hello"
print(a.replace("H","J"))
print(a.split())
print("a"+"n")
age="Name"
txt="my name is {}"
print(txt.format(age))
name="Name"
age=18
txt="My name is {} and age {}"
print(txt.format(name,age))
print(a.capitalize())
m="text"
s=""
print(s.join(m))
print(a.startswith("h"))
print(a.endswith("o"))

#3)
""" Dictionary Methods """
dict={1:"name", 2:"Age", 3:"Place", 4:"Profession"}
dict.clear()
print(dict)
dict={1:"name", 2:"Age", 3:"Place", 4:"Profession"}
print(dict.get(1))
dict={1:"name", 2:"Age", 3:"Place", 4:"Profession"}
print(dict.pop(1))
dict={1:"name", 2:"Age", 3:"Place", 4:"Profession"}
print(dict.setdefault(3))
print(dict.values())

# Create a dictionary with a number as the key and list, dictionary as a value
d1={1:[1,2,3]}
d2={2:{"one":"name","two":"age"}}
