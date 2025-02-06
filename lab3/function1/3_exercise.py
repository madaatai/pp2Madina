def solve(heads, legs):
    for chicken in range(heads+1):
        rabbits=heads-chicken
        if 2*chicken + 4*rabbits == legs:
            return chicken, rabbits
    return "No solution"
head=35
leg=94
result=solve(head, leg)
print("The amount of chickens and rabbits:", result)