def reverse_word(sentence):
    sentence=list(sentence.split())
    sentence.reverse()
    for i in sentence:
        print(i, end=" ")

sentence=str(input("Enter a sentence:"))
reverse_word(sentence)