#  Customer Shopping Behavior Analysis

> **Proyecto de portafolio** | Análisis de datos de comportamiento de compra de 3,900 clientes retail usando Python, SQL y Power BI.

**Autor:** Bianca Merchán Torres
**Institución:** UNI — Análisis de Datos  
**Contacto:** bianca.merchan.t@uni.pe

---

##  Descripción del Proyecto

Este proyecto analiza el comportamiento de compra de **3,900 clientes** de un retailer de moda, con **18 variables** por transacción. El objetivo es identificar patrones de consumo, calcular KPIs de negocio y proponer recomendaciones accionables para incrementar las ventas.

### Preguntas de negocio respondidas
- ¿Qué categorías y temporadas generan más revenue?
- ¿Qué segmento etario es el más valioso?
- ¿Los descuentos realmente incrementan el ticket promedio?
- ¿Cómo se distribuyen los métodos de pago?
- ¿Qué estrategias pueden mejorar la retención de clientes?

---

##  KPIs Principales

| KPI | Valor |
|-----|-------|
|  Ingresos Totales | $233,081 |
|  Ticket Promedio (AOV) | $59.76 |
|  Rating Promedio | 3.75 / 5.0 |
|  Tasa de Suscripción | 27% |
|  Uso de Código Promo | 43% |
|  Clientes analizados | 3,900 |

---

##  Estructura del Repositorio

```
customer-shopping-analysis/
│
├──  data/
│   └── customer_shopping_behavior.csv    # Dataset principal (3,900 filas · 18 col.)
│
├──  notebooks/
│   └── shopping_analysis.py             # Análisis completo en Python
│
├──  sql/
│   └── customer_behavior_queries.sql    # 10 consultas SQL comentadas
│
├──  dashboard/
│   └── index.html                       # Dashboard interactivo (HTML + Chart.js)
│
├──  docs/
│   └── analysis_charts.png             # Gráficos exportados (generado por Python)
│
├── requirements.txt                     # Dependencias Python
├── .gitignore
└── README.md
```

---

##  Herramientas y Tecnologías

| Herramienta | Uso |
|-------------|-----|
| **Python** (pandas, matplotlib, seaborn) | Análisis exploratorio, limpieza, visualizaciones |
| **SQL** (SQLite / PostgreSQL compatible) | Consultas de negocio, KPIs, segmentación |
| **Power BI** | Dashboard ejecutivo interactivo |
| **HTML + Chart.js** | Dashboard web del portafolio |
| **Git / GitHub** | Control de versiones |

---

##  Hallazgos Clave

### Revenue por Categoría
| Categoría | Revenue | Participación |
|-----------|---------|--------------|
| Clothing | $104,264 | 44.7% |
| Accessories | $74,200 | 31.8% |
| Footwear | $36,093 | 15.5% |
| Outerwear | $18,524 | 7.9% |

### Revenue por Temporada
| Temporada | Revenue | Pedidos |
|-----------|---------|---------|
|  Otoño | $60,018 | 975 |
|  Primavera | $58,679 | 999 |
|  Invierno | $58,607 | 971 |
|  Verano | $55,777 | 955 |

### Segmento de Mayor Valor
- El grupo **56–70 años** genera **$65,256** (28% del revenue total) con 1,105 pedidos.

---

##  Recomendaciones de Negocio

1. **Programa de Lealtad** — Solo 27% suscrito. Un programa escalonado puede triplicar la retención.
2. **Campaña Otoño** — Pico estacional de $60K. Aumentar stock y marketing en agosto–octubre.
3. **Replantear Descuentos** — El AOV con descuento ($59.28) ≈ sin descuento ($60.13). Migrar a bundles.
4. **Expandir Footwear y Outerwear** — Menor saturación y ticket competitivo vs. Clothing.
5. **Segmentación 56–70 años** — Email marketing personalizado puede aumentar su frecuencia de compra.

---

##  Cómo Ejecutar el Proyecto

### Requisitos
```bash
pip install -r requirements.txt
```

### Ejecutar el análisis Python
```bash
cd notebooks/
python shopping_analysis.py
```

### Ver el dashboard web
Abrir `dashboard/index.html` directamente en el navegador (no requiere servidor).

### Ejecutar las queries SQL
Las queries en `sql/customer_behavior_queries.sql` son compatibles con:
- SQLite (cargar el CSV como tabla)
- PostgreSQL
- MySQL / MariaDB (con ajustes menores de comillas)

---

##  Dataset

**Fuente:** Customer Shopping Behavior Dataset  
**Registros:** 3,900 transacciones  
**Variables:** 18 columnas

| Variable | Descripción |
|----------|-------------|
| Customer ID | ID único del cliente |
| Age | Edad del cliente |
| Gender | Género |
| Item Purchased | Producto comprado |
| Category | Categoría del producto |
| Purchase Amount (USD) | Monto de la compra |
| Location | Ubicación del cliente |
| Season | Temporada de compra |
| Review Rating | Calificación del cliente (1–5) |
| Subscription Status | ¿Tiene suscripción? |
| Payment Method | Método de pago |
| Discount Applied | ¿Se aplicó descuento? |
| Promo Code Used | ¿Usó código promocional? |
| Previous Purchases | Número de compras anteriores |
| Shipping Type | Tipo de envío |
| Frequency of Purchases | Frecuencia de compra |

---

##  Notas del Proyecto

- El análisis fue realizado de forma independiente como proyecto de portafolio.
- Los datos son públicos y de uso educativo.
- El dashboard web funciona sin instalar dependencias (solo abrir el `.html`).

---

*Proyecto desarrollado por J. Valencia · PUCP · 2024*
