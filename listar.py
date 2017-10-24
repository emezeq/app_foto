#!/usr/bin/python
#-*-encoding:utf-8-*-

import glob, os


def proc(carpeta_a_analizar):
#busco si todas las imagenes originales estan en la lista temporal
    lista_v = []
    for i in os.listdir("/tmp/miniaturas/jpg/"):
        (nombreFichero, extension) = os.path.splitext(i)
        lista_v.append(nombreFichero)

    for foto in glob.glob(carpeta_a_analizar+"*.jpg"):
        fichier = os.path.basename(foto)
        fil, ext = os.path.splitext(fichier)
        
        if fil not in lista_v:
            print "...se ha borrado: ",foto
            os.remove(foto)
        
