CREATE OR REPLACE TABLE `usm-infra-grupo1.data_mart.ventas_prov_tneg_mes` AS
SELECT
  c.provincia,
  c.tipo_negocio,
  DATE_TRUNC(f.fecha_cierre, MONTH) AS mes,
  SUM(f.venta_importe) AS importe_total,
  SUM(f.venta_unidades) AS unidades_total,
  AVG(f.venta_importe) AS ticket_promedio,
  COUNT(*) AS n_transacciones
FROM `usm-infra-grupo1.data_warehouse.fact_ventas` AS f
JOIN `usm-infra-grupo1.data_warehouse.dim_cliente` AS c
  ON f.cliente = c.cliente
GROUP BY 1,2,3;
