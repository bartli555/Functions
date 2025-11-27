def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_na_cale(n):
    return n / 2.54

def stopycale_na_cm(f, i):
    cale = (f *12) + i
    return cale * 2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'20cm = {cm_na_cale(20):.2f} cali')
    print(f'5 stóp i 10 cali = {stopycale_na_cm(5, 10):.2f}cm')
