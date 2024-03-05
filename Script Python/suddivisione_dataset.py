import pandas as pd

# Il dataset che utilizzeremo contiene diverse informazioni legate a delle abitazioni
# della zona di Boston.
boston = pd.read_csv("C:/Users/39346/IdeaProjects/Appunti-Python/data/boston.csv", index_col=0)
print("Verifico il dataset: ")
print(boston.head())
print()

# Per effettuare la suddivisione del dataset, partiamo dal test set e serviamoci del metodo sample() per
# selezionare random una frazione del dataset
boston_test_df = boston.sample(frac=0.3) #il 30% del dataset originario

# Per ottenere adesso il train set, eliminiamo dal dataset tutti gli elementi contenuti anche nel test set.
boston_train_df = boston.drop(boston_test_df.index)

# Per effettuare una verifica, diamo uno sguardo alla dimensione dei due dataset.
print("Numero di esempi nel Train Set: "+str(boston_train_df.shape[0]))
print("Numero di esempi nel Test Set: "+str(boston_test_df.shape[0]))
