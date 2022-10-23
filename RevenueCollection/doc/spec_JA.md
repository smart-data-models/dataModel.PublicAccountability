<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティRevenueCollection  
=======================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.PublicAccountability/blob/master/RevenueCollection/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**市の歳入徴収業務のためのデータモデル。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `amountCollected[number]`: この観測に対応するサービスに対して収集された金額。  - `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[string]`: ISO8601 UTC フォーマットによる観測日時  - `description[string]`: このアイテムの説明  - `enrollmentCertificateRecoveryAmount[number]`: 事業所から在籍証明書として毎年徴収する金額。  - `id[*]`: エンティティの一意な識別子  - `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `month[string]`: この観測に対応する月で、MM 形式で記述される（例：'05' は 5 月）。  - `municipalityInfo[object]`: この観測に対応する自治体情報。  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `registrationCertificateRecoveryAmount[number]`: 従業員1人当たり事業所から月単位で登録証のために徴収される金額。  - `revenueCollectionType[string]`: 固定資産税、車両登録、パーティー会場の予約、コミュニティホールの予約、講堂の予約などです。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `totalCount[number]`: この観測に対応する収益収集サービスのカウント。  - `type[string]`: NGSI エンティティタイプ。RevenueCollection である必要があります。  - `vehicleType[string]`: 構造的な特性から見た車両の種類。これは、車両カテゴリとは異なる。VehicleTypeEnum_ と _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm) で定義される以下の値である。  - `vehicleTypeCode[string]`: この観測に対応する車両タイプのコード。例：'1' - MOPED/SCOOTER, '2' - MOTOR CYCLE, '4' - PRIVATE MOTOR CAR/JEEP CAR, '21' - TEMPO, '26' - BUS, etc。  - `year[string]`: この観測に対応する年であり、YYYYフォーマットで記述される（例：'2020'）。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
<!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### RevenueCollection NGSI-v2 key-value 例  
以下は、RevenueCollection を JSON-LD 形式で key-value にした例です。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
#### RevenueCollection NGSI-v2 正規化例  
以下は，RevenueCollection を JSON-LD 形式で正規化した例である．これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### RevenueCollection NGSI-LD キー値の例  
ここでは、RevenueCollection を JSON-LD 形式で key-value とした例を示します。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返されます。  
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
#### RevenueCollection NGSI-LD 正規化例  
以下は，RevenueCollection を JSON-LD 形式で正規化した例である．これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
