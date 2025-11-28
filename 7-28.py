def f(dice):
    maksymalna_seria = 0
    zwycieska_cyfra = int(dice[0])

    aktualna_seria = 1

    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            aktualna_seria += 1
        else:
            if aktualna_seria > maksymalna_seria:
                maksymalna_seria = aktualna_seria
                zwycieska_cyfra = int(dice[i-1])

                aktualna_seria = 1    

    if aktualna_seria > maksymalna_seria:
        zwycieska_cyfra = int(dice[-1])            

    return zwycieska_cyfra

print(f'f("5233165554211") returns {f("5233165554211")}') # Oczekiwane: 5
print(f'f("2133") returns {f("2133")}')                   # Oczekiwane: 3