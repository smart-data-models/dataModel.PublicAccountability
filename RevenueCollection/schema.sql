/* (Beta) Export of data model RevenueCollection of the subject dataModel.PublicAccountability for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE RevenueCollection_type AS ENUM ('RevenueCollection');CREATE TYPE vehicleType_type AS ENUM ('agriculturalVehicle', 'anyVehicle', 'articulatedVehicle', 'autorickshaw', 'bicycle', 'binTrolley', 'BRT mini bus·', 'BRT bus', 'bus', 'car', 'caravan', 'carOrLightVehicle', 'carWithCaravan', 'carWithTrailer', 'cleaningTrolley', 'compactor', 'constructionOrMaintenanceVehicle', 'dumper', 'e-moped', 'e-scooter', 'e-motorcycle', 'fourWheelDrive', 'highSidedVehicle', 'hopper', 'lorry', 'minibus', 'moped', 'motorcycle', 'motorcycleWithSideCar', 'motorscooter', 'sweepingMachine', 'tanker', 'tempo', 'threeWheeledVehicle', 'tipper', 'trailer', 'tram', 'trolley', 'twoWheeledVehicle', 'van', 'vehicleWithoutCatalyticConverter', 'vehicleWithCaravan', 'vehicleWithTrailer', 'withEvenNumberedRegistrationPlates', 'withOddNumberedRegistrationPlates', 'other');
CREATE TABLE RevenueCollection (address json, alternateName text, amountCollected text, areaServed text, dataProvider text, dateCreated timestamp, dateModified timestamp, dateObserved timestamp, description text, enrollmentCertificateRecoveryAmount text, id text, location json, month text, municipalityInfo json, name text, owner json, registrationCertificateRecoveryAmount text, revenueCollectionType text, seeAlso json, source text, totalCount text, type RevenueCollection_type, vehicleType vehicleType_type, vehicleTypeCode text, year text);