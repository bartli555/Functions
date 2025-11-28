def f(n):
   znalezione = 0
   aktualna_liczba = 2

   while znalezione < n:
      
    jest_pierwsza = True

    for i in range(2, aktualna_liczba):
        if aktualna_liczba % i == 0:
            jest_pierwsza = False
            break
    if jest_pierwsza:
         znalezione += 1
    if znalezione == n:
       return aktualna_liczba
    
    aktualna_liczba += 1

print(f"f(1) returns {f(1)}")
print(f"f(5) returns {f(5)}")
print(f"f(10) returns {f(10)}")    