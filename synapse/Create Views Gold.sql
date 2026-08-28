--Calendar--
CREATE VIEW gold.calendar
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/AdventureWorks_Calendar/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Customers--
CREATE VIEW gold.customers
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/AdventureWorks_Customers/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Products--
CREATE VIEW gold.products
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/AdventureWorks_Products/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Sales--
CREATE VIEW gold.sales
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/AdventureWorks_Sales/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Territories--
CREATE VIEW gold.territories
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/AdventureWorks_Territories/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Product Subcategories--
CREATE VIEW gold.prodsubcat
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/Product_Subcategories/',
            FORMAT = 'PARQUET'
        )AS QUER1;

--Returns--
CREATE VIEW gold.returns
AS SELECT
        *
    FROM
        OPENROWSET(
            BULK 'https://deazstoragedatalake.blob.core.windows.net/transform/Returns/',
            FORMAT = 'PARQUET'
        )AS QUER1;