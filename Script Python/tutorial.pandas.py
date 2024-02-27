import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Carichiamo il dataset, scegliendo un formato
iris = pd.read_csv("C:\\Users\\39346\\IdeaProjects\\Appunti-Python\\data\\iris.csv")

# Visualizziamo di default le prime 5 righe del dataset mediante il metodo head() senza parametri in ingresso,
# altrimenti gli inseriamo noi come parametro il numero di righe che vogliamo visualizzare
iris_header1 = iris.head()
print("Prime 5 righe del dataset iris.csv: ")
print(iris_header1)
print()

iris_header2 = iris.head(10)
print("Prime 10 righe del dataset iris.csv: ")
print(iris_header2)
print()

# Il metodo tail() è il contrario del metodo head(), ovvero permette di visualizzare di default le ultime 5 righe
# del dataset, altrimenti anche qui possiamo scegliere quante righe visualizzare inserendo un numero come
# parametro in ingresso
iris_tail1 = iris.tail()
print("Ultime 5 righe del dataset iris.csv: ")
print(iris_tail1)
print()

iris_tail2 = iris.tail(10)
print("Ultime 10 righe del dataset iris.csv: ")
print(iris_tail2)
print()

# Se il file del dataset non ha sulla prima riga il nome delle feature, possiamo scriverle
# a codice utilizzando un array nel seguente modo
iris_no_header = pd.read_csv("C:\\Users\\39346\\IdeaProjects\\Appunti-Python\\data\\iris_noheader.csv",
                             header = None,
                             names = ["sepal_length",
                                      "sepal_width",
                                      "petal_length",
                                      "petal_width",
                                      "species"])

iris_no_header = iris_no_header.head()
print("Prime 5 righe del dataset iris_noheader.csv: ")
print(iris_no_header)
print()

# Accediamo al nome delle feature (o colonne) tramite l'attributo columns
iris_columns = iris.columns
print("Nome delle feature del dataset iris.csv: ")
print(iris_columns)
print()

# Possiamo ottenere qualche informazione in più sulle colonne tramite il metodo info()
iris.info()
print()

# Possiamo accedere ai valori di una singola colonna utilizzando la sua chiave
Y = iris['variety']
valori_colonna_variety = Y.head()
print("Primi 5 valori della colonna variety: ")
print(valori_colonna_variety)
print()

# Possiamo accedere anche ai valori di più colonne, utilizzando la loro chiave
X = iris[["sepal.length","sepal.width","petal.length","petal.width"]]
valori_colonne_multiple = X.head()
print("Primi 5 valori delle colonne sepal.length,sepal.width,petal.length,petal.width: ")
print(valori_colonne_multiple)
print()

# Possiamo accedere ai valori di più colonne anche solo dicendo quelle da escludere tramite drop().
# Il parametro axis compare in tutti quei metodi che operano per righe o colonne. Quando l'operazione del
# metodo deve essere svolta sulle righe, l'axis deve corrispondere a 1 (come in questo caso che  vogliamo
# rimuovere la colonna variety per ogni riga). Quando invece l'operazione deve essere svolta sulle
# colonne, l'axis deve corrispondere a 0
Y = iris.drop("variety", axis=1)
valori_colonne_multiple = Y.head()
print("Primi 5 valori di tutte le colonne, esclusa la colonna variety: ")
print(valori_colonne_multiple)
print()

# Per eseguire lo slicing del dataset, ovvero per selezionare solo alcune righe o alcune colonne,
# abbiamo due soluzioni diverse, ovvero quelle di usare loc[] o iloc[]. Per meglio comprendere
# la differenza tra questi due comandi, creiamo una copia del dataset tramite copy() e la
# mescoliamo tramite sample().
iris_sampled = iris.copy().sample(frac=1)
print("Valori del dataset mescolato: ")
print(iris_sampled)
print()

# Possiamo accedere alla riga con indice 3 nel dataset
print("Riga del dataset restituita da loc[3]: ")
loc_row = iris_sampled.loc[3]
print(loc_row)
print()

# Possiamo accedere alla riga che è alla posizione 4 nel dataset (la prima posizione parte da 0)
print("Riga del dataset restituita da iloc[3]: ")
iloc_row = iris_sampled.iloc[3]
print(iloc_row)
print()

# Possiamo accedere alla singola colonna sulla riga con indice 3 nel dataset
print("Valore del dataset restituita da loc[3, ""variety""]: ")
loc_row_variety = iris_sampled.loc[3, "variety"]
print(loc_row_variety)
print()

# Possiamo accedere alla singola colonna sulla riga in posizione 3 nel dataset
print("Valore del dataset restituita da iloc[3, ""variety""]: ")
iloc_row_variety = iris_sampled.iloc[3, 4]
print(iloc_row_variety)
print()

# Possiamo ottenere il numero di righe e colonne del dataset tramite shape
print("Numero di righe/colonne del dataset: ")
iris_shape = iris.shape
print(iris_shape)
print()

# Possiamo ottenere vari valori statistici del dataset tramite describe()
print("Valori statistici del dataset: ")
iris_describe = iris.describe()
print(iris_describe)
print()

# Possiamo visualizzare la classificazione di valori che avviene su una colonna del dataset tramite unique()
print("Classificazione di valori sulla colonna variety: ")
iris_variety_unique = iris['variety'].unique()
print(iris_variety_unique)
print()

# Possiamo creare dei filtri, applicando delle maschere. Ad esempio, proviamo a creare una maschera
# in grado di selezionare soltanto le osservazioni che hanno la lunghezza del petalo maggiore della
# lunghezza media
print("Prime 5 osservazioni con lunghezza del petalo > della lunghezza media: ")
long_petal_mask = iris["petal.length"] > iris["petal.length"].mean()
iris_long_petals = iris[long_petal_mask].head()
print(iris_long_petals)
print()

# Possiamo utilizzare una maschera per modificare le nostre osservazioni in base
# a delle condizioni. Ad esempio, proviamo a creare una maschera che ci permette di cambiare
# il valore della variety da Setosa a Undefined
print("Verifico se al posto di Setosa abbiamo il valore Undefined sulla colonna variety: ")
iris_copy = iris.copy()
iris_copy[ iris_copy["variety"] == "Setosa"] = "Undefined"
iris_variety_modified = iris_copy["variety"].unique()
print(iris_variety_modified)
print()

# Possiamo ordinare il dataset in base ai valori contenuti in una colonna tramite sort_values()
print("Prime 5 osservazioni ordinate per la colonna petal.length: ")
iris_sort_petal_length = iris.sort_values("petal.length").head()
print(iris_sort_petal_length)
print()

# Possiamo raggruppare le osservazioni all'interno del dataset in base a delle condizioni tramite groupby().
# Ad esempio, possiamo raggruppare tutte le osservazioni per variety e fare la media di tutte le altre colonne
print("Media di tutte le colonne raggruppate per variety: ")
grouped_variety = iris.groupby("variety")
grouped_variety_mean = grouped_variety.mean()
print(grouped_variety_mean)
print()

# Possiamo applicare delle funzioni su righe, o colonne, del dataset. Per farlo, dobbiamo utilizzare
# il metodo apply(), indicando come primo argomento il nome della funzione da applicare, che può
# essere una funzione standard, definita da noi o di una libreria esterna. Ad esempio, utilizziamo
# numpy per contare i valori differenti da 0 per riga
import numpy as np
print("Numero dei valori differenti da 0 per le prime 5 righe: ")
iris_count_nonzero = iris.apply(np.count_nonzero, axis=1).head()
print(iris_count_nonzero)
print()

# Possiamo anche applicare una funzione valore per valore tramite applymap().
# Ad esempio, proviamo ad arrotondare tutti quanti i valori all'interno del dataset
# all'intero più vicino
print("Prime 5 righe con valori tutti arrotondati all'intero più vicino: ")
X = iris.drop("variety", axis=1)
iris_round = X.applymap(lambda val:int(round(val, 0))).head()
print(iris_round)
print()

# Possiamo interfacciarci con la libreria matplotlib per costruire grafici e rappresentazioni
# Per esempio, possiamo fare un grafico per visualizzare la relazione che c'è tra la lunghezza
# del sepalo e la larghezza
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
iris_plot = iris.plot(x="sepal.length", y="sepal.width", kind="scatter")
print(iris_plot)
