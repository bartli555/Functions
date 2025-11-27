import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'233cm = {converters.cm_to_m(233)}m')
print(f'10cm = {converters.cm_na_cale(10):.2f} cali')
print(f'4 stopy i 5 cali = {converters.stopycale_na_cm(4, 5):.2f}cm')