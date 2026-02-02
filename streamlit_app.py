import streamlit as st
import pandas as pd
import Recursos_y_Personal as rh
import eventos as ev
import datetime as dt
import base64
import planner as pn
import os
import json
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
    numero =st.number_input("Indice",min_value=0,max_value= len(st.session_state.recursos_en_uso), key= "Resource Index")
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
      verificacion = verificar_restricciones(recurso)
      if verificacion == True:
        st.session_state.recursos_en_uso.append(recurso)
        st.success("Recurso Agregado")      
def verificar_restricciones(recurso):
  primer_elemento_exclusion = ("Osciloscopio","Fuente de poder","Estacion de Calor")
  segundo_elemento_exclusion = ("Multimetro","Regulador de voltaje","Cautin")
  if recurso in primer_elemento_exclusion:
    if segundo_elemento_exclusion[primer_elemento_exclusion.index(recurso)] in st.session_state.recursos_en_uso:
      st.error("Ya se selecciono una herramienta equivalente")
      return False
    else:
      return True
  elif recurso in segundo_elemento_exclusion:
    if primer_elemento_exclusion[segundo_elemento_exclusion.index(recurso)] in st.session_state.recursos_en_uso:
      st.error("Ya se selecciono una herramienta equivalente")
      return False
    else:
      return True
  else:
    return True
def verificar_inclusiones(recursos):
  if "Osciloscopio" in recursos or "Multimetro" in recursos:
    if "Monitor con BoardView" not in recursos:
      st.error("No se agrego Monitor con Boardview")
      return False
    else:
      return True
  elif "Monitor con BoardView" in recursos:
    if "Osciloscopio" not in recursos and "Multimetro" not in recursos:
      st.error("No se agrego Osiloscopio o Multimetro")
      return False
    else:
      return True
  elif "Estacion de Calor" in recursos or "Cautin" in recursos:
    if "Flux" not in recursos and "Estaño" not in recursos:
      st.error("Debe agregar Flux o Estaño")
      return False
    else:
      return True
  elif "Flux" in recursos or "Estaño" in recursos:
    if "Cautin" not in recursos and "Estacion de Calor" not in recursos:
      st.error("No se agrego Cautin o Estacion de Calor")
      return False
    else:
      return True
def registro(inicio_evento):
    reparacion = {
      "Nombre": nombre,
      "Tipo de Evento": evento,
      "Horario de Inicio": inicio_evento,
      "Horario de Terminacion": inicio_evento + duracion_eventos[evento],
      "Recursos": st.session_state.recursos_en_uso.copy()
      }
    st.session_state.eventos_en_curso.append(reparacion)
    pn.guardar_estado(st.session_state.eventos_en_curso)
    st.success("Registro añadido")
def registrar_evento(evento):
  col1,col2,col3 = st.columns([0.4,0.2,0.4],vertical_alignment= "center")
  with col1:
    registrar = st.button("Registrar Evento")
  with col2:
    nevento = st.number_input("Indice",min_value=0,max_value= len(st.session_state.eventos_en_curso),key= "Evemt Index")
  with col3:
    eliminar = st.button("Eliminar evento")
  if eliminar:
    if not st.session_state.eventos_en_curso:
      st.error("No hay eventos en la lista")
    else:
      del st.session_state.eventos_en_curso[nevento]
      pn.guardar_estado(st.session_state.eventos_en_curso)
      st.session_state.eventos_en_curso = pn.cargar_estado(st.session_state.eventos_en_curso)
  if registrar:
    if verificar_inclusiones(st.session_state.recursos_en_uso) == True:
      recursos_evento = st.session_state.recursos_en_uso.copy()
      if st.session_state.eventos_en_curso == False:
        registro(inicio_evento)
      else:
        for herramienta in recursos_evento:
          for eventico in st.session_state.eventos_en_curso:
            inicio = eventico["Horario de Inicio"]
            fin = eventico["Horario de Terminacion"]
            if isinstance(inicio, str): 
              inicio = dt.datetime.fromisoformat(inicio) 
            if isinstance(fin, str): 
              fin = dt.datetime.fromisoformat(fin)
            if herramienta in eventico["Recursos"]:
              final_evento = inicio_evento + duracion_eventos[evento]
              nosolapan = (final_evento <= inicio) or (inicio_evento >= fin)
              if not nosolapan:
                st.error(f"El/La {herramienta} no esta disponible en ese horario")
                return  
              
                
            else:
              continue
      registro(inicio_evento)  
      st.session_state.recursos_en_uso.clear()
def busqueda_automatica(lista_eventos,evento,inicio):
  busqueda = st.button("Busqueda de Huecos",width= "content")
  if busqueda:
    horarios = []
    for eventos in lista_eventos:
      horarios.append(eventos["Horario de Inicio"])
      horarios.append(eventos["Horario de Terminacion"])
    counter = 1
    while counter < len(horarios):
      if counter == len(horarios)-1:
        inicio = horarios[counter] + dt.timedelta(minutes= 15)
        registro(inicio)
        st.session_state.recursos_en_uso.clear()
        break
      hueco = horarios[counter+1] - horarios[counter]
      if hueco >= duracion_eventos[evento] + dt.timedelta(minutes= 15):
        registro(horarios[counter]+dt.timedelta(minutes= 15))
        st.session_state.recursos_en_uso.clear()
        break
      else:
        counter = counter + 2
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
st.session_state.eventos_en_curso = sorted(st.session_state.eventos_en_curso,key= lambda x: x["Horario de Terminacion"])
iniciar_evento(evento)
registrar_evento(evento)
busqueda_automatica(st.session_state.eventos_en_curso,evento,inicio_evento)
rs = pd.DataFrame(st.session_state.recursos_en_uso)
st.dataframe(st.session_state.recursos_en_uso)
df = pd.DataFrame(st.session_state.eventos_en_curso)
st.write("Eventos",df)