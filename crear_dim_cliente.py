from google.cloud import bigquery

PROJECT_ID = "usm-infra-grupo1"
TARGET_TABLE = f"{PROJECT_ID}.data_warehouse.dim_cliente"

def main():
    client = bigquery.Client(project=PROJECT_ID)

    sql = f"""
    CREATE OR REPLACE TABLE `{TARGET_TABLE}` AS
    SELECT
        cliente,               -- PK de la dimensión
        sucursal,
        ciudad,
        provincia,
        estado,
        nombre_cliente,
        cuit,
        razon_social,
        direccion,
        dia_visita,
        telefono,
        fecha_alta,
        fecha_baja,
        coordenada_latitud,
        coordenada_longitud,
        condicion_venta,
        deuda_vencida,
        tipo_negocio,
        distribuidor
    FROM (
        SELECT
            *,
            ROW_NUMBER() OVER (
                PARTITION BY cliente
                ORDER BY fecha_alta DESC
            ) AS rn
        FROM `{PROJECT_ID}.raw_bikesharing.maestro`
    )
    WHERE rn = 1;
    """

    job = client.query(sql)
    job.result()
    print("✅ dim_cliente creada con las columnas de raw_bikesharing.maestro")

if __name__ == "__main__":
    main()



