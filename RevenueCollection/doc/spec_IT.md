<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: EntrateRiscossione    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.PublicAccountability/blob/master/RevenueCollection/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Un modello di dati per le operazioni di riscossione delle entrate cittadine.**    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nome alternativo per questa voce  - `amountCollected[number]`: Importo riscosso per il servizio corrispondente a questa osservazione  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateObserved[date-time]`: La data e l'ora di questa osservazione nel formato ISO8601 UTC.  - `description[string]`: Descrizione dell'articolo  - `enrollmentCertificateRecoveryAmount[number]`: Importo raccolto per il certificato di iscrizione dallo stabilimento su base annuale  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `month[string]`: Mese corrispondente a questa osservazione e descritto nel formato MM, ad esempio '05' per il mese di maggio.  - `municipalityInfo[object]`: Informazioni sul comune corrispondenti a questa osservazione  	- `addressLocality`:       
	- `addressRegion`:       
	- `cityId`:       
	- `district`:       
	- `ulbName`:       
	- `wardNum`:       
- `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `registrationCertificateRecoveryAmount[number]`: Importo riscosso per la carta di circolazione su base mensile dallo stabilimento per dipendente  - `revenueCollectionType[string]`: Tipo di fonte da cui l'amministrazione comunale raccoglie le entrate, che può essere la tassa di proprietà, l'immatricolazione di veicoli, la prenotazione di sale per feste, sale comunitarie, auditorium, ecc.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `totalCount[number]`: Conteggio del servizio di riscossione delle entrate corrispondente a questa osservazione  - `type[string]`: Tipo di entità NGSI. Deve essere RevenueCollection  - `vehicleType[string]`: Tipo di veicolo dal punto di vista delle sue caratteristiche strutturali. È diverso dalla categoria del veicolo. I seguenti valori definiti da _VehicleTypeEnum_ e _VehicleTypeEnum2_, [DATEX 2 versione 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)  - `vehicleTypeCode[string]`: Il codice del tipo di veicolo corrispondente all'osservazione. Ad esempio: '1' - MOPED/SCOOTER, '2' - MOTOR CYCLE, '4' - PRIVATE MOTOR CAR/JEEP CAR, '21' - TEMPO, '26' - BUS, ecc.  - `year[string]`: Anno corrispondente all'osservazione, descritto nel formato AAAA, ad esempio "2020".  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### RevenueCollection NGSI-v2 valori chiave Esempio    
Ecco un esempio di RevenueCollection in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### RevenueCollection NGSI-v2 normalizzato Esempio    
Ecco un esempio di RevenueCollection in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.    
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
#### RevenueCollection Valori chiave NGSI-LD Esempio    
Ecco un esempio di RevenueCollection in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### Riscossione NGSI-LD normalizzata Esempio    
Ecco un esempio di RevenueCollection in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
