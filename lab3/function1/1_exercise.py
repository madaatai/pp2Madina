def gram_to_ounces(gram):
    ounces = 28.3495231 * gram
    return ounces
gram = float(input("Enter your gramm:"))
ounce=gram_to_ounces(gram)
print(gram, "in ounce equal to the", ounce)