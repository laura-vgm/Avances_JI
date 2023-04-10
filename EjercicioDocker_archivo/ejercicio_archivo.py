import os

url = input("Ingrese la ruta de la dirección del archivo: ")
archivo = open(url, 'r')
informacion = archivo.read()
archivo.close()

nuevo_contenido = informacion.replace('Sujeto','Nuevo_sujeto')+'Archivo modificado'
print(nuevo_contenido)
nueva_ruta = input('Ingrese la ruta de la carpeta en donde desea guardar el archivo modificado: ')
archivo_nuevo = 'nuevo_archivo.txt'
ruta_nueva = os.path.join(nueva_ruta, archivo_nuevo)

with open(ruta_nueva, 'w') as archivo_nuevo: # con with open se abre el archivo, 'w' se establece que sea de escritura
    archivo_nuevo.write(nuevo_contenido)  

#/home/laura/Documentos/UdeA/GRUNECO/Docker/EjercicioDocker_archivo/archivo1
#/home/laura/Documentos/UdeA/GRUNECO/Docker/EjercicioDocker_archivo/Salida