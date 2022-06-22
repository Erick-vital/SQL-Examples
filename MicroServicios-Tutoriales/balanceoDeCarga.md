## Balanceo de Carga

Cuando un servidor de Internet se vuelve lento debido a la congestión de información podemos escalar de forma vertical
ampliando la memoria, pero si necesitamos un escalado dinamico deacuerdo a las necesidades de las peticiones podemos usar un
balanceo de carga

![how-does-load-balancing-work](https://user-images.githubusercontent.com/71853038/175054770-adfdcc81-2d4e-4c9f-b3f1-0861a8d7aa60.png)

### Que es el balanceo de carga 
De forma sencilla, el balanceo de carga es la manera en que las peticiones de Internet son distribuídas sobre una fila de servidores.   
El balance de carga se mantiene gracias a un algoritmo que divide de la manera más equitativa posible el trabajo, para evitar los así denominados cuellos de botella

### Como funciona el balanceo de carga
El balanceador clona el servidor que esta recibiendo la peticiones ademas distribuye las peticiones del cliente entre estos dos servidores, sin enmbarga ambos servidores
el original y el clonado ambos consumen de la misma base de datos, las peticiones se distribuyen entre los servidores usando un porxy inverso

### Balanceo de Carga con traefik
Traefik está entre Reverse Proxy y Load Balancer, es fácil de utilizar y es dinámico

Traefik el cual ejercerá de nuestro routing hacia los distintos “backend” que utilizaremos. Es decir, conectaremos una série de “Frontends” con “Backends” mediante puntos de acceso (rutas)

#### Entry points
![entrypoints](https://user-images.githubusercontent.com/71853038/175059004-211c69ef-9434-4596-93e5-4cf3ea28c516.png)
Por ejemplo podemos identificar algunos Entrypoints como:
*  Puertos (80, 443 …),
*  SSL (Certificados, claves, autenticación,…),
*  Redirección a otro punto de entrada (redireccionar HTTP a HTTPS).

#### Routers
Un enrutador se encarga de conectar las solicitudes entrantes a los servicios que pueden manejarlas. En el proceso, los enrutadores pueden usar piezas de middleware para actualizar la solicitud o actuar antes de reenviar la solicitud al servicio.
![routers](https://user-images.githubusercontent.com/71853038/175059554-b6c4c5a2-7844-4359-aa6a-c2382140820c.png)


