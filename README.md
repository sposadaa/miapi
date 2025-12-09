# Documentacion API User

Este api permite una adminsitracion basica de usuarios que se almacenan en memoria usando la tecnologia de Pyton y Flask

### Metodos soportados
- **GET**
- **POST**

### Ruta principal API
- **/v1/users**

### GET
> Este metodo te entrega todos los usuarios que estan en memoria.

- **Endpoint**: /v1/users
- **HTTPs Codes Response:**
    - 200 OK
    - 500 internal server error
- **JSON Schema Responde:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schema Response Body",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "age": {
        "type": "number"
      },
      "name": {
        "type": "string"
      }
    },
    "required": [
      "age",
      "name"
    ]
  }
}
```
- **Example Response:**
```json
[
	{
		"age": 30,
		"name": "Sebas"
	},
	{
		"age": 38,
		"name": "Messi"
	}
]
```

### POST
> Inserta un usuario en el modelo de negocio

- **Endpoint**: /v1/users
- **HTTPs Codes Response:**
    - 201 Created
    - 400
        - empty body
        - bad data type
        - incomplete body
    - 500 internal server error

- **JSON Schema Body:**
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Schema body api",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "age"
  ]
}
```
- **Example Response:**
```json
{
	"name": "Messi",
	"age": "38"
}
```
