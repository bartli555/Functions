def time_string(hours, minutes, time_format):

    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        am_pm = 'AM' if hours < 12 else 'PM'

        hours_12 = hours

        if hours == 0:
            hours_12 = 12 #północ 00:00 czyli 12am
        elif hours > 12:
            hours_12 = hours - 12 # np. 13:00 to 1pm, a gdy jest 12:00 to zostaje 12pm
        return f'{hours_12}:{minutes:02}{am_pm}'

przyklady = [
    (15, 38, '24'),
    (8, 3, '24'),
    (0, 5, '24'),
    (11, 15, '12'),
    (0, 7, '12'),
    (7, 30, '12'),
    (12, 46, '12'),
    (13, 10, '12'),
    (19, 2, '12')
]    

for h,m ,tf in przyklady:
    wynik = time_string(h,m,tf)
    print(f"time_string({h}, {m}, '{tf}') zwraca '{wynik}'")