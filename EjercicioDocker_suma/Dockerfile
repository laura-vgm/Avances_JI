FROM python:latest
# se importa la imagen base, en este caso es la última versión de python

COPY funcion_suma.py /
# el código python se importa a nuestra imagen 
# El primer parámetro 'funcion.py' es el nombre del archivo en el host.
# El segundo parámetro '/' es la ruta donde colocar el archivo en la imagen.
# Aquí se coloca el archivo en la carpeta raíz de la imagen. 

CMD [ "python",  "funcion_suma.py"]
# Se define el comando a lanzar cuando se ejecute la imagen.
# Se ejecuta "python funcion.py".
