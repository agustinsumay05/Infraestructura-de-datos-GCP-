from google.cloud import bigquery

PROJECT_ID = "usm-infra-grupo1"
TARGET_TABLE = f"{PROJECT_ID}.data_warehouse.dim_tiempo"

def main():
    client = bigquery.Client(project=PROJECT_ID)

    sql = f"""
    CREATE OR REPLACE TABLE `{TARGET_TABLE}` AS
    WITH fechas_ventas AS (
        SELECT DISTINCT fecha_cierre AS fecha
        FROM `{PROJECT_ID}.raw_bikesharing.ventas`
        WHERE fecha_cierre IS NOT NULL
    ),
    fechas_stock AS (
        SELECT DISTINCT fecha_cierre AS fecha
        FROM `{PROJECT_ID}.raw_bikesharing.stock`
        WHERE fecha_cierre IS NOT NULL
    ),
    todas_las_fechas AS (
        SELECT fecha FROM fechas_ventas
        UNION DISTINCT
        SELECT fecha FROM fechas_stock
    )
    SELECT
        fecha AS fecha,
        EXTRACT(YEAR  FROM fecha) AS anio,
        EXTRACT(MONTH FROM fecha) AS mes,
        EXTRACT(DAY   FROM fecha) AS dia,
        FORMAT_DATE('%Y-%m', fecha) AS anio_mes
    FROM todas_las_fechas;
    """

    job = client.query(sql)
    job.result()
    print("✅ dim_tiempo creada / reemplazada")

if __name__ == "__main__":
    main()



