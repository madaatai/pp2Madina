def unique_list(lol_list):
    res=[]
    for i in lol_list:
        if lol_list.count(i)==1:
            res.append(lol_list[i])
    return res
num=int(input("Amount of elements:"))
list_lol=[]
for i in range(num):
    element=int(input())
    list_lol.append(element)
print("Unique elements:", unique_list(list_lol))