def count_letters(sentence):
    upp=0
    low=0
    for i in sentence:
        if i>="A" and i<="Z":
            upp+=1
        else:
            low+=1
    print(f"Summ of upper case:{upp}")
    print(f"Summ of lower case:{low}")

sentence=str(input("Enter sentence:"))
count_letters(sentence)