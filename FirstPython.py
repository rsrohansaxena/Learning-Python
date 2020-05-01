"""
a="   Hello,World  "
print (a.strip())#IP-"   Hello,World  ", OP -Hello,World
print(a.split(","))#OP - ['   Hello', 'World  ']

txt="Nayan"
x="ya" in txt
print (x)

x=5
if(x==3):
    print("T1")
elif(x==5):
    print("T2")
else:
    print("T3")

mylist=["A","B",3] #List[]
mylist1=mylist.copy()

mylist.append("Z")
mylist.insert(1,"Z")
del mylist[2]

for x in mylist1:
    print(x)
print("@@@@@@@@@@")
for x in mylist:
    print(x)

mytuple=("A","B",3) #Tuple()
mytuple1=list(mytuple).copy()

mytuple1.append("Z")
#mytuple.insert(1,"Z")
#del mytuple[2]
mytuple1=tuple(mytuple1)
#mytuple1.append("Z")

for x in mytuple1:
    print(x)
print("@@@@@@@@@@")
for x in mytuple:
    print(x)"""

myset={"A","B",3,3} #Set{}
myset1={"F","B"}
#myset2=myset.union(myset1)

myset2=myset+myset1
myset.add("Nayan")
myset.update(["Roh","Sax"])

myset.remove("A")
myset.discard("N")

myset

for x in myset2:
    print(x)
