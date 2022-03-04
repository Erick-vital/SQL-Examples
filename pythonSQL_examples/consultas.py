import click
# log
import logging
from logConf import *
# variables de entorno
from dotenv import load_dotenv
import os 
#conexion
import mysql.connector
from mysql.connector import Error
from conexion import ConexionDB
# peticiones
import requests
#json
import json

load_dotenv()
c = ConexionDB()

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    logging.info('Crear tabla')
    c.crear_tabla()

@cli.command()
def dropdb():
    c.cerrar_conexion()
    click.echo('Dropped the database')

@cli.command()
def consultaRegistros():

    #cursor = c.conexion.cursor()
    query = "select * from BANCO.ClienteBanco"
    #cursor.execute(query)

    records = c.query(query)
    
    print("Total number of rows in table: ", c.cursor.rowcount)
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")


@cli.command()
def ordenarPorNombre():

    # cursor = c.conexion.cursor()
    query = "select * from BANCO.ClienteBanco order by first_name"
    # cursor.execute(query)

    records = c.query(query)
    
    print("Ordena los nombres de forma alfabetica")
    for row in records:
        print('nombre', row[1], '\n')

@cli.command()
def insertarDatosDummy():
    r = requests.get('https://api.mockaroo.com/api/deb00080?count=10&key=fad71d20')
    y = json.loads(r.text)
    cursor = c.conexion.cursor()
    
    for i in range(0, len(y) - 1):
        cursor.callproc('insertar_cliente', args=(y[i]['first_name'], y[i]['last_name'], y[i]['email'], y[i]['gender'], y[i]['ip_address']))
        c.conexion.commit()
        logging.info("datos insertados")
    click.echo('datos dummy insertados')

if __name__ == '__main__':
    cli()

