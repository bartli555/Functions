import zakres_liczb_7_5

numer_str = input('A number: ')
numer = int(numer_str)

x = 2 
y = 15

w_zakresie = zakres_liczb_7_5.zakres(numer, x, y)

rezultat = 'yes ' if w_zakresie else 'no'

print(f'Number {numer} in the range <{x},{y}>: {rezultat}')