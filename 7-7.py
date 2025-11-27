def f(binary_number):

    for char in binary_number:
        if char != '0' and char != '1':
            return False
    return True

testery = ['101101', '1311a10100']

for numer in testery:
    wynik = f(numer)
    print(f'f("{numer}") returns {wynik}')