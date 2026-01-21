import streamlit as st
import Recursos_y_Personal as rh
import eventos as ev
import datetime as dt
"""import base64
def get_base64(bin_file): 
    with open(bin_file, 'rb') as f: 
        data = f.read() 
    return base64.b64encode(data).decode() 
def set_background(jpg_file): 
    bin_str = get_base64(jpg_file) 
    page_bg_img = f""" """
    <style> 
    [data-testid="stAppViewContainer"] {{ 
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover; 
        background-repeat: no-repeat; 
        background-attachment: fixed;
          }} 
          </style> 
    st.markdown(page_bg_img, unsafe_allow_html=True) # Llamar a la función con tu imagen 
set_background("background.jpg")"""
recursos_en_uso = []
st.title("TERAX")
st.header("Reparacion de Equipos de Computo")
evento = st.selectbox("Seleccione el tipo de reparacion",ev.lista_de_eventos)
if evento == "Defectacion":
    recurso =(st.selectbox("Selecione los recursos a usar",rh.listarecursos))
    boton = st.button("Agregar Recurso")
    if boton:
        recursos_en_uso.append(recurso)
        st.success("Recurso Agregado")
    
    momento_inicio = st.date_input("Seleccione la fecha",dt.date.today())
    hora_inicio = st.time_input("Seleccione la hora",dt.time(12,0))
