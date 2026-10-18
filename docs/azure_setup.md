# NordicGrid Azure Infrastructure

## Resource Group
- Name: rg-nordicgrid-dev

## Azure Data Lake Storage Gen2
- Region: Norway East (if available)
- Performance: Standard
- Redundancy: LRS
- Hierarchical namespace: Enabled

## Containers
- bronze: Raw electricity data
- silver: Cleaned Delta tables
- gold: Analytics-ready Delta tables

## Security
- Anonymous blob access disabled
- Secure transfer required
- Managed identity authentication planned for ADF

## Next Step
Create Azure Data Factory and ingest Norwegian electricity data.
