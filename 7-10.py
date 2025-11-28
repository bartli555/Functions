def f(x,y):
    licznik = 0

    for i in range(x, y +1):
        if i < 0 and i % 2 ==0:
            licznik += 1
    return licznik

print(f"f(-7, 8) returns {f(-100, 8)}")
print(f"f(-1, 11) returns {f(-1, 11)}")       