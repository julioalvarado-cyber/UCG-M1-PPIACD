import streamlit as st
import libreria_funciones as lf

st.title("Maestría en Ciencias de Datos - Universidad Casa Grande")
st.image("LogoUCG.jpeg")

st.sidebar.title("Paradigmas de programación para IA & CD")
st.write("Elaborado por: Julio Alvarado")

capital = st.number_input("Ingrese el capital", value = 1000)
taza_anual_pct = st.number_input("Ingrese el taza", value = 15)
dias_mora = st.number_input("Ingrese los dias de mora", value = 20)

resultado = lf.calcular_interes_mora(capital,taza_anual_pct,dias_mora)

st.write("El resultado por atrazo es: ", resultado)
