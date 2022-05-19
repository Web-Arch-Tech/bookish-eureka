# print(numbers[1])
# numbers[1] = 44

from ast import arg
import this
import os


numbers = tuple((3, 44, 32))  # tuple constructor


def kasuhik_function(name, age):
    tuple1 = tuple((name, age))
    print(tuple1)


for each in numbers:
    if 3 in numbers:
        print(each)
        kasuhik_function("kasuhik", 20)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
for i in range(len(fruits)):
    print(i)


def anika_function(this):
    this.surname = this
    this.country = this


i = 0
while i in range(len(fruits)):
    print(fruits[i])
    i += 1
    # anika_function():
    # surname, country
schools = tuple(("KV1", "KV RAJ", "KV lal", "KV VJA", "KV WEL", "KV APS"))
tuple3 = fruits * 2
print(tuple3)


set1 = set({"love", "hate", "greed"})
set1.add("lust")
feelings = set({"hurt", "loved", "horny"})
set1.update(feelings)
print(set1)
for x in set1:
    print(x)
    print("love" in set1)


set1.remove("lust")
set1.discard("greed")
print(set1)

set1.pop()
print(set1)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["year"])

x = thisdict["brand"]
print(x)
y = thisdict.get("year")
print(y)
z = thisdict.keys()
print(z)

thisdict["color"] = "green"
print(thisdict)


e = thisdict.values()
print(e)

o = thisdict.items()
print(o)

thisdict.update({"owner": "idkbro"})
print(o)

thisdict.pop("owner")
print(o)

thisdict.popitem()
print(o)

for f in thisdict:
    print(f)

for j in thisdict:
    print(thisdict[j])

for g in thisdict.values():
    print(g)

for t in thisdict.keys():
    print(t)

for m, p in thisdict.items():
    print(m, p)

jey = thisdict.copy()
thisdict.update({"owner": "idkbro"})
print(jey)
print(thisdict)


a = 54
b = 76
if a < b:
    pass
print("A") if a > b else print("=") if a == b else print("B")

for h in "kaushiknusrat":
    print(h)
    if h == "i":
        break


def my_onlymine(*args):
    print("my name is " + args[0] + " and i am" +
          args[1] + "years old" + args[2])


my_onlymine("Kaushik", "20", "bye")


def my_second(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)


my_second(arg1="Kaushik", arg2="babw", arg3="lego")


def my_third(**kwargs):
    print(kwargs["slaac"] + kwargs["ega"] + kwargs["asdfghj"])


my_third(slaac="hey", ega="dude", asdfghj="how are ya?")

f = open("babe.txt", "rt")
print(f.read(5))

for c in f:
    print(c)


f.close()

# x = open("some.txt", "w")
# x.write("HIHIHIHIIHIHIHIHIHI")
# x.close()

# x.open("some.txt", "r")
# print(x.read())

# os.remove("myfile.txt")


def my_greyarea(area="square"):
    print("area of shape:" + area)


my_greyarea()


def my_hunc(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_hunc(fruits)


def insta_gram(x):
    return 5 * x


print(insta_gram(90))


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myjub(self):
        print("mu nadjhcdskk" + self.name)   

p1 = Person("Kaushik", 20)
p1.myjub()
print(p1.name)
print(p1.age)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


class Lwtter:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname


    def printname(self):
        print(self.firstname, self.lastname)


x = Lwtter("Kaushik", "Chintam")
x.printname()            


class Name(Lwtter):
    pass

y = Name("shdsjdm","djksjdkdj")
y.printname()
