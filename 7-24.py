def f(expression):
    wynik = int(expression[0])

    for i in range(1, len(expression), 2):
        operator = expression[i]
        liczba_za_operatorem = int(expression[i+1])

        if operator == '+':
            wynik += liczba_za_operatorem
        elif operator == '-':
            wynik -= liczba_za_operatorem    
    return wynik

print(f'f("2+3") returns {f("2+3")}')             # Oczekiwane: 5
print(f'f("3+8+1") returns {f("3+8+1")}')         # Oczekiwane: 12
print(f'f("2+3-4+5-0") returns {f("2+3-4+5-0")}') # Oczekiwane: 6

