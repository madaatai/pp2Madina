def is_palindrome(sentence):
    sentence = sentence.replace(" ", "").lower()
    palin=sentence[::-1]
    if sentence==palin:
        return True
    return False

word=str(input("Enter word:"))
print(is_palindrome(word))