## Triggers 
Los triggers o disparadores con scripts sql que se ejecutan cuando ciertas acciones se producen, estas acciones pueden ser
 (tanto DML como DDL) (inserciones, modificaciones, borrados, creación de tablas, etc).
 
 ### Crear un trigger
 
 1. Primero declaramos un delimitador y usamos la sentencia CREATE
 2. Especificamos el evento o accion que ejecutara el trigger, en esta caso sera un INSERT
 3. Por último mediante el comando BEGIN y END indicamos las líneas de código SQL que ejecutará el TRIGGER:

Ejemplo:
```sql

    DELIMITER $$
    CREATE TRIGGER trigger_historico
    AFTER INSERT ON usuario
    FOR EACH ROW
    BEGIN
    //líneas de código SQL que se ejecutarán
    END; $$


```
