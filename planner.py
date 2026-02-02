import json
import os
import datetime as dt
salva = "salva.json"
def guardar_estado(lista_de_eventos: list):
 for eventos in lista_de_eventos:
   if isinstance(eventos["Horario de Inicio"],dt.datetime):
    eventos["Horario de Inicio"] = eventos["Horario de Inicio"].isoformat()
   if isinstance(eventos["Horario de Terminacion"],dt.datetime):
    eventos["Horario de Terminacion"] = eventos["Horario de Terminacion"].isoformat()
 with open(salva,"w") as f:
    json.dump(lista_de_eventos,f)
def cargar_estado(lista_de_eventos: list):
  if os.path.getsize(salva) > 0:
    with open(salva,"r") as f:
      try:
        lista_cargada = json.load(f)
        for eventos in lista_cargada:
          eventos["Horario de Inicio"] = dt.datetime.fromisoformat(eventos["Horario de Inicio"])
          eventos["Horario de Terminacion"] = dt.datetime.fromisoformat(eventos["Horario de Terminacion"])
        return lista_cargada.copy()
      except json.JSONDecodeError:
        print("Datos invalidos")
  else:
    print("El archivo esta vacio")   