def all_ele_true(tupleee):
    return all(tupleee)
value=input("Enter tuple's elements:")
list_for_tup=[]
for i in value:
    if i.isdigit():
        list_for_tup.append(int(i))
    elif i.replace(',',' ',1).isdigit():
        list_for_tup.append(float(i))
    else:
        list_for_tup.append(i)

tupp=tuple(list_for_tup)
print(all_ele_true(tupp))