def f(n):
    if n <= 0:
        return ""
    
    gwiazki = ["*"] * n 
    wynik = "/".join(gwiazki)

    return wynik

print(f'f(4) returns "{f(8)}"')
print(f'f(1) returns "{f(1)}"')