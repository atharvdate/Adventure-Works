# Architecture

## Data Flow

```
GitHub

↓

Azure Data Factory

↓

Azure Data Lake Storage Gen2
(Bronze)

↓

Azure Databricks
(PySpark)

↓

Azure Data Lake Storage Gen2
(Silver)

↓

Azure Synapse Analytics
(Gold)

↓

Power BI
```

---

## Components

### Source

- AdventureWorks CSV files
- Hosted on GitHub

### Ingestion

- Azure Data Factory
- Static and Dynamic Pipelines
- Lookup
- ForEach
- HTTP Connector

### Bronze Layer

- Azure Data Lake Storage Gen2
- Raw data storage
- No transformations

### Silver Layer

- Azure Databricks
- PySpark transformations
- Cleaned and standardized data

### Gold Layer

- Azure Synapse Analytics
- Reporting-ready tables

### Reporting

- Power BI dashboards
