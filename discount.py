from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-11-08
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-11-08 08:46:37.852865
print(type(time))  # <class 'datetime.datetime'>

# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomm = today + timedelta(days=1)
print(tomm)  # 2023-11-09

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime('%d/%m/%Y')
print(formated_date)  # 08/11/2023
print(datetime.now().timestamp())  # 1699430165.796852 od 1 stycznia 1970
timestamp = datetime.now().timestamp()
print(datetime.fromtimestamp(timestamp))  # 1699430165.796852 = 2023-11-08 08:58:32.984775

print(timestamp)

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 09:00
print(formated_time.removeprefix("0"))  # 9:01
# 09:47 AM
formated_time2 = datetime.now().strftime("%H:%M %b")
print(formated_time2)
formated_time3 = datetime.now().strftime("%I:%M %p")
print(formated_time3)  # 09:05 AM

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': today, 'price': 80.0},
    {'sku': 3, 'exp_date': tomm, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 150},
]

print(products)
for product in products:
    # print(product)
    # if product['exp_date'] == today:
    #     product['price'] *= 0.8
    #     print(f"""
    #     Price for {product['sku']}
    #     is now {product['price']}""")
    # ctrl / - komentarz zaznaczonych linii
    if product['exp_date'] != today:
        continue  # konczy biezącą iteracje pętli,wraca na poczatek petli, pobiera kolejny elemnt
    product['price'] *= 0.8
    print(f"""
    Price for {product['sku']}
    is now {product['price']}""")
    # Price for 1
    # is now 80.0
    #
    # Price for 2
    # is now 64.0
    #
    # Price for 4
    # is now 120.0
