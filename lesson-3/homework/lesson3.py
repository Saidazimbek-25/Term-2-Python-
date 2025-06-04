#task-1
a=['banana','pear','pineapple','grapes','wildberry']
print(a[0]) 
print(a[1]) 
print(a[2]) 
print(a[3]) 
print(a[4]) 
#task-2
list1=[1,2,3,4]
list2=[5,6,7]
result=list1+list2
print(result)
#task-3
a=[10,23,34,45,56,65]
first=a[0]
middle=a[len(a)//2]
last=a[-1]
print(first,middle,last)
#task-4

a=["Schindler's List","Inception","The Godfather Part II","The Godfather","Warcraft"]
mytuple=tuple(a)
print('tupled version:',mytuple)
#second way
tup=(*a,)
print('tuple:',tup)

#task-5
cities=['London','Kiyev','Moscow','Tashkent','Paris','Istanbul','Abu-Dhabi']
if 'Paris' in cities:
    print('Paris in the list🗼')
else:
    print('Paris is not in the list')

#task-6
a=[23,45,54,87,98,89,90]
#first way
b=a.copy()+a.copy()
#second way
c=a*2
#third way
d=a[:]+a[:]

print(b,c,d)
#task-7
a=[23,78,90,89,67]
a[0],a[-1]=a[-1],a[0]
print("List after swapping first and last elements:",a)
#task-8
tup=(1,2,3,4,5,6,7,8,9,10)
slice1=tup[3:7]
print(slice1)
#task-9
colors= [
    "red", "blue", "green", "yellow",
    "blue", "purple", "red", "orange",
    "pink", "green", "black", "white",
    "blue", "gray", "red"
]
print(colors.count('red'))
#task-10
animals = ["tiger", "leopard", "cheetah", "elephant",
    "giraffe", "zebra", "rhino", "lion","hippopotamus", "buffalo",
    "bear", "wolf", "hyena", "gorilla", "panther",
    "jaguar", "crocodile", "alligator", "antelope", "wild boar"
]
print(animals.index("lion"))
#task-11
a=(34,45,56,67,78,87)
b=(67,98,78,90,99,18,56)
merged=a+b
print(merged)
#task-12
list=[34,45,56,67,78,87]
tuple=(67,98,78,90,99,18,56)

print('list length:',len(list))
print('Tuple length:',len(tuple))

#task-13
a=(12,34,45,56,67,78)
b=list(a)
print(b)
#task-14
a=(12,4,34,45,789,56,67,78)

print('maxium number:',max(a))
print('minium number:',min(a))
#task-15
a=(12,4,34,45,789,56,67,78)
rev=a[::-1]
print(rev)
