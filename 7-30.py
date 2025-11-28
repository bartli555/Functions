def sum_natural(n):
    if n <= 1:
        return n
    
    return n + sum_natural(n - 1)

n = 10
wynik = sum_natural(n)

print(f"Suma liczb naturalnych z zakresu <1, {n}> wynosi: {wynik}")