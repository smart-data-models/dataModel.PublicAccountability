from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class MunicipalityInfo(BaseModel):
    addressLocality: Optional[str] = None
    addressRegion: Optional[str] = None
    cityId: Optional[str] = None
    district: Optional[str] = None
    ulbName: Optional[str] = None
    wardNum: Optional[float] = None
    zoneId: Optional[str] = None


class Type6(Enum):
    RevenueCollection = 'RevenueCollection'


class VehicleType(Enum):
    agriculturalVehicle = 'agriculturalVehicle'
    anyVehicle = 'anyVehicle'
    articulatedVehicle = 'articulatedVehicle'
    autorickshaw = 'autorickshaw'
    bicycle = 'bicycle'
    binTrolley = 'binTrolley'
    BRT_mini_bus_ = 'BRT mini bus·'
    BRT_bus = 'BRT bus'
    bus = 'bus'
    car = 'car'
    caravan = 'caravan'
    carOrLightVehicle = 'carOrLightVehicle'
    carWithCaravan = 'carWithCaravan'
    carWithTrailer = 'carWithTrailer'
    cleaningTrolley = 'cleaningTrolley'
    compactor = 'compactor'
    constructionOrMaintenanceVehicle = 'constructionOrMaintenanceVehicle'
    dumper = 'dumper'
    e_moped = 'e-moped'
    e_scooter = 'e-scooter'
    e_motorcycle = 'e-motorcycle'
    fourWheelDrive = 'fourWheelDrive'
    highSidedVehicle = 'highSidedVehicle'
    hopper = 'hopper'
    lorry = 'lorry'
    minibus = 'minibus'
    moped = 'moped'
    motorcycle = 'motorcycle'
    motorcycleWithSideCar = 'motorcycleWithSideCar'
    motorscooter = 'motorscooter'
    sweepingMachine = 'sweepingMachine'
    tanker = 'tanker'
    tempo = 'tempo'
    threeWheeledVehicle = 'threeWheeledVehicle'
    tipper = 'tipper'
    trailer = 'trailer'
    tram = 'tram'
    trolley = 'trolley'
    twoWheeledVehicle = 'twoWheeledVehicle'
    van = 'van'
    vehicleWithoutCatalyticConverter = 'vehicleWithoutCatalyticConverter'
    vehicleWithCaravan = 'vehicleWithCaravan'
    vehicleWithTrailer = 'vehicleWithTrailer'
    withEvenNumberedRegistrationPlates = 'withEvenNumberedRegistrationPlates'
    withOddNumberedRegistrationPlates = 'withOddNumberedRegistrationPlates'
    other = 'other'


class RevenueCollection(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    amountCollected: Optional[float] = Field(
        None,
        description='Amount collected towards the service corresponding to this observation',
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='The date and time of this observation in ISO8601 UTC format'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    enrollmentCertificateRecoveryAmount: Optional[float] = Field(
        None,
        description='Amount collected towards Enrollment Certificate from the establishment on annual basis',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    month: Optional[str] = Field(
        None,
        description="Month corresponding to this observation and is described in MM format, for eg. '05' for the month of May",
    )
    municipalityInfo: Optional[MunicipalityInfo] = Field(
        None, description='Municipality information corresponding to this observation'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    registrationCertificateRecoveryAmount: Optional[float] = Field(
        None,
        description='Amount collected towards Registration Certificate on monthly basis from the establishment per employee',
    )
    revenueCollectionType: Optional[str] = Field(
        None,
        description='Type of source from which the city administration collects the revenue, could be property tax, vehicle registration, party hall booking, community hall booking, auditorium booking etc',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    totalCount: Optional[float] = Field(
        None,
        description='Count of the revenue collection service corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be RevenueCollection'
    )
    vehicleType: Optional[VehicleType] = Field(
        None,
        description='Type of vehicle from the point of view of its structural characteristics. This is different than the vehicle category . The following values defined by _VehicleTypeEnum_ and _VehicleTypeEnum2_, [DATEX 2 version 2.3](http://d2docs.ndwcloud.nu/_static/umlmodel/v2.3/index.htm)',
    )
    vehicleTypeCode: Optional[str] = Field(
        None,
        description="The code for vehicleType corresponding to this observation. For eg.- '1' - MOPED/SCOOTER, '2' - MOTOR CYCLE, '4' - PRIVATE MOTOR CAR/JEEP CAR, '21' - TEMPO, '26' - BUS, etc",
    )
    year: Optional[str] = Field(
        None,
        description="Year corresponding to this observation and is described in YYYY format, for eg. '2020'",
    )
