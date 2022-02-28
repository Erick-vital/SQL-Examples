## Integridad Referencial
 La integridad referencial es un sistema de reglas que utilizan la mayoría de las bases de datos relacionales para asegurarse que los registros de tablas 
 relacionadas son válidos y que no se borren o cambien datos relacionados de forma accidental produciendo errores de integridad.

Primero repasemos un poco los tipos de relaciones. 

1. Relación Uno a Uno: Cuando un registro de una tabla sólo puede estar relacionado con un único registro de la otra tabla y viceversa. 
2.  Relación Uno a Varios: Cuando un registro de una tabla (tabla secundaria) sólo puede estar relacionado con un único registro de la otra tabla (tabla principal) y un registro de la tabla principal puede tener más de un registro relacionado en la tabla secundaria
3.  Relación Varios a Varios: Cuando un registro de una tabla puede estar relacionado con más de un registro de la otra tabla y viceversa. En este caso las dos tablas no pueden estar relacionadas directamente, se tiene que añadir una tabla entre las dos que incluya los pares de valores relacionados entre sí.

### Cuando se activa la integridad referencial
La integridad referencial se activa en cuanto creamos una clave foránea y a partir de ese momento se comprueba cada vez que se modifiquen 
datos que puedan alterarla.

- **Cuando insertamos una nueva fila en la tabla secundaria y el valor de la clave foránea no existe en la tabla principal.** 

- **Cuando modificamos el valor de la clave principal de un registro que tiene 'hijos'**

- **Cuando modificamos el valor de la clave foránea, el nuevo valor debe existir en la tabla principal.**

- **Cuando queremos borrar una fila de la tabla principal y ese registro tiene 'hijos'**

### Actualización y borrado en cascada

- **Actualizar registros en cascada** cuando se cambie un valor del campo clave de la tabla principal, automáticamente cambiará el valor de la clave foránea 
de los registros relacionados en la tabla secundaria.

- **Eliminar registros en cascada**  cuando se elimina un registro de la tabla principal automáticamente se 
borran también los registros relacionados en la tabla secundaria. 
