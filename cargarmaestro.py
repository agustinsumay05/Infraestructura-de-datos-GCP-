from google.cloud import bigquery
#ejemplo de como cargar los datos

# TODO : Change to your project id
PROJECT_ID = "usm-infra-grupo1"
DATASET_ID = "raw_bikesharing"
TABLE_NAME = "maestro"
GCS_URI = f"gs://testgp1/data/distribuidor_1/maestro/*.csv"
# This uri for load data from 2018-01-02
#GCS_URI = "gs://{}-data-bucket/from-git/chapter-3/dataset/trips/20180102/*.json".format(project_id)
TABLE_ID = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_NAME}"

client = bigquery.Client(project=PROJECT_ID)


def load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, table_schema):
    job_config = bigquery.LoadJobConfig(
        schema=table_schema,
        source_format=bigquery.SourceFormat.CSV, # Asegúrate que el formato coincide con los archivos
        write_disposition = 'WRITE_APPEND',
        skip_leading_rows=1, # Ignora la primera fila (el encabezado) del CSV
        )

    load_job = client.load_table_from_uri(
        GCS_URI, TABLE_ID, job_config=job_config
    )

    load_job.result()
    table = client.get_table(TABLE_ID)

    print("Loaded {} rows to table {}".format(table.num_rows, TABLE_ID))

bigquery_table_schema = [
    bigquery.SchemaField("sucursal", "STRING"),
    bigquery.SchemaField("cliente", "STRING"),
    bigquery.SchemaField("ciudad", "STRING"),
    bigquery.SchemaField("provincia", "STRING"),
    bigquery.SchemaField("estado", "STRING"),
    bigquery.SchemaField("nombre_cliente", "STRING"),
    bigquery.SchemaField("cuit", "STRING"),
    bigquery.SchemaField("razon_social", "STRING"),
    bigquery.SchemaField("direccion", "STRING"),
    bigquery.SchemaField("dia_visita", "STRING"),
    bigquery.SchemaField("telefono", "STRING"),
    bigquery.SchemaField("fecha_alta", "DATE"),
    bigquery.SchemaField("fecha_baja", "DATE"),
    bigquery.SchemaField("coordenada_latitud", "FLOAT"),
    bigquery.SchemaField("coordenada_longitud", "FLOAT"),
    bigquery.SchemaField("condicion_venta", "STRING"),
    bigquery.SchemaField("deuda_vencida", "FLOAT"),
    bigquery.SchemaField("tipo_negocio", "STRING"),
    bigquery.SchemaField("distribuidor", "STRING"),
]
if __name__ == '__main__':
    load_gcs_to_bigquery_event_data(GCS_URI, TABLE_ID, bigquery_table_schema)