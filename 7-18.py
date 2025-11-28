def f(sentence):
    return sentence.replace(" ", "")

sentence1 = "integrated development environment"
print(f'f("{sentence1}") returns "{f(sentence1)}"')

sentence2 = "A programming language is a system of notation for writing computer programs"
print(f'f("{sentence2}") returns "{f(sentence2)}"')