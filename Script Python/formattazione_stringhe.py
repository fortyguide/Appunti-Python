cat = "Elon"
age = 2
weight = 5.678

#Formattazione (old school)
print("Il mio gatto si chiama %s, ha %d anni e pesa %.2f kg" % (cat, age, weight))

#Formattazione (new school)
print("Il mio gatto si chiama {cat}, ha {age} anni e pesa {weight} kg".format(cat=cat, age=age, weight=weight))

#Formattazione Python 3.6
print(f"Il mio gatto si chiama {cat}, ha {age} anni e pesa {weight} kg")
