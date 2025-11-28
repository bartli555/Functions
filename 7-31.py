def power(x, n):
    if n == 0:
        return 1
    
    return x * power(x, n - 1)

podstawa = 5
wykladnik = 3

wynik = power(podstawa, wykladnik)

print(f"{podstawa} do potęgi {wykladnik} wynosi: {wynik}")