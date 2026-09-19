import streamlit as st
import libreria_funciones as lf

st.title("Maestría en Ciencias de Datos - Universidad Casa Grande")
st.image("LogoUCG.jpeg")

st.sidebar.title("Paradigmas de programación para IA & CD")
st.write("Elaborado por: Julio Alvarado")

capital=st.number_input("Ingrese el capital")
taza_anual_pct=st.number_input("Ingrese el taza")
dias_mora=st.number_input("Ingrese los dias de mora")

#resultado = lf.calcular_interes_mora()
