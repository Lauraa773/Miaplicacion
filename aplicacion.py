import streamlit as st
import Funciones as fun 
st.title("Aplicación de funciones")
capital = st.number_input("Ingrese el capital:",100,10000)
tiempo = st.number_input("Ingrese el tiempo:",value=12)
tasa_interes = st.number_input("Ingrese la tasa de interés:",value=0.05)
interes = fun.interes_simple(capital_inicial=capital,tiempo_meses=tiempo,tasa_interes=tasa_interes)
st.write("El interés simple es:",int(interes))
