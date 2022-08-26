# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 14:06:37 2022

@author: DIGITADOR10
"""
import msvcrt
import mysql.connector as sql
import os

conexion = sql.connect(
                    host = "sistemajudicial.com", 
                    user = "diego", 
                    passwd = "S1st3m4w3b",
                    database = "redjudicial")


inputFile=input("\n\nIngrese las cedulas a consultar separadas por comas: ")
dias = input("\nPeriodo de tiempo a consultar: ")
listFile=inputFile.split(",")
os.system ("cls")


for file in listFile:
         
    
    cedula = f"""SELECT COUNT(id_z04_estado) AS "Movimientos",
(SELECT COUNT(z02_abogado_idcedula_z02) FROM redjudicial.z01_radicacion_has_z02_abogado WHERE z02_abogado_idcedula_z02 LIKE "%{file}%" HAVING COUNT(z02_abogado_idcedula_z02)) AS "Procesos"
from z04_estado
JOIN z01_radicacion_has_z02_abogado ON z01_radicacion_has_z02_abogado.z01_radicacion_juzgado=z04_estado.z01_radicacion_juzgado
AND z01_radicacion_has_z02_abogado.z01_radicacion_z01_radicacion=z04_estado.z01_radicacion_z01_radicacion
AND z01_radicacion_has_z02_abogado.ciudad=z04_estado.ciudad
JOIN z02_abogado ON z01_radicacion_has_z02_abogado.z02_abogado_idcedula_z02=z02_abogado.idcedula_z02
WHERE z02_abogado.privilegio=1 AND z04_estado.fecha_notificacion BETWEEN (CURDATE() - INTERVAL {dias} DAY) AND CURDATE() AND z02_abogado.idcedula_z02 LIKE "%{file}%"
HAVING COUNT(id_z04_estado)"""


    print("-"*15)
    print("Proceso:")
    cursor = conexion.cursor()
    cursor.execute(cedula)
    consultasBD  = [item for item in cursor.fetchall()]
       
    print(f"La cedula: {file} Tiene:\nMovimientos: {consultasBD[0][0]}\nProcesos: {consultasBD[0][1]}")
    print("-"*15)

print("--Presione una tecla para cerrar--")
msvcrt.getch()

