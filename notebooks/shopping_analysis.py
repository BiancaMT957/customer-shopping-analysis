"""
Customer Shopping Behavior Analysis
=====================================
Autor  : Bianca Merchán Torres
Email  : bianca.merchan.t@uni.pe
Curso  : Análisis de Datos — Portafolio
Dataset: 3,900 clientes · 18 variables

Objetivo: Explorar patrones de comportamiento de compra,
calcular KPIs clave e identificar segmentos de clientes
para orientar estrategias de negocio.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# ── Estilo global ──────────────────────────────────────────
plt.rcParams.update({
    "figure.facecolor": "#F3F4F8",
    "axes.facecolor":   "#FFFFFF",
    "axes.edgecolor":   "#E0E3EB",
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.grid":        True,
    "grid.color":       "#E0E3EB",
    "grid.linewidth":   0.8,
    "font.family":      "DejaVu Sans",
    "font.size":        11,
    "axes.titlesize":   13,
    "axes.titleweight": "bold",
    "axes.labelsize":   11,
    "xtick.labelsize":  10,
    "ytick.labelsize":  10,
})

PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#6250d6"]

# ══════════════════════════════════════════════════════════
# 1. CARGA Y LIMPIEZA DE DATOS
# ══════════════════════════════════════════════════════════
print("=" * 60)
print("  CUSTOMER SHOPPING BEHAVIOR ANALYSIS")
print("  J. Valencia · PUCP")
print("=" * 60)

df = pd.read_csv("../data/customer_shopping_behavior.csv")

print(f"\n📦 Dataset cargado: {df.shape[0]:,} filas · {df.shape[1]} columnas")
print(f"   Valores nulos: {df.isnull().sum().sum()} total")
print(f"   Columnas: {list(df.columns)}\n")

# Crear grupo de edad
df["Age Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 71],
    labels=["18–25", "26–35", "36–45", "46–55", "56–70"]
)

# ══════════════════════════════════════════════════════════
# 2. KPIs CLAVE
# ══════════════════════════════════════════════════════════
print("─" * 60)
print("  KPIs PRINCIPALES")
print("─" * 60)

total_revenue     = df["Purchase Amount (USD)"].sum()
aov               = df["Purchase Amount (USD)"].mean()
avg_rating        = df["Review Rating"].mean()
subscription_rate = (df["Subscription Status"] == "Yes").mean() * 100
promo_rate        = (df["Promo Code Used"] == "Yes").mean() * 100
avg_prev_purch    = df["Previous Purchases"].mean()

print(f"  💰 Ingresos Totales  : ${total_revenue:>12,.2f}")
print(f"  🛒 Ticket Promedio   : ${aov:>12.2f}")
print(f"  ⭐ Rating Promedio   :  {avg_rating:>11.2f} / 5.0")
print(f"  🔁 Tasa Suscripción  :  {subscription_rate:>10.1f}%")
print(f"  🏷️ Uso Código Promo  :  {promo_rate:>10.1f}%")
print(f"  📦 Compras Previas   :  {avg_prev_purch:>10.1f} (prom.)")
print()

# ══════════════════════════════════════════════════════════
# 3. ANÁLISIS POR CATEGORÍA
# ══════════════════════════════════════════════════════════
cat_stats = (
    df.groupby("Category")["Purchase Amount (USD)"]
    .agg(pedidos="count", revenue="sum", ticket_prom="mean")
    .sort_values("revenue", ascending=False)
)
cat_stats["participacion_%"] = cat_stats["revenue"] / cat_stats["revenue"].sum() * 100

print("─" * 60)
print("  VENTAS POR CATEGORÍA")
print("─" * 60)
print(cat_stats.round(2).to_string())
print()

# ══════════════════════════════════════════════════════════
# 4. ANÁLISIS POR TEMPORADA
# ══════════════════════════════════════════════════════════
season_stats = (
    df.groupby("Season")["Purchase Amount (USD)"]
    .agg(pedidos="count", revenue="sum", ticket_prom="mean")
    .sort_values("revenue", ascending=False)
)

print("─" * 60)
print("  VENTAS POR TEMPORADA")
print("─" * 60)
print(season_stats.round(2).to_string())
print()

# ══════════════════════════════════════════════════════════
# 5. TOP 10 PRODUCTOS
# ══════════════════════════════════════════════════════════
top_products = (
    df.groupby("Item Purchased")["Purchase Amount (USD)"]
    .agg(pedidos="count", revenue="sum")
    .sort_values("revenue", ascending=False)
    .head(10)
)

print("─" * 60)
print("  TOP 10 PRODUCTOS POR REVENUE")
print("─" * 60)
print(top_products.to_string())
print()

# ══════════════════════════════════════════════════════════
# 6. IMPACTO DEL DESCUENTO
# ══════════════════════════════════════════════════════════
discount_impact = df.groupby("Discount Applied")["Purchase Amount (USD)"].mean()
print("─" * 60)
print("  IMPACTO DEL DESCUENTO EN TICKET PROMEDIO")
print("─" * 60)
print(discount_impact.round(2).to_string())
print()

# ══════════════════════════════════════════════════════════
# 7. ANÁLISIS POR GRUPO DE EDAD
# ══════════════════════════════════════════════════════════
age_stats = (
    df.groupby("Age Group", observed=True)["Purchase Amount (USD)"]
    .agg(pedidos="count", revenue="sum", ticket_prom="mean")
)

print("─" * 60)
print("  VENTAS POR GRUPO DE EDAD")
print("─" * 60)
print(age_stats.round(2).to_string())
print()

# ══════════════════════════════════════════════════════════
# 8. VISUALIZACIONES
# ══════════════════════════════════════════════════════════
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle(
    "Customer Shopping Behavior — Dashboard de Análisis\nJ. Valencia · PUCP · 2024",
    fontsize=14, fontweight="bold", y=1.01
)
fig.patch.set_facecolor("#F3F4F8")

# ── 8.1 Revenue por categoría ──
ax = axes[0, 0]
cat_rev = cat_stats["revenue"].sort_values()
bars = ax.barh(cat_rev.index, cat_rev.values, color=PALETTE[:len(cat_rev)], height=0.55)
ax.set_title("Revenue por Categoría")
ax.set_xlabel("USD")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}K"))
for bar, val in zip(bars, cat_rev.values):
    ax.text(val + 500, bar.get_y() + bar.get_height() / 2,
            f"${val/1000:.0f}K", va="center", fontsize=9, fontweight="bold")
ax.set_xlim(0, cat_rev.max() * 1.18)

# ── 8.2 Revenue por temporada ──
ax = axes[0, 1]
seasons = ["Primavera", "Verano", "Otoño", "Invierno"]
season_order = ["Spring", "Summer", "Fall", "Winter"]
rev_vals = [df[df.Season == s]["Purchase Amount (USD)"].sum() for s in season_order]
season_colors = ["#4ADE80", "#FCD34D", "#FB923C", "#93C5FD"]
bars = ax.bar(seasons, rev_vals, color=season_colors, width=0.6)
ax.set_title("Revenue por Temporada")
ax.set_ylabel("USD")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"${y/1000:.0f}K"))
for bar, val in zip(bars, rev_vals):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 200,
            f"${val/1000:.0f}K", ha="center", fontsize=9, fontweight="bold")
ax.set_ylim(0, max(rev_vals) * 1.15)

# ── 8.3 Top 10 productos ──
ax = axes[0, 2]
tp = top_products.sort_values("revenue")
bar_colors = [PALETTE[i % len(PALETTE)] for i in range(len(tp))]
ax.barh(tp.index, tp["revenue"], color=bar_colors, height=0.65)
ax.set_title("Top 10 Productos por Revenue")
ax.set_xlabel("USD")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.1f}K"))

# ── 8.4 Revenue por grupo de edad ──
ax = axes[1, 0]
age_rev = age_stats["revenue"]
intensity = np.linspace(0.45, 1.0, len(age_rev))
colors_age = [f"#{int(42*i):02x}{int(120*i):02x}{int(214*i):02x}" for i in intensity]
ax.bar(age_rev.index, age_rev.values, color=PALETTE[0], alpha=0.75, width=0.6,
       edgecolor=PALETTE[0], linewidth=1.2)
# Degradado manual: aplicar alpha progresivo
for i, (bar_val, alpha_val) in enumerate(zip(age_rev.values, intensity)):
    ax.bar(age_rev.index[i], bar_val, color=PALETTE[0], alpha=alpha_val, width=0.6)
ax.set_title("Revenue por Grupo de Edad")
ax.set_ylabel("USD")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda y, _: f"${y/1000:.0f}K"))

# ── 8.5 Métodos de pago ──
ax = axes[1, 1]
payment_counts = df["Payment Method"].value_counts()
wedges, texts, autotexts = ax.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct="%1.1f%%",
    colors=PALETTE,
    startangle=90,
    wedgeprops={"linewidth": 2, "edgecolor": "#F3F4F8"},
    pctdistance=0.82,
)
for at in autotexts:
    at.set_fontsize(8)
ax.set_title("Métodos de Pago")

# ── 8.6 Distribución del ticket promedio ──
ax = axes[1, 2]
ax.hist(
    df["Purchase Amount (USD)"],
    bins=30, color=PALETTE[0], alpha=0.85,
    edgecolor="#FFFFFF", linewidth=0.8
)
ax.axvline(aov, color=PALETTE[1], linewidth=2, linestyle="--",
           label=f"Prom: ${aov:.2f}")
ax.set_title("Distribución del Ticket de Compra")
ax.set_xlabel("Purchase Amount (USD)")
ax.set_ylabel("Frecuencia")
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("../docs/analysis_charts.png", dpi=150, bbox_inches="tight",
            facecolor="#F3F4F8")
print("✅ Gráfico guardado en docs/analysis_charts.png")
plt.show()

# ══════════════════════════════════════════════════════════
# 9. RECOMENDACIONES (resumen)
# ══════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  RECOMENDACIONES DE NEGOCIO (basadas en datos)")
print("=" * 60)
print("""
  01 [ALTO]  Programa de lealtad: solo 27% suscrito.
             Implementar beneficios exclusivos para aumentar retención.

  02 [ALTO]  Campaña Otoño: pico de revenue ($60K, +7.6% vs Verano).
             Aumentar stock y marketing en agosto–octubre.

  03 [MEDIO] Replantear descuentos: AOV con descuento ($59.28) ≈
             AOV sin descuento ($60.13). Migrar a bundles de valor.

  04 [MEDIO] Expandir Footwear y Outerwear (AOV más alto, menor
             saturación que Clothing con 44% del revenue).

  05 [DIREC] Segmento 56–70 años = 28% del revenue con 1,105 pedidos.
             Email marketing personalizado puede incrementar frecuencia.
""")
print("=" * 60)
print("  Análisis completado ✅")
print("=" * 60)
