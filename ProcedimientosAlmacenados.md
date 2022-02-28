## Procedimientos Almacenado
un procedimiento almacenado es un script SQL que puedes guardar y reutilizar,
es util para cuando repites la misma instuccion varias veces

### Crear un procedimiento almacenado
ejemplo de un procedimiento que te dice los numeros de productos segun su estado, 'agotado', 'disponible' etc

```sql
DELIMITER $$
CREATE PROCEDURE obtenerProductosPorEstado(IN nombre_estado VARCHAR(255))
BEGIN
    SELECT * 
    FROM productos
    WHERE estado = nombre_estado;
END$$
DELIMITER
```
LLamar procedimiento
```sql
CALL obtenerProductosPorEstado('disponible')
```
