import pandas as pd

#pokemon = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\pokemon.csv",squeeze=True,usecols=["Pokemon"])
#print(pokemon.head(10))
#print(pokemon.values)
#print(pokemon.is_unique)

#print(pokemon.sort_values().head())
#print(pokemon.sort_index().head())

pokemon = pd.read_csv(r"C:\Users\Rising IT\PycharmProjects\pokemon.csv",index_col="Pokemon",squeeze=True)
#print(pokemon[10])
#print(pokemon[[100,134]])

print(pokemon["Pikachu"])
print(pokemon.get("Pikachu"))
print(pokemon.get("Pikachjju", default="Not Pokemon"))

print(pokemon.value_counts())


