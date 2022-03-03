import mysql.connector
from mysql.connector import Error
# variables de entorno
from dotenv import load_dotenv
import os 
# log
import logging
from logConf import *


load_dotenv()

class ConexionDB:

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host = os.getenv('host'),
            database = os.getenv('database'),
            user = os.getenv('user'),
            password = os.getenv('password') 
        )
        self.cursor = self.conexion.cursor()

    def iniciar_conexion(self):
        try:

            if self.conexion.is_connected():
                db_info = self.conexion.get_server_info()
                logging.info(f'conexion a la DB establecida: {db_info}')

                # cursor nos sirve para ejecutar instrucciones sql
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                logging.info(f"You're connected to database: {record}" )
        except Error as e:
            logging.error(f'error al conectar a la db: {e}')

    def cerrar_conexion(self):
        if self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            logging.info('la conexion a la db se ha cerrado')
    

c = ConexionDB()
c.iniciar_conexion()
c.cerrar_conexion()