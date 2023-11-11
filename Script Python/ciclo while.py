#uguaglianza
is_equal = 5 == 5
print(is_equal)

#disuguaglianza
is_different = "casa" != "gatto"
print(is_different)

#maggioranza
is_greater = 6 > 9
print(is_greater)

is_greater_or_equal = 6 >= 6
print(is_greater_or_equal)

#minoranza
is_less = 6 > 9
print(is_less)

is_less_or_equal = 6 <= 6
print(is_less_or_equal)

#ciclo while
n = int(input("Fino a che numero vuoi contare? "))

i = 0

while i < n :
    if(i % 3 == 0): #multipli di 3
        i += 2
        continue
    print(i)
    i += 2

