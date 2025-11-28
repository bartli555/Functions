def f(number):

    number_str = str(number)
    suma = 0

    for znak_cyfry in '0123456789':
        licznik = number_str.count(znak_cyfry)

        if licznik >1:
            suma += int(znak_cyfry) * licznik

    return suma

print(f"f(1027) returns {f(1027)}")
print(f"f(230335) returns {f(230335)}")
print(f"f(513553007) returns {f(513553007)}")        