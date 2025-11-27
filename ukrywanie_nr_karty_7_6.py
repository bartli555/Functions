def hide(card_number):
    if len(card_number) <= 6:
        return card_number
    
    prefix = card_number[:2]
    suffix = card_number[-4:]

    gwiazdki_liczik = len(card_number) - 6
    gwiazdki = '*' * gwiazdki_liczik

    return f"{prefix}{gwiazdki}{suffix}"