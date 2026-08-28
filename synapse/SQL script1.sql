CREATE DATABASE SCOPED CREDENTIAL cred_atharv
WITH
    IDENTITY = 'Managed Identity'

--transform--
CREATE EXTERNAL DATA SOURCE source_transform
WITH(
    LOCATION = 'https://deazstoragedatalake.blob.core.windows.net/transform',
    CREDENTIAL = cred_atharv
)

--serve--
CREATE EXTERNAL DATA SOURCE source_serve
WITH(
    LOCATION = 'https://deazstoragedatalake.blob.core.windows.net/serve',
    CREDENTIAL = cred_atharv
)

--external file format--
CREATE EXTERNAL FILE FORMAT format_parquet
WITH(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)

--CREATE EXTERNAL TABLE EXTSALES
CREATE EXTERNAL TABLE gold.extsales
WITH(
    LOCATION = 'extsales',
    DATA_SOURCE = source_serve,
    FILE_FORMAT = format_parquet
)AS SELECT
        *
    FROM
        gold.sales
