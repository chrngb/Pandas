import pandas as pd

df = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\employees.csv", parse_dates=["Start Date","Last Login Time"])

#df["Start Date"] = pd.to_datetime(df["Start Date"])
#df["Last Login Time"]= pd.to_datetime(df["Last Login Time"])
df["Senior Management"]=df["Senior Management"].astype(bool)
df["Gender"] = df["Gender"].astype("category")

df.sort_values("First Name",inplace=True)

#print(df.head())
#print(df[df["Gender"] == "Male"].head)

mask1 = df["Gender"] == "Male"
mask2 = df["Team"] == "Marketing"
#print(df[mask1 & mask2].head())

#print(df[df["Team"].isin(["Sales","Product","Finance"])])

condition = df["Team"].notnull()
#print(df[condition])
#print(df[df["Salary"].between(60000, 70000)])

#print(df[~df["First Name"].duplicated(keep='last')].head())

print(df.drop_duplicates(subset=["First Name", "Team"], keep="last").head())
