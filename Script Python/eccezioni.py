#var = "gatto"
#var = int(var)

num = input("Inserisci un numero: ")
try:
	print(type(num))
	num = int(num)
	print("Il numero che hai inserito è",num)
except ValueError:
	print("Il dato che hai inserito non è un numero")