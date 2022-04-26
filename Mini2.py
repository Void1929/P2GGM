# -*- coding: utf-8 -*-
"""
@author: kilde
"""

import csv
import random

def leerArchivoR(nomArchivo, noLineas):
	listaDatos = []
	listaDatosAleatoria = []
	with open(nomArchivo) as archivoCSV:
		lectorCSV = csv.reader(archivoCSV,delimiter=',')
		archivoCSV.readline()
		for linea in lectorCSV:
			nombre, frec, edadMedia = linea
			listaDatos.append(nombre)
		
		posFinal = len(listaDatos) - 1
		for i in range(noLineas):
			posAleatoria = random.randint(1, posFinal)
			listaDatosAleatoria.append(listaDatos[posAleatoria])
	return listaDatosAleatoria
	
def leerMixtoR(nomArchivo1, nomArchivo2, noLineas):
	listaDatos1 = leerArchivoR(nomArchivo1, noLineas)
	listaDatos2 = leerArchivoR(nomArchivo2, noLineas)
	listaMixto = listaDatos1 + listaDatos2
	random.shuffle(listaMixto)
	return listaMixto

def escribirArchivo(nomArchivo, noLineas, nombres, apellidos):
	with open(nomArchivo, 'w', newline="") as archivoCSV:
		escritorCSV = csv.DictWriter(archivoCSV,fieldnames=["Nombre", "Apellido Paterno", "Apellido Materno"],delimiter='|')
		escritorCSV.writeheader()
		for i in range(noLineas):
			nombre = nombres[i]
			apPat = apellidos[i]
			apMat = apellidos[noLineas-1-i]
			escritorCSV.writerow({"Nombre": nombre, "Apellido Paterno": apPat, "Apellido Materno": apMat})

OpA = 0
OpB = 0	
try:
	OpA = int(input('Seleccione:' + "1. Hombres" + "2. Mujeres" + "3. Mixto (Hombres y mujeres)"))
except ValueError:
	print ("Intentalo de nuevo")
	
try:
    OpB = int(input('¿Cuantos Nombres desea generar? (1 a 1000)'))
except ValueError:
        print ("Intentalo de nuevo")
        
listaNombres = []
listaApellidos = []
if(OpA == 1):
	listaNombres = leerArchivoR("hombres.csv", OpB)
elif(OpA == 2):
	listaNombres = leerArchivoR("mujeres.csv", OpB)
elif(OpA == 3):
	listaNombres = leerMixtoR("hombres.csv", "mujeres.csv", OpB)
listaApellidos = leerArchivoR("apellidos.csv", 2*OpB)
	
archivoDestino = "NombresComp.csv"
escribirArchivo(archivoDestino, OpB, listaNombres, listaApellidos)
print("Se han escrito " + str(OpB) + " nombres en el archivo " + archivoDestino)