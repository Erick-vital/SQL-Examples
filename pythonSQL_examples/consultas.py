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

load_dotenv()
c = ConexionDB()

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    logging.info('iniciando la db')
    c.iniciar_conexion()
    click.echo('conexion iniciada')

@cli.command()
def dropdb():
    c.cerrar_conexion()
    click.echo('Dropped the database')

@cli.command()
def consultaRegistros():
    cursor = c.conexion.cursor()
    query = "select * from BANCO.ClienteBanco"
    cursor.execute(query)

    records = cursor.fetchall()
    
    print("Total number of rows in table: ", c.cursor.rowcount)
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")
    click.echo('Dropped the database')


if __name__ == '__main__':
    cli()

