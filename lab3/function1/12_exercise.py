def histogram(numbers):
    for num in numbers:
        print("*"*num)

num=input("Amount:")
nums=list(map(int, num.split()))
histogram(nums)