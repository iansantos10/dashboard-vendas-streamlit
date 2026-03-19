import pandas as pd
import plotly.express as px
import streamlit as st

data = {
    "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "faturamento": [100000, 80000, 120000, 110000, 130000, 90000],
    "canal": ["Online", "Loja", "Online", "Loja", "Online", "Loja"]
}

df = pd.DataFrame(data)

# KPIs
faturamento_total = df["faturamento"].sum()
media = df["faturamento"].mean()

crescimento = ((df["faturamento"].iloc[-1] - df["faturamento"].iloc[0]) 
               / df["faturamento"].iloc[0]) * 100

st.title("📊 Dashboard de Vendas")

# Colunas
col1, col2, col3 = st.columns(3)

col1.metric("Faturamento Total", f"R$ {faturamento_total:,.0f}")
col2.metric("Média Mensal", f"R$ {media:,.0f}")
delta = f"{crescimento:.2f}%"

col3.metric(
    "Crescimento",
    f"{crescimento:.2f}%",
    delta=delta
)

# Gráfico de linha
fig = px.line(df, x="mes", y="faturamento", title="Evolução do Faturamento")
st.plotly_chart(fig)

# Gráfico por canal
fig2 = px.bar(df, x="canal", y="faturamento", color="canal", title="Faturamento por Canal")
st.plotly_chart(fig2)
