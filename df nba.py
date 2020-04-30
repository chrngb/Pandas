import pandas as pd

nba = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\nba.csv",squeeze=True).dropna(how="all")

#nba.insert(3, column="Sport", value="Basketball")

#print(nba.dropna(subset=["Salary"]).head)

#print(nba.fillna(0))

#nba.sort_values("Age","Name")
#print(nba)

#print(nba.info())

#print(nba.get_dtype_counts())

nba["Salary"] = nba["Salary"].fillna(0).astype(int)

#print(nba["Salary"].rank(ascending=True).astype("int"))
nba["SalaryRank"] = nba["Salary"].rank(ascending=False).astype("int")

print(nba.sort_values("SalaryRank"))




