#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import commands
import shutil
import funciones
from PIL import Image
import glob, os
import crear_miniaturas
import listar


from  Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

root = Tk()
root.directory = tkFileDialog.askdirectory()
a = (root.directory)


#a = raw_input("Ingresar la carpeta a analizar: ")

#Esta linea puede ser que necesite quedar comentada para evitar errores, o descomentarla para solucionarlos.
#a = u' '.join(a).encode('utf-8').strip()

carpeta_a_analizar = a.replace(" ", "")
if carpeta_a_analizar != "/":
    carpeta_a_analizar = carpeta_a_analizar+"/"
print "CARPETA A ANALIZAR: ",carpeta_a_analizar

#creo las miniaturas importo la funcion
crear_miniaturas.hacer_miniaturas(carpeta_a_analizar)
#aca hago el link a la carpeta con las miniaturas, para que analize esta ultima
carpeta_a_analizar_real = "/tmp/miniaturas/jpg/"

print "carpeta donde hara el escaneo: ",carpeta_a_analizar_real
plantilla = "primero"
shutil.copy(plantilla, "primero.py")
fichero = "primero.py"
ficheror = open(fichero, "r")
buf = ficheror.read()
char10 = "delta"
char20 = carpeta_a_analizar_real
char20 = str(char20)
ficherow = open(fichero, "w")
rbuf = buf.replace(char10, char20)
ficherow.write(rbuf)
#cierro los ficheros
ficheror.close()
ficherow.close()

contador = 0
char2 = 0
while 1 > 0:

    resultado1=commands.getoutput('/usr/bin/python primero.py')#ejecuto primero.py
    print resultado1
    filename = 'plan.py'
    filer = open(filename, "r")
    buff = filer.read()
    char1 = "alfa"
    char2 = str(char2)
    contador = contador + 1
    #...esto es para implementar la Progress_Bar
    if contador >= 2:
        z = len(lista_valor)
        por_ciento = contador*100/z
        print "Completado al ",por_ciento ,"% ..."
#print "Analizando una nueva tanda......\n"
    filew = open(filename, "w")
    rbuff = buff.replace(char1, char2)
    filew.write(rbuff)
    filer.close()
    filew.close()
#ejecuto script plan.py
    comparacion=commands.getoutput('/usr/bin/python plan.py')
    print comparacion
    char2 = int(char2)
    char2 = char2 +1 #actualiza el indice de uno en uno
    ruta = (carpeta_a_analizar_real)            #ruta de las imagenes a analizar
    funciones.crear_carpeta('/tmp/fotos_borradas') ##############CREAR LA CARPETA TEMPORAL
    lista_valor = []

    def actualizar_lista():
        for f in os.listdir(ruta): #ficheros reemplazado directamente por el comando os.listdir
            (nombreFichero, extension) = os.path.splitext(f)
#if extension == ".jpeg" or extension == ".jpg": #decanto por extension
            if extension == ".jpeg":
#analizo solo .jpeg
                global lista_valor
                lista_valor.append(ruta+nombreFichero+extension)
    actualizar_lista()

    try:#si hay error de indice es porque se acabaron las fotos a analizar
        if lista_valor[char2] != "":
            print "Comparando... ",lista_valor[char2]
    except IndexError:
        print "\n-##########- ANALISIS TERMINADO -#############-"
        #elimino los ficheros temporales de trabajo plan.py, funciones.pyc, primero.py, y miniaturas
        os.remove("plan.py")
        os.remove("funciones.pyc")
        os.remove("primero.py")
        #busco si todas las imagenes originales estan en la lista temporal
        #print "carpeta donde estan las fotos a analizar ",carpeta_a_analizar
        listar.proc(carpeta_a_analizar)
        break
#elimino la carpeta miniaturas
shutil.rmtree("/tmp/miniaturas")
