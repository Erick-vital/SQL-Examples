## Pequeno proyecto en python para probar librerias
Actualmente se usan todas las librerias que tenian que ser probadas de python

### instalacion:
- descargar el proyecto y llenar las variables de entorno con tu base de datos
- crear tabla ClienteBanco con los mismos campos que te da un usuario de prueba en mockaro, ya que usaremos a este para sacar los datos

### uso:
puedes usar el proyecto mediante comandos

abre la conexion a la db
```
python3 consultas.py initdb
```

cierra conexion a la db
```
python3 consultas.py dropdb
```

inserta registros mediante arhivo excel descargado de mockaro
```
python3 cli.py --filename "ruta/archivo.xlsx
```

consulta registros insertados en la db
```
python3 consultas.py consultaregistros
```

muestra los nombre de los clientes en orden alfabetico
```
python3 consultas.py ordenarpornombre
```

inserta registros mediante la api de mockaro
```
python3 consultas.py insertardatosdummy
```


