def find007(nums):
    goal=[]
    for i in nums:
        if i==0 or i==7:
            goal.append(i)
    
    flag=True
    for i in range(len(goal)-2):
        if goal[i]==goal[i+1] and goal[i]==0 and goal[i+2]==7:
            flag=True
        else:
            flag=False
    if(flag==True):
        return True
    else:
        return False
    
print(find007([1,2,4,0,0,7,5]))
print(find007([1,0,2,4,0,5,7]))
print(find007([1,7,2,0,4,5,0]))
print(find007([1,3,4,5,8,3,0,1,2,0,7]))