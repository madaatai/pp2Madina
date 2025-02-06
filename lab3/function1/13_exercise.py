from random import randint
def number_guess():
    print("Hello! What is your name?")
    name=input("Name:")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    main_num=randint(1,20)
    attempts=0
    while True:
        your_num=int(input("Take a guess:"))
        attempts+=1
        if your_num>main_num:
            print("Your guess is too high. Take a guess.")
        if your_num<main_num:
            print("Your guess is too low. Take a guess.")
        if your_num==main_num:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            return 0

number_guess()