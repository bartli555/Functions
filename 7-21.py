def f(number1,number2,number3):
    najwieksza = max(number1, number2, number3)
    najmniejsza = min(number1, number2, number3)

    return najwieksza - najmniejsza

print(f"f(7, 4, 9) returns {f(7, 4, 9)}")
print(f"f(2, 12, 8) returns {f(2, 12, 8)}")