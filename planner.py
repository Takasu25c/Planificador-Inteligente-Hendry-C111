import json
import os
import datetime as dt
salva = "salva.json"
def guardar_estado(lista_de_eventos: list):
 for eventos in lista_de_eventos:
   eventos["Horario de Inicio"] = str(eventos["Horario de Inicio"])
   eventos["Horario de Terminacion"] = str(eventos["Horario de Terminacion"])
 with open(salva,"w") as f:
    json.dump(lista_de_eventos,f)
def cargar_estado(lista_de_eventos: list):
  if os.path.getsize(salva) > 0:
    with open(salva,"r") as f:
      try:
        lista_cargada = json.load(f)
        for eventos in lista_cargada:
          eventos["Horario de Inicio"] = dt.datetime.strptime(eventos["Horario de Inicio"], "%Y-%m-%d %H:%M:%S")
          eventos["Horario de Terminacion"] = dt.datetime.strptime(eventos["Horario de Terminacion"],"%Y-%m-%d %H:%M:%S")
        return lista_cargada.copy()
      except json.JSONDecodeError:
        print("Datos invalidos")
  else:
    print("El archivo esta vacio")   