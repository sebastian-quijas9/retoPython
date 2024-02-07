# El programa deberá preguntar cuando nuevos usuarios se pretenden registrar.
# gist //


num_registro = input("Cuantos usuarios quieres dar de alta?")

try:
    num_registro = int(num_registro)
    if num_registro > 0:
        print(f"Se registrarán {num_registro} usuarios.")
        for i in range(num_registro):
            print(f"Ingresa los datos a continuacion del usuario {i+1}")
            nombre = input("Ingresa el nombre: ")
            if len(nombre) >= 5 and len(nombre) <= 50:
                apellidos = input("Ingresa los apellidos: ")
                if len(apellidos) >= 5 and len(apellidos) <= 50:
                    num_telefono = int(
                        input("Ingresa el numero de telefono: "))
                    num_telefono_string = str(num_telefono)
                    if len(num_telefono_string) == 10:
                        correo_electronico = input(
                            "Ingresa el correo electronico: ")
                        if len(correo_electronico) >= 5 and len(correo_electronico) <= 50:
                            print(
                                f"\nInformación del Usuario {i+1} registrado:")

                            print(
                                f" El nombre registrado: {nombre} \n El apellido registrado: {apellidos} \n El numero de telefono registrado: {num_telefono} \n El correo electronico registrado: {correo_electronico}")
                        else:
                            print(
                                f"Intenta de nuevo el apellido tiene que ser mayor que 5 y menor que 50 y tienes: {len(correo_electronico)}")
                    else:
                        print(
                            f"Intenta de nuevo el numero de celular tiene que ser igual a 8 y tienes: {len(num_telefono_string)}")

                else:
                    print(
                        f"Intenta de nuevo el apellido tiene que ser mayor que 5 y menor que 50 y tienes: {len(apellidos)}")
            else:
                print(
                    f"Intenta de nuevo el nombre tiene que ser mayor que 5 y menor que 50 y tienes: {len(nombre)}")

    else:
        print("El número de usuarios debe ser mayor que cero.")
except ValueError:
    print("La entrada no es un número entero del numero de telefono.")
