#n = int(input("Fino a che numero vuoi stampare ? "))

#for i in range(0,n):
#    print(i)

#iterazione sulle liste
shopping_list = ["tofu", "latte di soia", "riso basmati", "yogurt greco"]

for index, element in enumerate(shopping_list):
    print("%d) %s" % (index+1, element)) 