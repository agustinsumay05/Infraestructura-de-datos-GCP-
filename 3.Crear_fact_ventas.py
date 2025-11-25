from google.cloud import bigquery

PROJECT_ID = "usm-infra-grupo1"
TARGET_TABLE = f"{PROJECT_ID}.data_warehouse.fact_ventas"

def main():
    client = bigquery.Client(project=PROJECT_ID)

    sql = f"""
    CREATE OR REPLACE TABLE `{TARGET_TABLE}` AS
    SELECT
        sucursal,
        cliente,
        fecha_cierre,          -- lo dejo así porque así está en RAW
        sku,
        venta_unidades,
        venta_importe,
        condicion_venta,
        distribuidor
    FROM `{PROJECT_ID}.raw_bikesharing.ventas`;
    """

    job = client.query(sql)
    job.result()
    print("✅ fact_ventas creada con los nombres originales")

if __name__ == "__main__":
    main()


