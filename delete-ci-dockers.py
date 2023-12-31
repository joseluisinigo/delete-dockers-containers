import subprocess

def mostrar_menu_opciones(opciones):
    print("Selecciona una opción:")
    for i, opcion in enumerate(opciones):
        print(f"{i + 1}. {opcion}")
    print("0. Salir")

def listar_contenedores():
    output = subprocess.check_output(['sudo', 'docker', 'ps', '--format', '{{.ID}}\t{{.Image}}\t{{.Names}}'], text=True)
    contenedores = [line.split('\t') for line in output.strip().split('\n')]
    
    print("Contenedores disponibles:")
    for i, (id_contenedor, imagen, nombre) in enumerate(contenedores):
        print(f"{i + 1}. ID: {id_contenedor}, Imagen: {imagen}, Nombre: {nombre}")
    
    return contenedores

def eliminar_contenedor(id_contenedor):
    subprocess.run(['sudo', 'docker', 'rm', '-f', id_contenedor])

def listar_imagenes():
    output = subprocess.check_output(['sudo', 'docker', 'image', 'list', '--format', '{{.ID}}\t{{.Repository}}:{{.Tag}}\t{{.Size}}'], text=True)
    imagenes = [line.split('\t') for line in output.strip().split('\n')]
    
    print("Imágenes disponibles:")
    for i, (id_imagen, nombre, tamano) in enumerate(imagenes):
        print(f"{i + 1}. ID: {id_imagen}, Nombre: {nombre}, Tamaño: {tamano}")
    
    return imagenes

def eliminar_imagen(id_imagen):
    subprocess.run(['sudo', 'docker', 'rmi', '-f', id_imagen])

def listar_y_eliminar_redes():
    output = subprocess.check_output(['sudo', 'docker', 'network', 'list', '--format', '{{.ID}}\t{{.Name}}'], text=True)
    redes = [line.split('\t') for line in output.strip().split('\n')]
    
    print("Redes Docker disponibles:")
    for i, (id_red, nombre_red) in enumerate(redes):
        print(f"{i + 1}. ID: {id_red}, Nombre: {nombre_red}")

    opcion_red = input("Selecciona el número de la red que deseas eliminar (o 0 para cancelar): ")
    if opcion_red.isdigit() and 1 <= int(opcion_red) <= len(redes):
        subprocess.run(['sudo', 'docker', 'network', 'rm', redes[int(opcion_red) - 1][1]])
        print(f"Red {redes[int(opcion_red) - 1][1]} eliminada.")
    elif opcion_red == '0':
        print("Operación cancelada.")
    else:
        print("Opción no válida. Introduce un número válido.")

def limpiar_docker():
    subprocess.run(['sudo', 'docker', 'image', 'prune', '-f'])
    subprocess.run(['sudo', 'docker', 'container', 'prune', '-f'])
    subprocess.run(['sudo', 'docker', 'builder', 'prune', '-f'])

opciones_principales = ["Listar y eliminar contenedores", "Listar y eliminar imágenes", "Listar y eliminar redes Docker", "Limpiar Docker"]
while True:
    mostrar_menu_opciones(opciones_principales)
    opcion = input("Selecciona una opción: ")
    if opcion == '0':
        break
    elif opcion == '1':
        contenedores = listar_contenedores()
        opcion_contenedor = input("Selecciona el número del contenedor que deseas eliminar (o 0 para cancelar): ")
        if opcion_contenedor.isdigit() and 1 <= int(opcion_contenedor) <= len(contenedores):
            eliminar_contenedor(contenedores[int(opcion_contenedor) - 1][0])
        elif opcion_contenedor == '0':
            print("Operación cancelada.")
        else:
            print("Opción no válida. Introduce un número válido.")
    elif opcion == '2':
        imagenes = listar_imagenes()
        opcion_imagen = input("Selecciona el número de la imagen que deseas eliminar (o 0 para cancelar): ")
        if opcion_imagen.isdigit() and 1 <= int(opcion_imagen) <= len(imagenes):
            eliminar_imagen(imagenes[int(opcion_imagen) - 1][0])
        elif opcion_imagen == '0':
            print("Operación cancelada.")
        else:
            print("Opción no válida. Introduce un número válido.")
    elif opcion == '3':
        listar_y_eliminar_redes()
    elif opcion == '4':
        limpiar_docker()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

print("¡Hasta luego!")
