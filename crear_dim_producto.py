from google.cloud import bigquery

PROJECT_ID = "usm-infra-grupo1"
TARGET_TABLE = f"{PROJECT_ID}.data_warehouse.dim_producto"

def main():
    client = bigquery.Client(project=PROJECT_ID)

    sql = f"""
    CREATE OR REPLACE TABLE `{TARGET_TABLE}` AS
    SELECT
        sku,
        producto,
        unidad
    FROM (
        SELECT
            sku,
            producto,
            unidad,
            ROW_NUMBER() OVER (
                PARTITION BY sku
                ORDER BY fecha_cierre DESC
            ) AS rn
        FROM `{PROJECT_ID}.raw_bikesharing.stock`
    )
    WHERE rn = 1;
    """

    job = client.query(sql)
    job.result()
    print("✅ dim_producto creada (sin stock)")

if __name__ == "__main__":
    main()


