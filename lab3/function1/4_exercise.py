def search_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True
def primes_print(nums):
    return list(filter(search_prime, nums))

num_amount=input("Please enter list numbers:")
num_list=list(map(int, num_amount.split()))
result=primes_print(num_list)
print("Prime numbers are:", result)