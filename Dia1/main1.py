# -------------------------------DIA 1-------------------------
#Variables
#Tipos de datos
#int - float
#Nombre de la variable = valor 

first_name = "Sebastian" # String
last_name  = "Garcia Quijas"
# print(first_name)
# print(last_name)

full_name = first_name + " " + last_name
print(full_name)

#int, float, string, bool

age =24
score = 8.7
active = False

print(age)
print(score)
print(active)

#la funcion type es para saber de que tipo es si es int, float,string,bool
result = type(age)
print(result)


#Pedirle al usuario que ingrese algo y lo que ponga se almacena en resultado_de_lo_ingresado
resultado_de_lo_ingresado = input("Ingresa tu nombre: ")
print("Se ingreso por teclado tu nombre: "+ resultado_de_lo_ingresado)


name1 = input("Ingresa tu nombre: ")
age1 = input("Ingresa tu edad: ")
score1 = input("Ingresa tu calificacion: ")
active1 = input("El usuario se encuentra activo (si/no? ") == "si"


#cambiarlo a entero y a flotante
age1 = int(age1)
score1 = float(score1)

print(name1,age1,score1,active1)


#Aqui obtenemos el int o el float desde que preguntamos 
name2 = input("Ingresa tu nombre: ")
age2 = int(input("Ingresa tu edad: "))
score2 = float(input("Ingresa tu calificacion: "))
active2 = input("El usuario se encuentra activo (si/no? ") == "si"


print(name2,age2,score2,active2)