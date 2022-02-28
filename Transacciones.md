## Transacciones
EJEMPLO:
imaginemos que yo quiero transferir dinero de una cuenta a otra dentro de una base de datos, esto seria 
una transaccion, pero al ocurrir cualquier error en el servidor esta no se debe ejecutar o es todo o nada,
es por esto que las transacciones siguen el modelo **ACID**

1. Atomicidad: aseguran que todas las operaciones dentro de la secuencia de trabajo se completen satisfactoriamente. Si no es así, la transacción se abandona en el punto del error y las operaciones previas retroceden a su estado inicial.
2. Consistencia: aseguran que la base de datos cambie estados en una transacción exitosa.
3. Aislamiento: permiten que las operaciones sean aisladas y transparentes unas de otras.
4. Durabilidad: aseguran que el resultado o efecto de una transacción completada permanezca en caso de error del sistema.


Ejemplo de transaccion en python:

```python
import mysql.connector

try:
    conn = mysql.connector.connect(host='localhost',
                                   database='python_db',
                                   user='pynative',
                                   password='pynative@#29')

    conn.autocommit = False
    cursor = conn.cursor()
    # Retiro de la cuenta A 
    sql_update_query = """Update account_A set balance = 1000 where id = 1"""
    
    # Cursos nos sirve para ejecutar instrucciones
    cursor.execute(sql_update_query)

    # Deposito a la cuetna B 
    sql_update_query = """Update account_B set balance = 1500 where id = 2"""
    cursor.execute(sql_update_query)
    print("Record Updated successfully ")

    # Commit cambios
    conn.commit()

except mysql.connector.Error as error:
    print("Fallo al actualizar los registros rollback: {}".format(error))
    # revierte los cambios al entrar a la exepcion
    conn.rollback()
finally:
    # cierra la conexion a la db.
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("conexion cerrada")
```
