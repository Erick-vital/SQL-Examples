## SUBSCRIPCION A WEBHOOK SHOPIFY
Como crear una nueva susbcripcion

### Argumentos
- topic: el tipo de evento que activa el webhook
- webhookSubscription: especifica los campos de entrada de la subscripcion

### Campos de entrada (WebhookSubscriptionInput fields)

- callbackurl: url donde el webhook envia el post al ocurrir el evento
- format: el formato de como la data sera enviada
- includefield: la lista de campos que sera incluido en el webhook
- metafieldNamespaces: la metadata que sera incluida en la subscripcion
- privateMetafieldNamespaces: metadata privada a ser incluida en la subscripcion

### Ejemplo
ejemplo de subscripcion al webhook construido con curl    
con el topic 'APP_UNISTALLED'

```
curl -X POST \
https://your-development-store.myshopify.com/admin/api/2022-04/graphql.json \
-H 'Content-Type: application/json' \
-H 'X-Shopify-Access-Token: {access_token}' \
-d '{
"query": "mutation webhookSubscriptionCreate($topic: WebhookSubscriptionTopic!, $webhookSubscription: WebhookSubscriptionInput!) { webhookSubscriptionCreate(topic: $topic, webhookSubscription: $webhookSubscription) { webhookSubscription { id topic format endpoint { __typename ... on WebhookHttpEndpoint { callbackUrl } } } } }",
 "variables": {
    "topic": "APP_UNINSTALLED",
    "webhookSubscription": {
      "callbackUrl": "https://example.org/endpoint",
      "format": "JSON"
    }
  }
}'
```



## SUBSCRIPCION A WEBHOOK AMAZON
una vez creado el evento y el destino esta es la forma de crear una subscripcion a una notificacion

**Nota**: solamente una subscripcion por aplicacion es permitido por
cada region y vendedor

### Parametros del path
- notificationType: el tipo de notificacion a la quieres susbscribir, para saber
los tipos de notificacion haz click [aqui](https://developer-docs.amazon.com/sp-api/docs/notifications-api-v1-use-case-guide#notificationtype)

### Parametros del body
- payloadVersion: la version del payload usado en la notificacion
- destinationId: el identificador de destino donde las notificaciones seran enviadas

### Ejemplo
```
POST https://sellingpartnerapi-na.amazon.com/ notifications/v1/subscriptions/BRANDED_ITEM_CONTENT_CHANGE
{
  "payloadVersion":"1.0",
  "destinationId":"3acafc7e-121b-1329-8ae8-1571be663aa2"
}
```

## SUBSCRIPCION A WEBHOOK MercadoLibre
Para comenzar a recibir notificaciones, debes realizar el login e ingresar a Mis aplicaciones, donde creaste tu aplicación por primera vez, editas detalles y especificas los topics que recibirás. Si aún no has creado tu aplicación, puedes hacerlo ahora. 

<img width="604" alt="255590940211-Captura-de-Tela-2022-05-02-a-s-15 26 17" src="https://user-images.githubusercontent.com/71853038/187470448-7df2c1e8-6a07-4abe-96ec-d52e4ac917c9.png">

**Callback URL** de notificaciones: configura el URL público del dominio donde quieres recibir notificaciones para los diferentes topics. Por ejemplo: “http://myshoes-app.com/callbacks”.   
**Topics**: selecciona entre diferentes topics para recibir sus notificaciones.

### Topics disponibles
- items: recibirás notificaciones de cualquier cambio en un artículo que publicaste.
- payments: recibirás notificaciones cuando se crea un pago en una orden o el estado del mismo cambia.
- messages: recibirás notificaciones de los mensajes nuevos que se generen teniendo como destinatario su user_id.
- orders_v2: recibirás notificaciones desde la creación y cambios realizados en alguna de tus ventas confirmadas (recomendable).
- shipments: recibirás notificaciones desde la creación y cambios realizados en los envíos (shippings) de tus ventas confirmadas.
- orders feedback: recibirás notificaciones desde la creación y cambios realizados en feedbacks de tus ventas confirmadas.
- quotations: recibirás notificaciones referidas a cotizaciones que sucedan en las publicaciones (aplica solo para integración de inmuebles en Mercado Libre Chile).
- invoices: recibirás notificaciones relacionadas a invoices (notas fiscales) generadas mediante la facturación automática der Mercado Libre (aplica solamente a quien trabaja con el facturador de Mercado Envio Full *Solo disponible en Brasil).
- claims: recibirás notificaciones relacionadas a reclamos que sean hechos por las ventas (trabajar con reclamos)
- item competition: recibirás notificaciones cuando las publicaciones de catálogo que se encuentran compitiendo cambian de estado. Tanto de competidor a ganador y viceversa.
- stock fulfillment: recibirás notificaciones con el detalle de una operación en particular ejecutada sobre el stock que el seller tiene almacenado en los depósitos de FBM.
- best price eligible: recibirás notificaciones cuando se crea una nueva promoción, se modifica el monto del target price y cuando un ítem que está compitiendo deja de ser el ganador del destaque especial en catálogo.
- items prices: recibirás notificaciones del item_id cada vez que el precio se crea, se actualiza o se borra.
- public candidates: Recibirá notificaciones cada vez que un ítem sea invitado a participar en una promoción.
- public offers: recibirás notificaciones cuando se crea o cambia de estado una oferta en un ítem.

