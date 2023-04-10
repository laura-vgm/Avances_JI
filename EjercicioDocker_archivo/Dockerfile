FROM python:latest                  
# se importa la imagen base, en este caso es la última versión de python

COPY ejercicio_archivo.py /         
# el código python se importa a nuestra imagen 
# El primer parámetro 'ejercico_archivo.py' es el nombre del archivo en el host.
# El segundo parámetro '/' es la ruta donde colocar el archivo en la imagen.
# Aquí se coloca el archivo en la carpeta raíz de la imagen. 

CMD [ "python",  "ejercicio_archivo.py"]
# Se define el comando a lanzar cuando se ejecute la imagen.
# Se ejecuta "python ejercicio_archivo.py".