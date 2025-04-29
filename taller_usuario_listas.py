lista_personas = []

while True:
    print("\n")
    print("\033[1m\033[31m=\033[0m" * 30)
    print("\033[1m\033[34m=\033[0m" * 30)
    opciones = int(input("\033[1m\033[32mMenu De usuario\033[0m"
                         "\n\033[1m\033[32m1\033[0m Crear Usuario"
                         "\n\033[1m\033[32m2\033[0m Consultar Usuarios"
                         "\n\033[1m\033[32m3\033[0m Eliminar Usuario"
                         "\n\033[1m\033[32m4\033[0m Modificar Usuario"
                         "\n\033[1m\033[32m5\033[0m Salir"
                         "\nOpcion = "))

    if opciones == 1:
        nombre = input("\n\033[1m\033[32mIngrese Nombre: \033[0m")
        apellido = input("\033[1m\033[32mIngrese Apellido:\033[0m ")
        correo = input("\033[1m\033[32mIngrese Correo:\033[0m ")
        edad = input("\033[1m\033[32mIngrese Edad: \033[0m")
        usuario = [nombre, apellido, correo, edad]  
        lista_personas.append(usuario)
        print("\n\033[1m\033[32mUsuario creado correctamente")

    elif opciones == 2:
        if lista_personas:
            print("\nLa lista de usuarios es:")
            
            i = 0
            while i < len(lista_personas):
                usuario = lista_personas[i]
                print(str(i + 1) + "." "\n\033[1m\033[32mNombre\033[0m : "+ usuario[0] + "\n\033[1m\033[32mApellido : \033[0m" + usuario[1] + "\n\033[1m\033[32mCorreo : \033[0m" + usuario[2] + "\n\033[1m\033[32mEdad : \033[0m" + str(usuario[3]))
                i += 1
        else:
            print("\033[1m\033[31mNo hay usuarios registrados")

    elif opciones == 3:
        if lista_personas:
            usuario_a_eliminar = int(input("Ingrese el número del usuario a eliminar: ")) - 1
            if 0 <= usuario_a_eliminar < len(lista_personas):
                del lista_personas[usuario_a_eliminar]
                print("\033[1m\033[34mUsuario eliminado correctamente")
            else:
                print("\033[1m\033[31mNúmero de usuario incorrecto")
        else:
            print("\033[1m\033[31mNo hay usuarios")

    elif opciones == 4:
        if lista_personas:
            usuario_a_actualizar = int(input("Ingrese el número del usuario que desea modificar: ")) - 1
            if 0 <= usuario_a_actualizar < len(lista_personas):
                usuario = lista_personas[usuario_a_actualizar]

                nuevo_nombre = input("Ingrese nuevo nombre (Enter para mantener): ")
                if nuevo_nombre:
                    usuario[0] = nuevo_nombre

                nuevo_apellido = input("Ingrese nuevo apellido (Enter para mantener): ")
                if nuevo_apellido:
                    usuario[1] = nuevo_apellido

                nuevo_correo = input("Ingrese nuevo correo (Enter para mantener): ")
                if nuevo_correo:
                    usuario[2] = nuevo_correo

                nueva_edad = input("Ingrese nueva edad (Enter para mantener): ")
                if nueva_edad:
                    usuario[3] = nueva_edad

                print("\033[1m\033[32mUsuario modificado correctamente")
            else:
                print("\033[1m\033[31mNúmero ingresado incorrecto")
        else:
            print("\033[1m\033[31mNo hay usuarios para modificar")

    elif opciones == 5:
        print("\033[1m\n\033[31mSaliendo del programa")
        break

    else:
        print("\n\033[1m\033[31mOpción inválida")
