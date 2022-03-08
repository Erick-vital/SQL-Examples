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

    def probar_conexion(self):
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
            try:
                self.cursor.close()
                self.conexion.close()
                logging.info('la conexion a la db se ha cerrado')
            except Error as e:
                logging.error(f'error al cerrar: {e}')

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def crear_tabla(self):
        try:
            self.cursor.execute("""
            CREATE TABLE ClienteBanco (
                `ID` int NOT NULL AUTO_INCREMENT,
                `first_name` varchar(10) NOT NULL,
                `last_name` varchar(10) DEFAULT NULL,
                `email` varchar(40) DEFAULT NULL,
                `gender` varchar(10) DEFAULT NULL,
                `ip_address` varchar(16) DEFAULT NULL,
                PRIMARY KEY (`ID`)
            ) ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
            """)
            logging.info('tabla clientes_banco creada con exito')
            print('tabla clientes_banco creada con exito')
        except Error as e:
            logging.error(f'error al crear tabla {e}')
            print(f'error al crear tabla {e}')
    
    def drop_tabla(self):
        try:
            self.cursor.execute("""
            DROP TABLE IF EXISTS ClienteBanco;;
            """)
            logging.info('tabla eliminada correctamente')
            print('tabla eliminada correctamente')
        except Error as e:
            logging.error(f'error al remover tabla {e}')
            print(f'error al remover tabla {e}')
    
    def crear_procedimiento(self):
        try:
            self.cursor.execute("""
            CREATE DEFINER=`root`@`localhost` PROCEDURE `insertar_cliente`(nombre varchar(50), apellido varchar(50), correo varchar(50), genero varchar(50), ip varchar(50))
            BEGIN
                insert into ClienteBanco(first_name, last_name, email, gender, ip_address) values (nombre, apellido, correo, genero, ip); 
            END
            """)
            logging.info('procedimiento creado')
            print('procedimiento creado')
        except Error as e:
            logging.error(f'error al crear procedimiento {e}')
            print(f'error al crear procedimiento {e}')
    

    
    
