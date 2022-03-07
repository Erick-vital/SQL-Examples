from pydoc import cli
import click
import logging
from logConf import *
from conexion import ConexionDB
import requests
import json
from validaciones import Validaciones

c = ConexionDB() 
v = Validaciones()

@click.command()
@click.option('--tabla', is_flag=True, help='crear tabla')
@click.option('--insertar', is_flag=True, help='inserta registros a la tabla')
@click.option('--order', is_flag=True, help='ordena los nombres alfabeticamente')
@click.option('--registros', is_flag=True, help='muestra los registros de la tabla')
@click.option('--drop', is_flag=True, help='borra la tabla')
@click.option('--procedimiento', is_flag=True, help='crea un procedimiento almacenado')
# @click.option('--apellido', prompt="tu apellido", help="escribe tu apellido")
def process(tabla, insertar, order, registros, drop, procedimiento):
    if tabla:
        c.crear_tabla()
        print('soy la tabla')
    elif insertar:
        try:
            insertartDatosDummy()
            click.echo('datos insertados en la db')
        except:
            click.echo('no existe tabla, favor de crear una con la opcion --tabla')
    elif order:
        ordenarPorNombre()
    elif registros:
        consultaRegistros()
    elif drop:
        c.drop_tabla()
    elif procedimiento:
        c.crear_procedimiento()
    


def insertartDatosDummy():
    r = requests.get('https://api.mockaroo.com/api/deb00080?count=10&key=fad71d20')
    y = json.loads(r.text)
    cursor = c.conexion.cursor()
    
    for i in range(0, len(y) - 1):
        # validaciones
        """
            todos los datos tienen que cumplir con las validaciones  
            esperado antes de continuar con el procedimiento y si este
            no cumple se lanzara una excepcion
        """
        if v.is_name(y[i]['first_name']):
            pass
        else:
            logging.error('nombre no es correcto')
            click.echo('nombre no es correcto')
            break
        if v.is_name(y[i]['last_name']):
            pass
        else:
            logging.error('apellido no es correcto')
            click.echo('apellido no es correcto')
            break
        if v.is_email(y[i]['email']):
            pass
        else:
            logging.error('email no es correcto')
            click.echo('email no es correcto')
            break
        if v.is_gender(y[i]['gender']):
            pass
        else:
            logging.error('genero no es correcto')
            click.echo('genero no es correcto')
            break
        if v.is_ip(y[i]['ip_address']):
            pass
        else:
            logging.error('ip no es correcta')
            click.echo('ip no es correcta')
            break
        cursor.callproc('insertar_cliente', args=(
            y[i]['first_name'],
            y[i]['last_name'], 
            y[i]['email'], 
            y[i]['gender'], 
            y[i]['ip_address']
            ))
        c.conexion.commit()
        logging.info("datos insertados")
    click.echo('datos dummy insertados')

 
def consultaRegistros():
    query = "select * from BANCO.ClienteBanco"

    records = c.query(query)
    
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")


def ordenarPorNombre():
    query = "select * from BANCO.ClienteBanco order by first_name"

    records = c.query(query)
    
    print("Ordena los nombres de forma alfabetica")
    for row in records:
        print('nombre: ', row[1], '\n')

if __name__ == '__main__':
    process()
    c.cerrar_conexion()