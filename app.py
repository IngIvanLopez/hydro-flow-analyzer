import streamlit as st
import pandas as pd
from hydro_analysis import hydro_metrics, plot_flow_duration_curve

st.title("HydroFlow Analyzer")
st.write("Aplicación para análisis hidrológico básico")

uploaded_file = st.file_uploader("Sube un archivo CSV con datos de caudal", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.write("Datos cargados:")
    st.dataframe(df)

    results = hydro_metrics(df)

    st.subheader("Resultados")

    st.write(f"Caudal promedio: {results['mean_flow']:.2f}")
    st.write(f"Caudal máximo: {results['max_flow']:.2f}")
    st.write(f"Caudal mínimo: {results['min_flow']:.2f}")

    st.subheader("Curva de duración de caudales")

    fig = plot_flow_duration_curve(df)
    st.pyplot(fig)
