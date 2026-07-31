# Azure End-to-End Data Engineering Pipeline

End-to-end Azure Data Engineering project implementing the Medallion Architecture (Bronze → Silver → Gold) using Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks, Azure Synapse Analytics, and Power BI.

---

## Architecture

![Architecture](docs/screenshots/09_architecture.png)

---

## Technology Stack

| Service | Purpose |
|----------|---------|
| Azure Data Factory | Data Ingestion |
| Azure Data Lake Storage Gen2 | Storage |
| Azure Databricks | Data Transformation |
| PySpark | Data Processing |
| Azure Synapse Analytics | Data Warehouse |
| Power BI | Reporting |

---

## Repository Structure

```
adf/
    datasets/
    linkedServices/
    pipelines/

config/
    git.json

Data/

databricks/

synapse/

powerbi/

docs/
    architecture.md
    screenshots/

README.md
```

---

## Current Progress

### Bronze Layer

- Resource Group
- Storage Account (ADLS Gen2)
- Azure Data Factory
- HTTP Linked Service
- ADLS Linked Service
- Static Ingestion Pipeline
- Dynamic Ingestion Pipeline
- Parameterized Dataset
- Lookup Activity
- ForEach Activity
- Configuration-driven ingestion using `git.json`

---

## Azure Data Factory Assets

### Pipelines

- GetToRaw
- DynamicGetToRaw

### Datasets

- ds_http
- ds_raw
- ds_git_dynamic
- ds_git_parameters
- ds_sink_dynamic

### Linked Services

- httplinkedservice
- storagedatalake

---

## Roadmap

- Bronze Layer
- Silver Layer (Databricks + PySpark)
- Gold Layer (Synapse)
- Power BI Dashboard
