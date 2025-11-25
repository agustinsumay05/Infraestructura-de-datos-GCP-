CREATE OR REPLACE TABLE `usm-infra-grupo1.data_mart.ventas_por_producto` AS
SELECT
  p.producto AS producto,
  SUM(f.venta_importe) AS ventas_totales,
  SUM(f.venta_unidades) AS unidades_vendidas
FROM `usm-infra-grupo1.data_warehouse.fact_ventas` AS f
JOIN `usm-infra-grupo1.data_warehouse.dim_producto` AS p
  ON f.sku = p.sku
GROUP BY producto;

