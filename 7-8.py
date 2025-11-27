def f(amount_to_pay):

    piatki = amount_to_pay // 5
    reszta = amount_to_pay % 5

    dwojki = reszta // 2
    reszta = reszta %2

    zlotowki = reszta

    return piatki + dwojki + zlotowki

print(f"f(23) returns {f(23)}")
print(f"f(8) returns {f(8)}") 
print(f"f(2) returns {f(2)}")   
print(f"f(0) returns {f(0)}")