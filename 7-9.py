def f(number, even):
    
    #Jeśli even == True, sumuje cyfry parzyste.
    #Jeśli even == False, sumuje cyfry nieparzyste.

    number_str = str(number)
    suma = 0

    for char in number_str:
        if not char.isdigit():           
            continue

        cyfra = int(char)  
        cyfra_parzysta = (cyfra %2 == 0)  

        if cyfra_parzysta == even:
            suma += cyfra

    return suma

print(f"f(3124, True) returns {f(3124, True)}") 
print(f"f(3124, False) returns {f(3124, False)}")
print(f"f(20576, False) returns {f(20576, False)}")
print(f"f(20576, True) returns {f(20576, True)}")
print(f"f(13115, True) returns {f(13115, True)}")  