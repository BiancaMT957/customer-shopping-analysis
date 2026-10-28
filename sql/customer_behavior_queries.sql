-- =============================================================
-- Customer Shopping Behavior Analysis — SQL Queries
-- Autor: Bianca Merchán Torres | UNI | Análisis de Datos
-- Dataset: 3,900 transacciones · 18 variables
-- =============================================================


-- ─────────────────────────────────────────────
-- 1. KPI PRINCIPAL: Revenue y métricas globales
-- ─────────────────────────────────────────────
SELECT
    COUNT(*)                              AS total_transacciones,
    ROUND(SUM("Purchase Amount (USD)"), 2)  AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)  AS ticket_promedio,
    ROUND(MIN("Purchase Amount (USD)"), 2)  AS ticket_minimo,
    ROUND(MAX("Purchase Amount (USD)"), 2)  AS ticket_maximo,
    ROUND(AVG("Review Rating"), 2)           AS rating_promedio,
    ROUND(AVG("Previous Purchases"), 1)      AS compras_previas_prom
FROM customer_shopping_behavior;


-- ─────────────────────────────────────────────
-- 2. KPI: Tasa de suscripción y uso de promo
-- ─────────────────────────────────────────────
SELECT
    COUNT(*)                                                    AS total_clientes,
    SUM(CASE WHEN "Subscription Status" = 'Yes' THEN 1 ELSE 0 END) AS suscriptores,
    ROUND(
        SUM(CASE WHEN "Subscription Status" = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1
    )                                                           AS tasa_suscripcion_pct,
    SUM(CASE WHEN "Promo Code Used" = 'Yes' THEN 1 ELSE 0 END)     AS usaron_promo,
    ROUND(
        SUM(CASE WHEN "Promo Code Used" = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1
    )                                                           AS uso_promo_pct
FROM customer_shopping_behavior;


-- ─────────────────────────────────────────────
-- 3. Ventas por categoría de producto
-- ─────────────────────────────────────────────
SELECT
    Category,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(
        SUM("Purchase Amount (USD)") * 100.0 /
        (SELECT SUM("Purchase Amount (USD)") FROM customer_shopping_behavior), 1
    )                                            AS participacion_pct
FROM customer_shopping_behavior
GROUP BY Category
ORDER BY revenue_total DESC;


-- ─────────────────────────────────────────────
-- 4. Ventas por temporada
-- ─────────────────────────────────────────────
SELECT
    Season,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(AVG("Review Rating"), 2)               AS rating_promedio
FROM customer_shopping_behavior
GROUP BY Season
ORDER BY revenue_total DESC;


-- ─────────────────────────────────────────────
-- 5. Top 10 productos más rentables
-- ─────────────────────────────────────────────
SELECT
    "Item Purchased"                            AS producto,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(AVG("Review Rating"), 2)               AS rating_promedio
FROM customer_shopping_behavior
GROUP BY "Item Purchased"
ORDER BY revenue_total DESC
LIMIT 10;


-- ─────────────────────────────────────────────
-- 6. Análisis por grupo etario
-- ─────────────────────────────────────────────
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 25 THEN '18–25'
        WHEN Age BETWEEN 26 AND 35 THEN '26–35'
        WHEN Age BETWEEN 36 AND 45 THEN '36–45'
        WHEN Age BETWEEN 46 AND 55 THEN '46–55'
        ELSE '56–70'
    END                                         AS grupo_edad,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio
FROM customer_shopping_behavior
GROUP BY grupo_edad
ORDER BY MIN(Age);


-- ─────────────────────────────────────────────
-- 7. Métodos de pago más usados
-- ─────────────────────────────────────────────
SELECT
    "Payment Method"                            AS metodo_pago,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM customer_shopping_behavior), 1) AS participacion_pct
FROM customer_shopping_behavior
GROUP BY "Payment Method"
ORDER BY pedidos DESC;


-- ─────────────────────────────────────────────
-- 8. Impacto del descuento en el ticket promedio
-- ─────────────────────────────────────────────
SELECT
    "Discount Applied"                          AS descuento_aplicado,
    COUNT(*)                                    AS pedidos,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total
FROM customer_shopping_behavior
GROUP BY "Discount Applied";


-- ─────────────────────────────────────────────
-- 9. Análisis por género
-- ─────────────────────────────────────────────
SELECT
    Gender,
    COUNT(*)                                    AS pedidos,
    ROUND(SUM("Purchase Amount (USD)"), 0)       AS revenue_total,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(AVG("Review Rating"), 2)               AS rating_promedio,
    ROUND(AVG("Previous Purchases"), 1)          AS compras_previas_prom
FROM customer_shopping_behavior
GROUP BY Gender;


-- ─────────────────────────────────────────────
-- 10. Clientes de alto valor (Heavy Buyers)
--     Definición: >38 compras previas (top 25%)
-- ─────────────────────────────────────────────
SELECT
    COUNT(*)                                    AS clientes_alto_valor,
    ROUND(AVG("Purchase Amount (USD)"), 2)       AS ticket_promedio,
    ROUND(AVG("Review Rating"), 2)               AS rating_promedio,
    ROUND(AVG(Age), 1)                           AS edad_promedio,
    -- Categoría favorita de este segmento
    (
        SELECT Category FROM customer_shopping_behavior
        WHERE "Previous Purchases" > 38
        GROUP BY Category ORDER BY COUNT(*) DESC LIMIT 1
    )                                            AS categoria_favorita
FROM customer_shopping_behavior
WHERE "Previous Purchases" > 38;
