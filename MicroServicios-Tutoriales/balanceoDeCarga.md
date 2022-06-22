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
