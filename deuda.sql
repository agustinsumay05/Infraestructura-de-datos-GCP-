CREATE OR REPLACE TABLE `usm-infra-grupo1.data_mart.deuda_por_provincia_tneg` AS
SELECT
  c.provincia,
  c.tipo_negocio,
  c.distribuidor,
  COUNT(DISTINCT c.cliente)        AS cantidad_clientes,
  SUM(c.deuda_vencida)             AS deuda_total,
  AVG(c.deuda_vencida)             AS deuda_promedio,
  SUM(CASE WHEN c.deuda_vencida > 0 THEN 1 ELSE 0 END) AS clientes_con_deuda
FROM `usm-infra-grupo1.data_warehouse.dim_cliente` AS c
GROUP BY 1,2,3
ORDER BY deuda_total DESC;
