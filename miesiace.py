def month(n):
    nazwy_miesiecy = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

    if 1 <= n <= 12:
        return nazwy_miesiecy[n - 1]