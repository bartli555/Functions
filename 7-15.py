def f(detector):
    licznik_ludzi = 0

    for zdzarzenie in detector:
        if zdzarzenie == '+':
            licznik_ludzi += 1
        elif zdzarzenie == '-':
            licznik_ludzi -= 1

        if licznik_ludzi >= 3:
            return True

    return False 

print(f'f("+-+++-+---") returns {f("+-+++-+---")}')
print(f'f("+-+-+-+-") returns {f("+-+-+-+-")}')
print(f'f("+-++-+--") returns {f("+-++-+--")}')
print(f'f("+-++-++-+---") returns {f("+-++-++-+---")}')           