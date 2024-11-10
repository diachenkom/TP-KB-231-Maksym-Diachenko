import requests 

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")
currency_all = ["EUR", "USD", "PLN"]

for elem in response.json():
    if elem['cc'] in currency_all:
        print(elem['cc'], "  ", elem['rate'])

while True:
    currency = input("Уведіть тип валюти (EUR, USD, PLN):") 
    currency = currency.upper()
    if currency not in currency_all:
        print("Неправильно введений тип валюти. Уведіть EUR, USD або PLN: ")
        continue
    else: 
        break

while True:
    amount = input("Уведіть кількість валюти:")
    try:
        amount=float(amount)
        if amount <= 0:
            print("Неправильне значення. Уведіть ненульове додатне число")
            continue
        else:
            break
    except ValueError:
        print("Неправильне значення. Уведіть додатне число")
        continue

for elem in response.json():
    if elem['cc'] == currency:
        sum = elem['rate'] * amount
        print(f"Сума в гривнях згідно курсу вказаної вами валюти: {sum:10.2f}")