def factorial(n):
    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

# n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    
n = 5
wynik = factorial(n)

print(f"Silnia z {n} wynosi: {wynik}")