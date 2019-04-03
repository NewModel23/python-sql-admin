# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:24:03 2019

@author: rguerrerop
"""
import pyodbc as cnn
import pandas as pd
import os


# Copiar al Clipboard
def copia (argumento):
    df=pd.DataFrame(argumento)
    df.to_clipboard(index=False,header=True)

conexion = cnn.connect('DSN=;UID=;PWD=')
# cursor = conexion.cursor()
# sql = "Select * from PRODFINA.FNDRESMEN fetch first 10 rows only"

# data = pd.read_sql(sql, conexion)

# tabla = pd.read_sql("Select TABLE_SCHEMA || '.' || TABLE_NAME TABLE, TABLE_TEXT, TABLE_OWNER, TABLE_TYPE, COLUMN_COUNT, ROW_LENGTH from QSYS2.SYSTABLES where table_schema = 'PRODGRAL' AND tABLE_TEXT LIKE '%EQUIVALEN%'", conexion)

# columnas = pd.read_sql("SELECT TABLE_NAME,TABLE_SCHEMA,COLUMN_NAME,DATA_TYPE,IS_NULLABLE,COLUMN_TEXT  FROM QSYS2.SYSCOLUMNS WHERE TABLE_NAME = 'FNDRESMEN'", conexion)

# copia(tabla)

tablas_opl = pd.read_sql("Select * from qsys2.systables where table_schema = 'PRODFINA' and table_name like '%OPL%'", conexion)

reporteopl = pd.read_sql("Select * from PRODFINA.FNDRPTOPL WHERE FIFNYEAR = 2019 AND FIFNMONTH = 4 AND FIFNIDCIAU = 27", conexion)

os.getcwd()

pd.set_option('display.float_format', '{.1f}'.format)

query = open('C:/Users/rguerrerop/Documents/QueryData.sql', 'r')

consulta = query.read()

consulta1 = consulta.replace('[PREFIX]', 'PROD').replace('@IDAGENCIA', '27').replace('@EJERCICIO', '2019')

resultado = pd.read_sql(consulta1, conexion)






