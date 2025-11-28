def f(n):

    lista_numerow = [str(i) for i in range(1, n + 1)]
    wynik = ''.join(lista_numerow)
    return wynik

print(f'f(11) returns "{f(15)}"')
print(f'f(4) returns "{f(4)}"')