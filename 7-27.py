def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    d1 = int(product_code[0])
    d2 = int(product_code[1])
    d3 = int(product_code[2])
    
    suma_trzech = d1 + d2 + d3

    oczekiwana_kontrola = suma_trzech % 7

    rzeczywista_kontrola = int(product_code[3])

    return oczekiwana_kontrola == rzeczywista_kontrola

print(f'f("1082") returns {f("1082")}') # Oczekiwane: True (1+0+8=9, 9%7=2. Ostatnia to 2. OK)
print(f'f("2035") returns {f("2035")}') # Oczekiwane: True (2+0+3=5, 5%7=5. Ostatnia to 5. OK)
print(f'f("1114") returns {f("1114")}') # Oczekiwane: False (1+1+1=3, 3%7=3. Ostatnia to 4. ŹLE)
print(f'f("7071") returns {f("7071")}')