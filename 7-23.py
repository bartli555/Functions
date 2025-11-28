def f(password):
    if len(password) < 6:
        return False
    
    if len(set(password)) != len(password):
        return False
    
    return True

print(f'f("ax15") returns {f("ax15")}')
print(f'f("book123") returns {f("book123")}')   
print(f'f("A2water3") returns {f("A2water3")}') 
print(f'f("qwerty") returns {f("qwerty")}')    
print(f'f("") returns {f("")}')