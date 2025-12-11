import streamlit as st
import Recursos_y_Personal as rh
import eventos as ev
st.title("TERAX")
st.header("Reparacion de Equipos de Computo")
st.selectbox("Seleccione el tipo de reparacion",ev.lista_de_eventos)
