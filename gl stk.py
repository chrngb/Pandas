import pandas as pd

google = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\google_stock_price.csv", squeeze=True)

#print(google.head())

def classify_per(number):
    if number<300:
        return "OK"
    elif number >= 300 and number < 650:
        return "Satisfactory"
    else:
        return "Inredible"

#print(google.apply(classify_per).head(11))

print(google.apply(lambda sto: sto+1))


