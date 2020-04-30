import pandas as pd

Rate = [3.99,4.54,6.52,5.55,7.91]

r = pd.Series(Rate)

#print(r)
print(r.sum())
print(r.product())
print(r.mean())

fruits = ["Apple","Mango","Watermelon","Pineapple","Grape"]
weekdays=["Mon","Tue","Wed","Thru","Fri"]

print(pd.Series(fruits,weekdays))



