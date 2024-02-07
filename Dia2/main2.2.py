# -------------------------------DIA 2-------------------------
# if, matvh (Swith), foreach, while

if 10 != 20:
    print("la condicion se cumple")
else:
    print("Se ejecuta cuando la condicion no se cumpla")

age = int(input("Ingresa tu edad: "))

if age >= 18:
    print("Ya eres mayor de edad")
    if age >= 19 and age <= 45:
        print("Eres menor de 45 y mayor de 18 ")
else:
    print("Eres menor de 18")

color = "Green"

if color == "Green":
    print("Puede continuar")
else:
    if color == "Yellow":
        print("Alto parcial")
    else:
        if color == "Red":
            print("Alto total")


if color == "Green":
    print("Puede continuar")
elif color == "Yellow":
    print("Alto parcial")
elif color == "Red":
    print("Alto total")
else:
    print("El color no es valido")

# match es como el switch en otro lenguaje de programacion
match color:
    case 'Red':
        print("Alto total")
    case "Yellow":
        print("Alto parcial")
    case "Green":
        print("Puede continuar")
    case _:
        print("No es valido el color")





#Collections (String)

title = "Estructuras de control"
for caracter in title:
    # print(caracter)
    print()


# Saber si los numeros son par
rangos = range(1, 11)

for cara in rangos:
    if cara % 2 == 0:
        # print(cara)
        print()


# Saber si los numeros son IMPAR
rangos = range(1, 11)

for cara in rangos:
    if not cara % 2 == 0:
        # print(cara)
        print()

numero = 0

while numero < 10:
    print(numero)
    numero += 1
else:
    print("No se cumple")