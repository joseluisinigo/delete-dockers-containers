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

def limpiar_docker():
    subprocess.run(['sudo', 'docker', 'image', 'prune', '-f'])
    subprocess.run(['sudo', 'docker', 'container', 'prune', '-f'])
    subprocess.run(['sudo', 'docker', 'builder', 'prune', '-f'])

opciones_principales = ["Listar contenedores", "Eliminar contenedor por ID", "Listar imágenes", "Eliminar imagen por ID", "Limpiar Docker"]
while True:
    mostrar_menu_opciones(opciones_principales)
    opcion = input("Selecciona una opción: ")
    if opcion == '0':
        break
    elif opcion == '1':
        listar_contenedores()
    elif opcion == '2':
        contenedores = listar_contenedores()
        opcion_contenedor = input("Selecciona el número del contenedor que deseas eliminar: ")
        if opcion_contenedor.isdigit() and 1 <= int(opcion_contenedor) <= len(contenedores):
            eliminar_contenedor(contenedores[int(opcion_contenedor) - 1][0])
        else:
            print("Opción no válida. Introduce un número válido.")
    elif opcion == '3':
        listar_imagenes()
    elif opcion == '4':
        imagenes = listar_imagenes()
        opcion_imagen = input("Selecciona el número de la imagen que deseas eliminar: ")
        if opcion_imagen.isdigit() and 1 <= int(opcion_imagen) <= len(imagenes):
            eliminar_imagen(imagenes[int(opcion_imagen) - 1][0])
        else:
            print("Opción no válida. Introduce un número válido.")
    elif opcion == '5':
        limpiar_docker()
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

print("¡Hasta luego!")
