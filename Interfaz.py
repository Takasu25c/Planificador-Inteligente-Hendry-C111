import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

# Lista para almacenar días seleccionados
dias_seleccionados = []

# Crear ventana principal
root = tk.Tk()
root.title("TERAX REPARACION DE MOTHERBOARD")
root.geometry("700x450")
root.configure(bg="lightgray")

# Encabezado azul
header = tk.Frame(root, bg="blue", height=50)
header.pack(fill="x")

title_label = tk.Label(header, text="TERAX REPARACION DE MOTHERBOARD", bg="blue", fg="white",
                       font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Marco principal
main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Sección de botones
button_frame = tk.Frame(main_frame, bg="lightgray")
button_frame.pack(side="left", padx=10)

def solicitar_reparacion():
    if dias_seleccionados:
        messagebox.showinfo("Reparación solicitada", f"Días bloqueados: {', '.join(dias_seleccionados)}")
    else:
        messagebox.showwarning("Sin selección", "No has seleccionado ningún día.")

buttons = [
    ("Solicitar Reparacion", solicitar_reparacion),
    ("Busqueda de Horarios", lambda: print("Busqueda de Horarios")),
    ("Ver Reparaciones Programadas", lambda: print("Ver Reparaciones Programadas"))
]

for text, command in buttons:
    btn = tk.Button(button_frame, text=text, bg="red", fg="white",
                    font=("Helvetica", 12), width=25, height=2, command=command)
    btn.pack(pady=5)

# Sección de calendario
calendar_frame = tk.Frame(main_frame, bg="white", bd=2, relief="groove")
calendar_frame.pack(side="right", padx=10)

# Obtener mes y año actual
now = datetime.now()
year = now.year
month = now.month

# Mostrar mes y año
month_year_label = tk.Label(calendar_frame, text=calendar.month_name[month] + " " + str(year),
                            font=("Helvetica", 14, "bold"), bg="white")
month_year_label.pack(pady=10)

# Encabezado de días
days = ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"]
header_frame = tk.Frame(calendar_frame, bg="white")
header_frame.pack()

for day in days:
    tk.Label(header_frame, text=day, font=("Helvetica", 10, "bold"), bg="white", width=4).pack(side="left")

# Fechas como botones
cal = calendar.monthcalendar(year, month)

def toggle_day(day_btn, day_str):
    if day_str in dias_seleccionados:
        dias_seleccionados.remove(day_str)
        day_btn.config(bg="white")
    else:
        dias_seleccionados.append(day_str)
        day_btn.config(bg="lightblue")

    for week in cal:
     week_frame = tk.Frame(calendar_frame, bg="white")
     week_frame.pack()
    for day in week:
        if day == 0:
            tk.Label(week_frame, text="", bg="white", width=4).pack(side="left")
        else:
            day_str = f"{day:02d}/{month:02d}/{year}"
            day_btn = tk.Button(week_frame, text=str(day), bg="white", width=4,
                                command=lambda b=day_btn, d=day_str: toggle_day(b, d))
            day_btn.pack(side="left")

# Ejecutar la aplicación
root.mainloop()
