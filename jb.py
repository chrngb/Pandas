import pandas as pd

bond = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\jamesbond.csv",index_col="Film")
#bond.set_index("Film", inplace=True)
#bond.reset_index(drop=True,inplace=True)
#bond.sort_index(inplace=True)
#print(bond.loc["C":"L"])
#print("Gold Bond" in bond.index)
#print(bond.iloc[0:10:2])
print(bond.ix["GoldenEye"])

#print(bond.head())






