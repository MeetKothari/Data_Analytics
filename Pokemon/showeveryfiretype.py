import pandas as pd

pokemon = pd.read_csv('pokemon_data.csv')

# print(pokemon.head()) # get an idea of what data we're working with

# print("\n") # formatting
# print(pokemon.columns) # find out what overall headings we're working with

# print(pokemon['Name']) # return a truncuated list of every Pokemon

print(pokemon.loc[pokemon['Type 1'] == "Fire"])
