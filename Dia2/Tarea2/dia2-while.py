num_registro = input("¿Cuántos usuarios quieres dar de alta? ")

try:
    num_registro = int(num_registro)
    if num_registro > 0:
        print(f"Se registrarán {num_registro} usuarios.")
        for i in range(num_registro):
            print(f"\nIngresa los datos a continuación del usuario {i+1}")

            # Obtener nombre
            while True:
                nombre = input("Ingresa el nombre: ")
                if 5 <= len(nombre) <= 50:
                    break
                else:
                    print(
                        "Intenta de nuevo. El nombre debe tener entre 5 y 50 caracteres.")

            # Obtener apellidos
            while True:
                apellidos = input("Ingresa los apellidos: ")
                if 5 <= len(apellidos) <= 50:
                    break
                else:
                    print(
                        "Intenta de nuevo. Los apellidos deben tener entre 5 y 50 caracteres.")

            # Obtener número de teléfono
            while True:
                try:
                    num_telefono = int(
                        input("Ingresa el número de teléfono: "))
                    num_telefono_string = str(num_telefono)
                    if len(num_telefono_string) == 10:
                        break
                    else:
                        print(
                            "Intenta de nuevo. El número de teléfono debe tener 10 dígitos.")
                except ValueError:
                    print("Intenta de nuevo. Ingresa un número válido.")

            # Obtener correo electrónico
            while True:
                correo_electronico = input("Ingresa el correo electrónico: ")
                if 5 <= len(correo_electronico) <= 50:
                    break
                else:
                    print(
                        "Intenta de nuevo. El correo electrónico debe tener entre 5 y 50 caracteres.")

            # Mostrar información del usuario registrado
            print(f"\nInformación del Usuario {i+1} registrado:")
            print(
                f"Nombre: {nombre}\nApellidos: {apellidos}\nNúmero de teléfono: {num_telefono}\nCorreo electrónico: {correo_electronico}")
    else:
        print("El número de usuarios debe ser mayor que cero.")
except ValueError:
    print("La entrada no es un número entero del número de teléfono.")
