<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Recouvrement des recettes    
==================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.PublicAccountability/blob/master/RevenueCollection/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Modèle de données pour les opérations de collecte des recettes de la ville**.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `amountCollected[number]`: Montant perçu pour le service correspondant à cette observation  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `dateObserved[date-time]`: La date et l'heure de cette observation au format ISO8601 UTC  - `description[string]`: Une description de l'article  - `enrollmentCertificateRecoveryAmount[number]`: Montant perçu de l'établissement au titre du certificat d'inscription sur une base annuelle  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `month[string]`: Mois correspondant à cette observation et décrit au format MM, par exemple "05" pour le mois de mai.  - `municipalityInfo[object]`: Informations sur la municipalité correspondant à cette observation  	- `addressLocality`:       
	- `addressRegion`:       
	- `cityId`:       
	- `district`:       
	- `ulbName`:       
	- `wardNum`:       
- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `registrationCertificateRecoveryAmount[number]`: Montant perçu pour le certificat d'enregistrement sur une base mensuelle auprès de l'établissement par employé  - `revenueCollectionType[string]`: Type de source auprès de laquelle l'administration municipale perçoit les recettes : impôt foncier, immatriculation des véhicules, réservation de salles de fêtes, de salles communautaires, d'auditoriums, etc.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `totalCount[number]`: Compte du service de perception des recettes correspondant à cette observation  - `type[string]`: Type d'entité NGSI. Il doit s'agir de RevenueCollection  - `vehicleType[string]`: Type de véhicule du point de vue de ses caractéristiques structurelles. Ce type de véhicule est différent de la catégorie de véhicule. Les valeurs suivantes définies par _VehicleTypeEnum_ et _VehicleTypeEnum2_, [DATEX 2 version 2.3] (http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  - `vehicleTypeCode[string]`: Le code du type de véhicule correspondant à cette observation. Par exemple : '1' - MOPED/SCOOTER, '2' - MOTOCYCLE, '4' - AUTOMOBILE PRIVÉ/JEEP CAR, '21' - TEMPO, '26' - BUS, etc.  - `year[string]`: L'année correspondant à cette observation est décrite au format AAAA, par exemple "2020".  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
RevenueCollection:      
  description: A Data Model for city revenue collection operations.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    amountCollected:      
      description: Amount collected towards the service corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: The date and time of this observation in ISO8601 UTC format      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    enrollmentCertificateRecoveryAmount:      
      description: Amount collected towards Enrollment Certificate from the establishment on annual basis      
      type: number      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    month:      
      description: 'Month corresponding to this observation and is described in MM format, for eg. ''05'' for the month of May'      
      type: string      
      x-ngsi:      
        type: Property      
    municipalityInfo:      
      description: Municipality information corresponding to this observation      
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
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    registrationCertificateRecoveryAmount:      
      description: Amount collected towards Registration Certificate on monthly basis from the establishment per employee      
      type: number      
      x-ngsi:      
        type: Property      
    revenueCollectionType:      
      description: 'Type of source from which the city administration collects the revenue, could be property tax, vehicle registration, party hall booking, community hall booking, auditorium booking etc'      
      type: string      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    totalCount:      
      description: Count of the revenue collection service corresponding to this observation      
      type: number      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity type. It has to be RevenueCollection      
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
        - BRT mini bus·      
        - BRT bus      
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
      description: 'The code for vehicleType corresponding to this observation. For eg.- ''1'' - MOPED/SCOOTER, ''2'' - MOTOR CYCLE, ''4'' - PRIVATE MOTOR CAR/JEEP CAR, ''21'' - TEMPO, ''26'' - BUS, etc'      
      type: string      
      x-ngsi:      
        type: Property      
    year:      
      description: 'Year corresponding to this observation and is described in YYYY format, for eg. ''2020'''      
      type: string      
      x-ngsi:      
        type: Property      
  required: []      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Exemples de charges utiles    
#### RevenueCollection NGSI-v2 key-values Exemple    
Voici un exemple de RevenueCollection au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### RevenueCollection NGSI-v2 normalisé Exemple    
Voici un exemple de RevenueCollection au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:001:rtir:0234",  
  "type": "RevenueCollection",  
  "totalCount": {  
    "type": "Number",  
    "value": 436  
  },  
  "registrationCertificateRecoveryAmount": {  
    "type": "Number",  
    "value": 10400  
  },  
  "enrollmentCertificateRecoveryAmount": {  
    "type": "Number",  
    "value": 8400  
  },  
  "year": {  
    "type": "Text",  
    "value": "2020"  
  },  
  "dateObserved": {  
    "type": "DateTime",  
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
    "type": "Number",  
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
#### RevenueCollection Valeurs clés NGSI-LD Exemple    
Voici un exemple de RevenueCollection au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### RevenueCollection NGSI-LD normalisé Exemple    
Voici un exemple de RevenueCollection au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
