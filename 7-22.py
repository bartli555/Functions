def f(name):
    slowa = name.split()

    pierwsza_litera = [slowo[0] for slowo in slowa]

    return "".join(pierwsza_litera)

print(f'f("Internet of Things") returns "{f("Internet of Things")}"')
print(f'f("For Your Information") returns "{f("For Your Information")}"')
print(f'f("Python") returns "{f("Python")}"')