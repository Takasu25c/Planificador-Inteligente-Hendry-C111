import streamlit as st
import Recursos_y_Personal as rh
import eventos as ev
import datetime as dt
import base64
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
if "eventos_en_curso" not in st.session_state:
  st.session_state.eventos_en_curso = {}
if "recursos_en_uso" not in st.session_state:
  st.session_state.recursos_en_uso = []
def agregar_recurso(recurso):  
   boton = st.button("Agregar Recurso")
   if boton:
    if recurso in st.session_state.recursos_en_uso:
      st.error("Recurso no disponible")
    else:
      st.session_state.recursos_en_uso.append(recurso)
      st.success("Recurso Agregado")
def iniciar_evento(evento):
   recurso =(st.selectbox("Selecione los recursos a usar",rh.listarecursos))
   inicio_evento = st.datetime_input("Seleccione la fecha",dt.datetime.now())
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
     if recurso not in rh.socket:
       st.error("No compatible con el servicio")
     else:
       agregar_recurso(recurso)
   elif evento == "Reparacion de los 15 seg":
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
iniciar_evento(evento)
st.write("Recursos en uso:", st.session_state.recursos_en_uso)
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