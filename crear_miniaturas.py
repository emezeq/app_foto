#!/usr/bin/python
#-*-encoding:utf-8-*-

from PIL import Image
import glob, os

os.makedirs("/tmp/miniaturas/jpg")
size = 128, 128

def hacer_miniaturas(carpeta_a_analizar):
    for foto in glob.glob(carpeta_a_analizar+"*.jpg"):
        fichier = os.path.basename(foto)
        file, ext = os.path.splitext(fichier)
        im = Image.open(foto)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save( "/tmp/miniaturas/jpg/" + file + ".jpeg" , "JPEG")
        
