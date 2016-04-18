from troposphere import Parameter, Ref, Template
from troposphere.apigateway import RestApi


t = Template()

swagger = """{
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Troposphere Example",
    "description": "A sample API",
    "termsOfService": "http://example.com/",
    "contact": {
      "name": "Troposphere Team"
    },
    "license": {
      "name": "MIT"
    }
  },
  "host": "foobar.example.com",
  "basePath": "/api",
  "schemes": [
    "http"
  ],
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "paths": {
    "/armadillos": {
      "get": {
        "description": "Returns all armadillos from the system that the user has access to",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "A list of armadillos.",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Armadillo"
              }
            }
          }
        }
      }
    }
  },
  "definitions": {
    "Armadillo": {
      "type": "object",
      "required": [
        "id",
        "name"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      }
    }
  }
}"""

t.add_resource(RestApi(
    "ExampleApi",
    Body=swagger,
))

print(t.to_json())
