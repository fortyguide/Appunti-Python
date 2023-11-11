#Liste
my_list = [10, 5, 8, 3, 11, 2]
print(type(my_list))
lunghezza_lista = len(my_list)
print("La lista è lunga",str(lunghezza_lista))

#indexing
print(my_list[0])
print(my_list[1])
print(my_list[-1])

#slicing
print(my_list[0:3])
print(my_list[:5])
print(my_list[2:])
print(my_list[:])

print(my_list[::-1])

#modifica del primo valore della lista
my_list[0] = 0

#modifica degli ultimi due valori della lista
my_list[-2:] = [7,1]
print(my_list[:])

#ricerca elemento nella lista
animals = ["cane", "gatto", "topo"]
print("uomo" in animals)
print("gatto" in animals)

#rimozione per valore
animals.remove("gatto")
print(animals)

#rimozione per indice
animal = animals.pop(1)
print(animals)
print(animal)

#aggiunta elemento nella lista
animals.append("bestia demoniaca")
print(animals)

#aggiunta elemento nella lista in una posizione predefinita
animals.insert(1, "topo")
print(animals)

#Tuple
my_tuple = (10, 5, 8, "ciao", 3, 9, "ciao")
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
print(my_tuple[:3])

# my_tuple[0] = 0

#ottenere l'indice di un elemento
indice = my_tuple.index("ciao")
print(str(indice))

#ottenere il numero di volte in cui un elemento è presente nella lista/tupla
n_occorrenze = my_tuple.count("ciao")
print(str(n_occorrenze))