CREATE OR REPLACE TABLE `usm-infra-grupo1.data_mart.stock_por_producto` AS
SELECT
  p.producto,
  s.distribuidor,
  AVG(s.stock)   AS stock_promedio,
  MAX(s.stock)   AS stock_maximo,
  MIN(s.stock)   AS stock_minimo
FROM `usm-infra-grupo1.data_warehouse.fact_stock` AS s
JOIN `usm-infra-grupo1.data_warehouse.dim_producto` AS p
  ON s.sku = p.sku
GROUP BY 1,2
ORDER BY stock_promedio DESC;
