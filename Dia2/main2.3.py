# -------------------------------DIA 2-------------------------
# if,
#  match (Swith),
# foreach ---> cuando sepamos cuantas iteraciones se necesitan
# while  --> cuando no sepamos cuantas iteraciones se necesitan (Condicion)

attends= 1
random, number, max_attends = 5, 0, 5

while number != random and attends <= max_attends :
    number = int( input("Ingresa un numero: "))
    attends += 1
else:
    if number == random:
        print("Felicidades encontraste el numero :) ")
    else:
        print("Se acabaron tus oportunidades :) ")