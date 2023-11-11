#Set
names = {"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"}
print(names)

#aggiunta di un elemento
names.add("Lorenzo")
print(names)

#rimuovere un elemento
names.remove("Antonino")
print(names)

names.discard("Paolo")
print(names)

#estrazione di un elemento
name = names.pop()
print(name)
print(names)

#svuotare il set
names.clear()
print(names)

#conversione da lista a set
names_list = ["Giuseppe", "Federico", "Antonino", "Matteo", "Federico"]
print(names_list)

names_set = set(names_list)
print(names_set)

#conversione da set a lista 
names_list = list(names_set)
print(names_list)

#frozenset
names = frozenset({"Giuseppe", "Federico", "Antonino", "Matteo", "Federico"})
