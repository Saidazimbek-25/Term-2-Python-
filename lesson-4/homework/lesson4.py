#task-1
my_dict={"apple":2,"banana":30,"kiwi":12,"pear":90}
asc_sorted=dict(sorted(my_dict.items(),key=lambda item:item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1],reverse=True))
print("Acsending order",asc_sorted)
print("Decsending order",desc_sorted)
