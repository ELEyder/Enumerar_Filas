import os
#Definir la ruta del archivo
os.system("cls")
ruta = os.path.dirname(os.path.abspath(__file__)) + "\\"
#Mostrar la ruta _del _archivo
print("ruta del archivo: ", ruta)
#Abrir el archivo de texto
archivo = open(ruta + "archivo.txt")
#Contador de lineas del archivo
i=1
palabras = 0
#Leer lineas de archivo de texto linea por linea
total_palabras = 0
total_vocales = 0
vocales = ["a", "e", "i", "o", "u","A","E","I","O","U"]
numVocales = 0
for linea in archivo:
    linea = linea.rstrip("\\")
    #Obtener la longitud de la linea de texto
    longitud = len(linea)-1
    #Obtener cantidad de palabras
    for indice in range(longitud):
        caracter = linea[indice]
        if (caracter==" "):
            palabras = palabras + 1
        elif(caracter in vocales):
            numVocales = numVocales + 1
            
    #Mostrar la linea en pantalla
    print("%4d: %s" % (i,linea))
    print("Longitud de caracteres : ", longitud)
    print("Cantidad de palabras : ", palabras)
    print("Cantidad de Vocales : ", numVocales)
    total_palabras = total_palabras + palabras
    total_vocales = total_vocales + numVocales
    #Incrementar el contador de lineas
    i+=1
    palabras = 0
    numVocales = 0
print("Total de palabras del archivo: ", total_palabras)
print("Total de vocales del archivo: ", total_vocales)
#Cerrar archivo de texto
archivo.close()