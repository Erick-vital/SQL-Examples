## Pequeno proyecto en python para probar librerias
Actualmente se usan todas las librerias que tenian que ser probadas de python

### instalacion:
- descargar el proyecto y llenar las variables de entorno con tu base de datos
- crear entorno virtual e instalar librerias de requerimientos
```
pip install -r requirements.txt
```

### variables de entorno:
crear archivo .env y llenar las variables de entorno con tus datos

ejemplos de variables a crear:
```
host = localhost
user = root
password = 1234
database = DBName

token = 1234
p_k = 2233
port = 5058
```

abre la conexion a la db
```
python3 consultas.py initdb
```

cierra conexion a la db
```
python3 consultas.py dropdb
```

### Crea tabla y procedimientos almacenados
Ahora correremos los comandos para crear la tabla y los procedimientos, tenemos dos opciones
1. opcion uno
Correr los comandos de creacion de forma manual
```
python3 consultas.py --tabla
```
```
python3 consultas.py --procedimiento
```

2. opcion dos
Crear tabla y procedimientos desde el cliente con el comando crear

### Uso del cliente y servidores
Acontinuacion podemos correr los servidores que querramos usar desde la carpeta de servidores
Correr servidor
```
python3 servidor_nombre.py
```
Correr Cliente
```
python3 cliente.py
```
#### Seleciona grupo de servidores
una ves el cliente activo nos pide que seleccionemos el grupo de servidores con el que queremos interactuar   
ejemplo: podemos escribir el grupo **desarrollo*

#### escribe comando a ejecutar desde el cliente
Ahora podemos decir al cliente que operacion ejecutar
