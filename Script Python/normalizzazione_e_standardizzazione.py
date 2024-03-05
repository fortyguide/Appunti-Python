import pandas as pd

# Una funzione interessante di Pandas è quella che permette di caricare un dataset
# anche da un URL remoto. È possibile anche scegliere quali colonne utilizzare e
# assegnare dei nomi alle colonne scelte.
wines = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                    usecols=[0,1,7],
                    names=['classe','alcol','flavonoidi'])

print("Stampo alcuni valori del dataset wine: ")
print(wines.head(10))
print()

# Effettuo la normalizzazione del dataset
wines_norm = wines.copy()
features = ["alcol","flavonoidi"]
to_norm = wines[features]
wines_norm[features] = (to_norm - to_norm.min())/(to_norm.max() - to_norm.min())
print("Stampo alcuni valori del dataset wine normalizzato: ")
print(wines_norm.head(10))
print()

# Effettuo la standardizzazione del dataset
wines_std = wines.copy()
to_std = wines[features]
wines_std[features] = (to_std - to_std.mean())/to_std.std()
print("Stampo alcuni valori del dataset wine standardizzato: ")
print(wines_std.head(10))
print()
