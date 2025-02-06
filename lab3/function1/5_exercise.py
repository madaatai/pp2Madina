import itertools
def permutation_printer(word):
    word_permts=itertools.permutations(word)
    for perm in word_permts:
        print(''.join(perm))

word=input("Please enter a word:")
permutation_printer(word)