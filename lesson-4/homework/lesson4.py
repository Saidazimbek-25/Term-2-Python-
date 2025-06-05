#task-1
my_dict={"apple":2,"banana":30,"kiwi":12,"pear":90}
asc_sorted=dict(sorted(my_dict.items(),key=lambda item:item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1],reverse=True))
print("Acsending order",asc_sorted)
print("Decsending order",desc_sorted)
#task-2
#1st way
a={0:10,1:20}
a[2]=30
print(a)
#second way
a.update({2:30})
print(a)
#task-3
#1st way
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
#second way
dic1=dic1|dic2|dic3
print(dic1)
