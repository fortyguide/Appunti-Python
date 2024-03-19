import pandas as pd

# Eseguiamo la regressione lineare semplice, utilizzando il dataset boston per predire il valore delle
# abitazioni a partire dal numero delle stanze.
boston = pd.read_csv("C:/Users/39346/IdeaProjects/Appunti-Python/data/boston.csv",
                     usecols=[6, 14])
print("Verifico il dataset: ")
print(boston.head())
print()

# Creiamo due array numpy collegati a proprietà e target
X = boston.drop("PRICE", axis=1).values     # Array per la proprietà
Y = boston["PRICE"].values      # Array per il target

# Dividiamo il dataset in due parti, ovvero test set e train set, utilizzando scikit-learn
# Configurare test_size=0.3 vuol dire assegnare il 30% del dataset al test set e la parte restante
# al train set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

# Possiamo utilizzare la classe LinearRegression di scikit-learn per costruire il nostro modello.
# Tutte le classi di scikit-learn funzionano allo stesso modo, ovvero si istanziano, si utilizza
# il metodo fit() per costruire il modello e si utilizza il metodo predict() per effettuare la predizione.
from sklearn.linear_model import LinearRegression
ll = LinearRegression()
ll.fit(X_train, Y_train)
Y_pred = ll.predict(X_test)

# Vediamo quanto è valido questo modello tramite la funzione di costo.
from sklearn.metrics import mean_squared_error
mean_squared_error = mean_squared_error(Y_test, Y_pred)
print("La funzione di costo ha restituito il valore " + str(mean_squared_error))

# Anche se otteniamo un valore dalla funzione di costo, non abbiamo un dato oggettivo.
# La metrica oggettiva per valutare la validità del modello sarà un range che va da 0 a 1.
# Per valori inferiori a 0.3 il modello è inutile, tra 0.3 e 0.5 è abbastanza scarso,
# tra 0.5 e 0.7 è discreto, tra 0.7 e 0.9 è buono, tra 0.9 a 1 è ottimo.
from sklearn.metrics import r2_score
r2_score = r2_score(Y_test, Y_pred)
print("Il punteggio del nostro modello è " + str(r2_score))

# Costruiamo un grafico che ci permette di visualizzare i coefficienti bias e peso
# che il nostro modello ha appreso.
import matplotlib.pyplot as plt
print("Peso di RM: " + str(ll.coef_[0]))
print("Bias: " + str(ll.intercept_))

plt.scatter(X_train, Y_train, c="green", edgecolor="white", label="Train set")
plt.scatter(X_test, Y_test, c="blue", edgecolor="white", label="Test set")

plt.xlabel("Numero medio di stanze [RM]")
plt.ylabel("Valore in $1000 [PRICE]")

plt.legend(loc="upper left")

plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.show()


