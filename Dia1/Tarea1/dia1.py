#El programa deberá pedir a nuestro usuario final ingrese su siguiente información.
#gist // https://gist.github.com/sebastian-quijas9/280a69c10963e1617640f977059dc1d6


nombre = input("INGRESA LOS DATOS A CONTINUACION \nIngresa tu nombre: ")
apellidos = input("Ingresa tus apellidos: ")
num_telefono = int(input("Ingresa tu numero de telefono: "))
correo_electronico = input("Ingresa tu correo electronico: ")

full_name = nombre + " " + apellidos



print("Hola "+ full_name +" en breve recibirás un correo a " + correo_electronico)