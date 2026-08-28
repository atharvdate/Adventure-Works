# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC # Transformation Layer Script

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data access using application

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.auth.type.deazstoragedatalake.dfs.core.windows.net",
    "OAuth"
)

spark.conf.set(
    "fs.azure.account.oauth.provider.type.deazstoragedatalake.dfs.core.windows.net",
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)

spark.conf.set(
    "fs.azure.account.oauth2.client.id.deazstoragedatalake.dfs.core.windows.net",
    "40ab6e3e-573a-4078-841b-108b3360f002"
)

spark.conf.set(
    "fs.azure.account.oauth2.client.secret.deazstoragedatalake.dfs.core.windows.net",
    dbutils.secrets.get(
        scope="azure-secrets",
        key="client-secret"
    )
)

spark.conf.set(
    "fs.azure.account.oauth2.client.endpoint.deazstoragedatalake.dfs.core.windows.net",
    "https://login.microsoftonline.com/4f8dd70b-2405-472a-9949-9ecd8f71a243/oauth2/token"
)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Loading

# COMMAND ----------

# MAGIC %md
# MAGIC #### Reading data

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.deazstoragedatalake.dfs.core.windows.net",
    dbutils.secrets.get(
        scope="azure-secrets",
        key="storage-account-key"
    )
)

# COMMAND ----------

df_cal = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_cus = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_prod = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_sales = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_terr = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

df_prodcat = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/Product_Categories')

# COMMAND ----------

df_prodsubcat = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/Product_Subcategories')

# COMMAND ----------

df_ret = spark.read.format('csv') \
    .option("header", True) \
    .option("inferSchema", True) \
    .load('abfss://raw@deazstoragedatalake.dfs.core.windows.net/Returns')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Transformations

# COMMAND ----------

# MAGIC %md
# MAGIC #### Calendar

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cal = df_cal.withColumn('Month', month(col('Date'))) \
    .withColumn('Year', year(col('Date')))

df_cal.display()

# COMMAND ----------

df_cal.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Calendar"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Customers

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus.withColumn(
    "fullName",
    concat(
        col('Prefix'),
        lit(' '),
        col('FirstName'),
        lit(' '),
        col('LastName')
    )
).display()

# COMMAND ----------

df_cus = df_cus.withColumn(
    'fullName',
    concat_ws(
        ' ',
        col('Prefix'),
        col('FirstName'),
        col('LastName')
    )
)

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Customers"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Product Sub Categories

# COMMAND ----------

df_prodsubcat.display()

# COMMAND ----------

df_prodsubcat.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/Product_Subcategories"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Products

# COMMAND ----------

df_prod.display()

# COMMAND ----------

df_prod = df_prod.withColumn(
    'ProductSKU',
    split(col('ProductSKU'), '-')[0]
).withColumn(
    'ProductName',
    split(col('ProductName'), ' ')[0]
)

# COMMAND ----------

df_prod.display()

# COMMAND ----------

df_prod.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Products"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/Returns"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Territories

# COMMAND ----------

df_terr.display()

# COMMAND ----------

df_terr.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Territories"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn(
    'StockDate',
    to_timestamp('StockDate')
)

# COMMAND ----------

df_sales = df_sales.withColumn(
    'OrderNumber',
    regexp_replace(col('OrderNumber'), 'S', 'T')
)

# COMMAND ----------

df_sales = df_sales.withColumn(
    'multiply',
    col('OrderLineItem') * col('OrderQuantity')
)

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('parquet') \
    .mode('append') \
    .option(
        "path",
        "abfss://transform@deazstoragedatalake.dfs.core.windows.net/AdventureWorks_Sales"
    ) \
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales Analysis

# COMMAND ----------

df_sales.groupBy('OrderDate') \
    .agg(
        count('OrderNumber').alias('total_order')
    ) \
    .display()

# COMMAND ----------

df_prodcat.display()

# COMMAND ----------

df_terr.display()