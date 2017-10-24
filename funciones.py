#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import os
import commands
import shutil

def crear_carpeta(carpeta):
#carpeta = '/tmp/fotos_borradas' #carpeta donde guardo las fotos borradas
    if os.path.exists(carpeta) == True:
        pass
    else:
        os.makedirs(carpeta)
