def palindrome(sentence, reverse_s):
    for i in sentence:
        for j in reverse_s:
            if i!=j:
                return False
            return True

sentence=str(input("Enter sentence:"))
reverse_s=''.join(reversed(sentence))
print(palindrome(sentence, reverse_s))