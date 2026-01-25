import streamlit as st
import pandas as pd
import Recursos_y_Personal as rh
import eventos as ev
import datetime as dt
import base64
import planner as pn
def get_base64(bin_file): 
    with open(bin_file, 'rb') as f: 
        data = f.read() 
    return base64.b64encode(data).decode() 
def fondo(jpg_file): 
    bin_str = get_base64(jpg_file) 
    page_bg_img = f"""
    <style> 
    [data-testid="stAppViewContainer"] {{ 
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover; 
        background-repeat: no-repeat; 
        background-attachment: fixed;
          }} 
          </style> """
    st.markdown(page_bg_img, unsafe_allow_html=True)
fondo("background.jpg")
if "eventos_en_curso" not in st.session_state:
  st.session_state.eventos_en_curso = []
if "recursos_en_uso" not in st.session_state:
  st.session_state.recursos_en_uso = []
st.session_state.eventos_en_curso = pn.cargar_estado(st.session_state.eventos_en_curso)
duracion_eventos = {
  "Defectacion": dt.timedelta(hours=1),
  "Reparacion de tarjeta de video": dt.timedelta(hours=5),
  "Reparacion de Socket": dt.timedelta(hours=12),
  "Reparacion de los 15 segundos": dt.timedelta(hours=1),
  "Reparacion del 12v del procesador": dt.timedelta(hours=5),
  "Cambio de pastilla de audio": dt.timedelta(hours=3),
  "Sustitucion de puerto usb": dt.timedelta(hours=2),
  "Sustitucion de puerto de video": dt.timedelta(hours=2),
  "Reparacion de chipset de video": dt.timedelta(hours=9),
  "Mantenimiento: Bajo": dt.timedelta(hours=1),
  "Mantenimiento: Medio": dt.timedelta(hours=2),
  "Mantenimiento: Alto": dt.timedelta(hours=4),
  "Reparacion Sencilla": dt.timedelta(hours=2),
}
def agregar_recurso(recurso):  
   col1,col2,col3 = st.columns([0.4,0.2,0.4],vertical_alignment= "center")
   with col1:
    boton = st.button("Agregar Recurso")
   with col2:
    numero =st.number_input("Indice",min_value=0,max_value= len(st.session_state.recursos_en_uso))
   with col3:
     eliminar = st.button("Eliminar recurso")
   if eliminar:
     if not st.session_state.recursos_en_uso:
       st.error("No hay elementos que eliminar")
     else:
       del st.session_state.recursos_en_uso[numero]
   if boton:
    if recurso in st.session_state.recursos_en_uso:
      st.error("Recurso no disponible")
    else:
      st.session_state.recursos_en_uso.append(recurso)
      st.success("Recurso Agregado")
def registrar_evento(evento):
  def registro():
    reparacion = {
      "Nombre": nombre,
      "Tipo de Evento": evento,
      "Horario de Inicio": inicio_evento,
      "Horario de Terminacion": inicio_evento + duracion_eventos[evento],
      "Recursos": recursos_evento
      }
    st.session_state.eventos_en_curso.append(reparacion)
    pn.guardar_estado(st.session_state.eventos_en_curso)
    st.success("Registro añadido")
  registrar = st.button("Registrar Evento")
  if registrar:
    recursos_evento = st.session_state.recursos_en_uso.copy()
    if st.session_state.eventos_en_curso == False:
      registro()
    else:
      for herramienta in recursos_evento:
        for eventico in st.session_state.eventos_en_curso:
          if herramienta in eventico["Recursos"]:
            if not inicio_evento + duracion_eventos[evento] <= eventico["Horario de Inicio"] or inicio_evento >= eventico["Horario de Terminacion"]:
              st.error(f"El/La {herramienta} no esta disponible en ese horario")
              return
            else:
              registro()
          else:
            continue
      else:
        registro()
    st.session_state.recursos_en_uso.clear()
def iniciar_evento(evento):
   recurso =(st.selectbox("Selecione los recursos a usar",rh.listarecursos))
   if evento == "Defectacion":
     if recurso not in rh.rdefectacion:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion de tarjeta de video":
     if recurso not in rh.rtvideo:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion de Socket":
     if recurso not in rh.rsocket:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion de los 15 segundos":
     if recurso not in rh.r15seg:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion del 12v del procesador":
     if recurso not in rh.r12vcpu:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Cambio de pastilla de audio":
     if recurso not in rh.rpaudio:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Sustitucion de puerto usb":
     if recurso not in rh.rsususb:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Sustitucion de puerto de video":
     if recurso not in rh.rpvideo:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion de chipset de video":
     if recurso not in rh.rcvideo:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion Sencilla":
     if recurso not in rh.rsencilla:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Mantenimiento: Bajo":
     if recurso not in rh.mbajo:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Mantenimiento: Medio":
     if recurso not in rh.mmedio:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Mantenimiento: Alto":
     if recurso not in rh.malto:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
st.title("TERAX",text_alignment= "center")
st.header("Reparacion de Equipos de Computo",text_alignment= "center")
evento = st.selectbox("Seleccione el tipo de reparacion",ev.lista_de_eventos)
nombre = st.text_input("Por favor diga su nombre","Nombre y apellidos")
inicio_evento = st.datetime_input("Seleccione la fecha",dt.datetime.now())
iniciar_evento(evento)
registrar_evento(evento)
rs = pd.DataFrame(st.session_state.recursos_en_uso)
st.dataframe(st.session_state.recursos_en_uso)
df = pd.DataFrame(st.session_state.eventos_en_curso)
st.write("Eventos",df)