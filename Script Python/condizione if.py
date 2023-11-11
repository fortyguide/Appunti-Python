#istruzioni condizionali
n = int(input("Inserisci un numero positivo: "))

if(n < 0):
    print("%d non è un numero positivo" % n)
elif(n % 2 == 0):
    print("%d è un numero pari" % n)
else:
    print("%d è un numero dispari" % n)

#operatori logici
1 == 4 and 2 == 2
1 == 2 or 2 == 1
not 2 == 1