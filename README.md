# 🚀 Infraestructura Analítica en Google Cloud + Dashboard en Looker Studio

Este proyecto implementa una solución completa de ingeniería y análisis de datos utilizando **Google Cloud Platform**, integrando información proveniente de **cinco distribuidores** con datos de **ventas, stock, clientes y deuda**.

El objetivo es centralizar datos dispersos, transformarlos mediante un modelo analítico y construir visualizaciones que permitan responder preguntas clave del negocio.

---

# 📌 Objetivos del Proyecto

- Integrar datos provenientes de múltiples distribuidores en distintos formatos.
- Unificar la información en un **Data Lake → Data Warehouse → Data Mart** dentro de GCP.
- Crear un **modelo dimensional (esquema estrella)** para analizar patrones de compras y deuda.
- Construir un **dashboard ejecutivo** para validar hipótesis comerciales y financieras.

---

# 🧱 Arquitectura del Proyecto


### **🔹 Cloud Storage**
- Ingesta y almacenamiento de archivos de:
  - Ventas
  - Stock
  - Maestro de Clientes

### **🔹 BigQuery – Data Raw**
Estandarización inicial:
- Limpieza de fechas
- Normalización de campos
- Conversión de tipos

### **🔹 BigQuery – Data Warehouse (Modelo Estrella)**

Tablas de **dimensión**:
- `dim_cliente`
- `dim_producto`
- `dim_tiempo`

Tablas de **hechos**:
- `fact_ventas`
- `fact_stock`

---

# ⭐ Modelo Estrella

El Data Warehouse fue modelado utilizando un **esquema estrella**, separando:

- **Hechos:** métricas numéricas (ventas, unidades, stock)
- **Dimensiones:** atributos descriptivos (cliente, producto, fecha)

Esto facilita:
- consultas rápidas,
- joins simples
- integración con herramientas BI.

(Agregar imagen del modelo si querés)

---

# 📊 Data Mart

Desde el DW se construyeron tablas agregadas para análisis:

### `ventas_prov_tneg_mes`
- Compras por tipo de negocio
- Compras por provincia
- Compras por mes

### `deuda_por_provincia_tneg`
- Deuda vencida agrupada por tipo de negocio y provincia

### `ventas_por_producto`
- Unidades totales por SKU y distribuidor


---

# 🧪 Tecnologías Utilizadas

- **Google Cloud Storage**
- **BigQuery**
- **Python** (`google-cloud-bigquery`)
- **SQL**
- **Looker Studio**
- **Colab / Python ETL**

---


# 📚 Conclusiones

- Se integraron datos de cinco distribuidores.
- Se estandarizó y centralizó la información en BigQuery.
- Se construyó un Data Warehouse robusto bajo un **esquema estrella**.
- Se creó un Data Mart optimizado para análisis comercial.
- El dashboard permitió **refutar la hipótesis inicial**:  
  > *Los minoristas NO son quienes más compran ni quienes más deuda acumulan.*

---

# 👨‍💻 Autor

**Agustín Sumay**  
*Estudiante de Ciencia de Datos – UNSAM*  


