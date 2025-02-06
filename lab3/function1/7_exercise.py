def has33(num):
    for i in range(len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False

print(has33([1, 3, 3]))
print(has33([1, 3, 1, 3]))
print(has33([3,1,3]))