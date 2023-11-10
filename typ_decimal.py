# decimal , który zachuwuje precyzje przy obliczniach
# w odróżnieniu od float jest mniej narazóny na bład zaokrąglenia

from decimal import Decimal

kwota1 = Decimal('10.25')
kwota2 = Decimal('5.50')

print(kwota1, kwota2)
suma = kwota1 + kwota2
print("Suma", suma)

a = Decimal('0.7')
b = Decimal('0.2')
print(a + b)  # 0.9

precyzja = Decimal('0.00')

podatek = Decimal('0.23')
kwota_z_podatkiem = kwota1 * (1 + podatek)
print("Kwota z podatkiem:", kwota_z_podatkiem)
print("Kwota z podatkiem:", kwota_z_podatkiem.quantize(precyzja))
# 10.25 5.50
# Suma 15.75
# 0.9
# Kwota z podatkiem: 12.6075
# Kwota z podatkiem: 12.61
