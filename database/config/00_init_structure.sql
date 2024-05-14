CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS "EmailDomains" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "domain" VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "BankProviders" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR(255) NOT NULL UNIQUE
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

CREATE TABLE IF NOT EXISTS "Streets" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "name" VARCHAR NOT NULL UNIQUE,
    "teryt" VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS "Addresses" (
    "id" uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    "street_id" uuid NOT NULL,
    "number" varchar(10) NOT NULL,
    "postal_code" varchar(10) NOT NULL,
    "gus" varchar(100) NOT NULL,
    "settlement" varchar(100) NOT NULL
);

ALTER TABLE "Addresses" ADD CONSTRAINT "fk_street_id" FOREIGN KEY ("street_id") REFERENCES "Streets"("id");