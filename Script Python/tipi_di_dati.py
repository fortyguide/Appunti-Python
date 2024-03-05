import pandas as pd

# Carichiamo il dataset all'interno di un dataframe.
shirts = pd.read_csv("C:/Users/39346/IdeaProjects/Appunti-Python/data/shirts.csv", index_col=0)
print("Verifico il dataset: ")
print(shirts.head())
print()

# Osservando il dataset, le colonne taglia e colore sono entrambe rappresentate da label e appartengono
# alla categoria delle variabili categoriche. Più nello specifico, taglia appartiene alla sottocategoria
# delle variabili ordinali, poichè è possibile stabilire una relazione di ordine tra i vari label. Colore
# invece appartiene alla sottocategoria delle variabili nominali, poichè non è possibile stabilire alcuna
# relazione di ordine, ma soltanto quella di uguaglianza.

# Data questa premessa, vediamo due metodi che ci permettono di trasformare questo tipo di variabili in numeri.
# Partendo dalle ordinali, il metodo consiste nel sostituire il label con un numero che rappresenta l'ordine
# tramite l'uso di un dizionario.
mappa_taglie = {"S":0, "M":1, "L":2, "XL":3}

# Utilizzando Pandas, possiamo servirci del metodo map() per sostituire tutti i valori chiave della mappa
# creata precedentemente con il suo contenuto.
shirts["taglia"] = shirts["taglia"].map(mappa_taglie)
print("Verifico che i valori della colonna taglia siano stati sostituiti dai numeri predefiniti: ")
print(shirts.head())
print()

# Nel caso di variabili nominali questo metodo non è applicabile, poichè appunto non può essere definita
# una relazione di ordine al loro interno. Il metodo da utilizzare in questi casi consiste nella sostituzione
# della colonna con più colonne, una per ogni label. Ogni colonna creata conterrà una variabile booleana
# che indica l'appartenenza o meno alla classe rappresentata dalla label (0 per False e 1 per True).
shirts = pd.get_dummies(shirts, columns=["colore"]).astype(int)
print("Verifico che la colonna colore sia stata suddivisa in più colonne contenenti valori 0 o 1: ")
print(shirts.head())
print()
