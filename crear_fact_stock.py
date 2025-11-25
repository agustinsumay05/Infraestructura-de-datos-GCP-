from google.cloud import bigquery

PROJECT_ID = "usm-infra-grupo1"
TARGET_TABLE = f"{PROJECT_ID}.data_warehouse.fact_stock"

def main():
    client = bigquery.Client(project=PROJECT_ID)

    sql = f"""
    CREATE OR REPLACE TABLE `{TARGET_TABLE}` AS
    SELECT
        sucursal,
        distribuidor,
        fecha_cierre,
        sku,
        stock,
        unidad
    FROM `{PROJECT_ID}.raw_bikesharing.stock`;
    """

    job = client.query(sql)
    job.result()
    print("✅ fact_stock creada")

if __name__ == "__main__":
    main()
