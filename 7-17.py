def f(palindrome):

    odwrocony_palindrome = palindrome[::-1]

    return palindrome == odwrocony_palindrome

print(f'f("radar") returns {f("radar")}')
print(f'f("12-11-21") returns {f("12-11-21")}')
print(f'f("book") returns {f("book")}')