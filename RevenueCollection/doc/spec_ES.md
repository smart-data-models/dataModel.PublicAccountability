<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: RevenueCollection  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.PublicAccountability/blob/master/RevenueCollection/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un modelo de datos para las operaciones de recaudación de la ciudad.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `amountCollected[number]`: Importe recaudado por el servicio correspondiente a esta observación.  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved[string]`: La fecha y la hora de esta observación en formato ISO8601 UTC  - `description[string]`: Una descripción de este artículo  - `enrollmentCertificateRecoveryAmount[number]`: Importe recaudado por el certificado de matriculación del establecimiento sobre una base anual.  - `id[*]`: Identificador único de la entidad  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `month[string]`: Mes correspondiente a esta observación y se describe en formato MM, por ejemplo, "05" para el mes de mayo.  - `municipalityInfo[object]`: Información del municipio correspondiente a esta observación.  - `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `registrationCertificateRecoveryAmount[number]`: Importe recaudado para el Certificado de Registro sobre una base mensual del establecimiento por empleado.  - `revenueCollectionType[string]`: El tipo de fuente de la que la administración municipal recauda los ingresos puede ser el impuesto sobre bienes inmuebles, la matriculación de vehículos, la reserva de salas de fiesta, la reserva de salas comunitarias, la reserva de auditorios, etc.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `totalCount[number]`: Recuento del servicio de recaudación correspondiente a esta observación.  - `type[string]`: Tipo de entidad NGSI. Tiene que ser RevenueCollection  - `vehicleType[string]`: Tipo de vehículo desde el punto de vista de sus características estructurales. Es diferente de la categoría del vehículo. Los siguientes valores definidos por _VehicleTypeEnum_ y _VehicleTypeEnum2_, [DATEX 2 versión 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  - `vehicleTypeCode[string]`: El código del tipo de vehículo correspondiente a esta observación. Por ejemplo: "1" - MOPED/SCOOTER, "2" - MOTOR CYCLE, "4" - PRIVATE MOTOR CAR/JEEP CAR, "21" - TEMPO, "26" - BUS, etc.  - `year[string]`: Año correspondiente a esta observación y se describe en formato AAAA, por ejemplo, "2020".  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RevenueCollection:    
  description: 'A Data Model for city revenue collection operations.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    amountCollected:    
      description: 'Amount collected towards the service corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    enrollmentCertificateRecoveryAmount:    
      description: 'Amount collected towards Enrollment Certificate from the establishment on annual basis.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &revenuecollection_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    month:    
      description: 'Month corresponding to this observation and is described in MM format, for eg. ''05'' for the month of May.'    
      type: string    
      x-ngsi:    
        type: Property    
    municipalityInfo:    
      description: 'Municipality information corresponding to this observation.'    
      properties:    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        cityId:    
          type: string    
        district:    
          type: string    
        ulbName:    
          type: string    
        wardNum:    
          type: number    
        zoneId:    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *revenuecollection_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    registrationCertificateRecoveryAmount:    
      description: 'Amount collected towards Registration Certificate on monthly basis from the establishment per employee.'    
      type: number    
      x-ngsi:    
        type: Property    
    revenueCollectionType:    
      description: 'Type of source from which the city administration collects the revenue, could be property tax, vehicle registration, party hall booking, community hall booking, auditorium booking etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    totalCount:    
      description: 'Count of the revenue collection service corresponding to this observation.'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be RevenueCollection'    
      enum:    
        - RevenueCollection    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleType:    
      description: 'Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)'    
      enum:    
        - agriculturalVehicle    
        - anyVehicle    
        - articulatedVehicle    
        - autorickshaw    
        - bicycle    
        - binTrolley    
        - 'BRT mini bus·'    
        - 'BRT bus'    
        - bus    
        - car    
        - caravan    
        - carOrLightVehicle    
        - carWithCaravan    
        - carWithTrailer    
        - cleaningTrolley    
        - compactor    
        - constructionOrMaintenanceVehicle    
        - dumper    
        - e-moped    
        - e-scooter    
        - e-motorcycle    
        - fourWheelDrive    
        - highSidedVehicle    
        - hopper    
        - lorry    
        - minibus    
        - moped    
        - motorcycle    
        - motorcycleWithSideCar    
        - motorscooter    
        - sweepingMachine    
        - tanker    
        - tempo    
        - threeWheeledVehicle    
        - tipper    
        - trailer    
        - tram    
        - trolley    
        - twoWheeledVehicle    
        - van    
        - vehicleWithoutCatalyticConverter    
        - vehicleWithCaravan    
        - vehicleWithTrailer    
        - withEvenNumberedRegistrationPlates    
        - withOddNumberedRegistrationPlates    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleTypeCode:    
      description: 'The code for vehicleType corresponding to this observation. For eg.- ''1'' - MOPED/SCOOTER, ''2'' - MOTOR CYCLE, ''4'' - PRIVATE MOTOR CAR/JEEP CAR, ''21'' - TEMPO, ''26'' - BUS, etc.'    
      type: string    
      x-ngsi:    
        type: Property    
    year:    
      description: 'Year corresponding to this observation and is described in YYYY format, for eg. ''2020''.'    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.PublicAccountability/blob/master/RevenueCollection/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.PublicAccountability/RevenueCollection/schema.json    
  x-model-tags: IUDX    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### RevenueCollection NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una RevenueCollection en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:001:rtir:0234",  
  "type": "RevenueCollection",  
  "totalCount": 436,  
  "registrationCertificateRecoveryAmount": 10400,  
  "enrollmentCertificateRecoveryAmount": 8400,  
  "year": "2020",  
  "dateObserved": "2021-11-10T01:16:01Z",  
  "month": "02",  
  "revenueCollectionType": "Property Tax",  
  "vehicleTypeCode": "2",  
  "amountCollected": 20400,  
  "vehicleType": "motorcycle",  
  "municipalityInfo": {  
    "district": "Bangalore Urban",  
    "ulbName": "BMC",  
    "cityId": "23",  
    "addressRegion": "Karnataka",  
    "addressLocality": "Bangalore",  
    "zoneId": "2",  
    "wardNum": 4  
  }  
}  
```  
</details>  
#### RevenueCollection NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de una RevenueCollection en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:001:rtir:0234",  
  "type": "RevenueCollection",  
  "totalCount": {  
    "type": "number",  
    "value": 436  
  },  
  "registrationCertificateRecoveryAmount": {  
    "type": "number",  
    "value": 10400  
  },  
  "enrollmentCertificateRecoveryAmount": {  
    "type": "number",  
    "value": 8400  
  },  
  "year": {  
    "type": "Text",  
    "value": "2020"  
  },  
  "dateObserved": {  
    "type": "Date-Time",  
    "value": "2021-11-10T01:16:01Z"  
  },  
  "month": {  
    "type": "Text",  
    "value": "02"  
  },  
  "revenueCollectionType": {  
    "type": "Text",  
    "value": "Property Tax"  
  },  
  "vehicleTypeCode": {  
    "type": "Text",  
    "value": "2"  
  },  
  "amountCollected": {  
    "type": "number",  
    "value": 20400  
  },  
  "vehicleType": {  
    "type": "Text",  
    "value": "motorcycle"  
  },  
  "municipalityInfo": {  
    "type": "StructuredValue",  
    "value": {  
      "district": "Bangalore Urban",  
      "ulbName": "BMC",  
      "cityId": "23",  
      "addressRegion": "Karnataka",  
      "addressLocality": "Bangalore",  
      "zoneId": "2",  
      "wardNum": 4  
    }  
  }  
}  
```  
</details>  
#### RevenueCollection NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una RevenueCollection en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:001:rtir:0234",  
    "@context": [  
        "iudx:RevenueCollection",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PublicAccountability/master/context.jsonld"  
    ],  
    "type": "RevenueCollection",  
    "totalCount": 436,  
    "registrationCertificateRecoveryAmount": 10400,  
    "enrollmentCertificateRecoveryAmount": 8400,  
    "year": "2020",  
    "dateObserved": "2021-11-10T01:16:01Z",  
    "month": "02",  
    "revenueCollectionType": "Property Tax",  
    "vehicleTypeCode": "2",  
    "amountCollected": 20400,  
    "vehicleType": "motorcycle",  
    "municipalityInfo": {  
        "district": "Bangalore Urban",  
        "ulbName": "BMC",  
        "cityId": "23",  
        "addressRegion": "Karnataka",  
        "addressLocality": "Bangalore",  
        "zoneId": "2",  
        "wardNum": 4  
    }  
}  
```  
</details>  
#### RevenueCollection NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una RevenueCollection en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:001:rtir:0234",  
    "type": "RevenueCollection",  
    "totalCount": {  
        "type": "Property",  
        "value": 436  
    },  
    "registrationCertificateRecoveryAmount": {  
        "type": "Property",  
        "value": 10400  
    },  
    "enrollmentCertificateRecoveryAmount": {  
        "type": "Property",  
        "value": 8400  
    },  
    "year": {  
        "type": "Property",  
        "value": "2020"  
    },  
    "dateObserved": {  
        "type": "Property",  
        "value": {  
            "@type": "date-time",  
            "@value": "2021-11-10T01:16:01Z"  
        }  
    },  
    "month": {  
        "type": "Property",  
        "value": "02"  
    },  
    "revenueCollectionType": {  
        "type": "Property",  
        "value": "Property Tax"  
    },  
    "vehicleTypeCode": {  
        "type": "Property",  
        "value": "2"  
    },  
    "amountCollected": {  
        "type": "Property",  
        "value": 20400  
    },  
    "vehicleType": {  
        "type": "Property",  
        "value": "motorcycle"  
    },  
    "municipalityInfo": {  
        "type": "Property",  
        "value": {  
            "district": "Bangalore Urban",  
            "ulbName": "BMC",  
            "cityId": "23",  
            "addressRegion": "Karnataka",  
            "addressLocality": "Bangalore",  
            "zoneId": "2",  
            "wardNum": 4  
        }  
    },  
    "@context": [  
        "iudx:RevenueCollection",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/master/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.PublicAccountability/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
