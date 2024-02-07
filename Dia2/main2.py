# -------------------------------DIA 2-------------------------
#Structuras de control
#if, matvh (Swith), foreach, while

#Bool
#True / False
#Operadores relacionales (==, !=, >, >= <, <=)
#Operadores logicos (and, or, not)



number1 = 10
number2 = 20

result = number1 == number2
result1 = number1 != number2


#CON EL AND TODO TIENE QUE SER VERDADERO PARA QUE SEA VERDADERO, SI HAY ALGO NEGATIVO TODO SE CONVIERTE NEGATIVO
#               TRUE               TRUE       FALSO
result2 = number1 != number2 and 10 == 10 and 5 != 5 

#CON EL OR CON QUE SEA 1 VERDADERO YA DA EL VERDADERO
#               TRUE              FALSE      FALSO
result3 = number1 != number2 or 10 == 20 or 5 != 5 

print(result3)