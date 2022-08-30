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

### Ejemplo de subscripcion
```
POST https://sellingpartnerapi-na.amazon.com/ notifications/v1/subscriptions/BRANDED_ITEM_CONTENT_CHANGE
{
  "payloadVersion":"1.0",
  "destinationId":"3acafc7e-121b-1329-8ae8-1571be663aa2"
}
```
