import pandas as pd
rev = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\revenue.csv", index_col="Date")

#print(rev.head())

#print(rev.sum(axis="columns"))

nba = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\nba.csv",squeeze=True)
#print(nba.Team)

Select = ["Team","Name","Weight"]

print(nba[Select])


