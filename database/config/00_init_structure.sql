CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "EmailDomains" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "domain" VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "BankProviders" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "internal_id" VARCHAR(10) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "number" VARCHAR(10) NOT NULL,
    "address" VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS "FemaleNames" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "MaleNames" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "MaleLastNames" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "FemaleLastNames" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR(255) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS "Addresses" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "street" VARCHAR NOT NULL,
    "number" varchar(10) NOT NULL,
    "postal_code" varchar(10),
    "gus_terc" varchar(100) NOT NULL,
    "settlement" varchar(100) NOT NULL
);