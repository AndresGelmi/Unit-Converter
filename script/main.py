import customtkinter as ctk
from database import *

BUTTON_COLOR = "#3174EA"
HOVER_COLOR = "#143266"
FRAME_COLOR = "#5489E5"

input_unit = ctk.StringVar
output_unit = ctk.StringVar

app = ctk.CTk()
app.geometry("600x300")
app.title("Unit Converter")

def button_function(name):
    for _list in options:
        if options.index(_list) == name:
            input_selection.set(_list[0])
            output_selection.set(_list[0])
    input_selection.configure(values=options[name])
    output_selection.configure(values=options[name])
    output_label.configure(text="")
    unit_historial.append(name)

def convert():
    local_text = input_entry.get()
    current_mode = unit_historial[-1]
    try:
        input_number = float(local_text)
    except ValueError:
        pass
    else:
        input_unit = input_selection.get()
        output_unit = output_selection.get()

        # Si el modo no es "temperatura" (índice 3), usamos la lógica de multiplicadores
        if current_mode != 3:
            multiplier = conversion_factors[current_mode][input_unit]
            divider = 1 / conversion_factors[current_mode][output_unit]
            # Caso especial para electron-volt (evita redondear innecesariamente)
            if input_unit != "electron-volt":
                output_label.configure(text=str(round(input_number * multiplier * divider,3)))
            else: 
                output_label.configure(text=str(input_number * multiplier * divider))

        # Modo de temperatura (índice 3)
        else:
            # Variable para almacenar el resultado antes de mostrarlo
            salida = 0.0

            if input_unit == "celsius":
                if output_unit == "celsius":
                    salida = input_number
                elif output_unit == "fahrenheit":
                    # C -> F
                    salida = (input_number * 9/5) + 32
                elif output_unit == "kelvin":
                    # C -> K
                    salida = input_number + 273.15
                elif output_unit == "rankine":
                    # C -> R
                    salida = (input_number + 273.15) * 9/5

            elif input_unit == "fahrenheit":
                if output_unit == "celsius":
                    # F -> C
                    salida = (input_number - 32) * 5/9
                elif output_unit == "fahrenheit":
                    salida = input_number
                elif output_unit == "kelvin":
                    # F -> K
                    salida = (input_number + 459.67) * 5/9
                elif output_unit == "rankine":
                    # F -> R
                    salida = input_number + 459.67

            elif input_unit == "kelvin":
                if output_unit == "celsius":
                    # K -> C
                    salida = input_number - 273.15
                elif output_unit == "fahrenheit":
                    # K -> F
                    salida = (input_number * 9/5) - 459.67
                elif output_unit == "kelvin":
                    salida = input_number
                elif output_unit == "rankine":
                    # K -> R
                    salida = input_number * 9/5

            elif input_unit == "rankine":
                if output_unit == "celsius":
                    # R -> C
                    salida = (input_number - 491.67) * 5/9
                elif output_unit == "fahrenheit":
                    # R -> F
                    salida = input_number - 459.67
                elif output_unit == "kelvin":
                    # R -> K
                    salida = input_number * 5/9
                elif output_unit == "rankine":
                    salida = input_number

            output_label.configure(text=str(round(salida, 3)))

def update_input_unit(choice):
    input_unit = choice

def update_output_unit(choice):
    output_unit = choice

variable_texto = ctk.StringVar()

frame = ctk.CTkFrame(app,width=590,height= 76,fg_color=FRAME_COLOR)
frame.pack_propagate(False)
frame.pack(pady = 5)

top_frame = ctk.CTkFrame(frame,fg_color=FRAME_COLOR)
top_frame.pack(side="top") 

bottom_frame = ctk.CTkFrame(frame,fg_color=FRAME_COLOR)
bottom_frame.pack()

selection_frame = ctk.CTkFrame(app,width= 590,height=50)
selection_frame.propagate(False)
selection_frame.pack()

mass_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(0),
    text="Masa",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
distancia_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(1),
    text="Distancia",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
time_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(2),
    text="Tiempo",
    width= 50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
temperature_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(3),
    text="Temperatura",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
speed_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(4),
    text="Velocidad",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
presion_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(5),
    text="Presión",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
volumen_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(6),
    text="Volumen",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
aceleration_button = ctk.CTkButton(master=top_frame,
    command=lambda:button_function(7),
    text=" Aceleración ",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
density_button = ctk.CTkButton(master=bottom_frame,
    command=lambda:button_function(8),
    text="Densidad",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
energy_button = ctk.CTkButton(master=bottom_frame,
    command=lambda:button_function(9),
    text="Energía",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
flow_button = ctk.CTkButton(master=bottom_frame,
    command=lambda:button_function(10),
    text="Flujo",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")
area_button = ctk.CTkButton(master=bottom_frame,
    command=lambda:button_function(11),
    text="Área",
    width=50,
    fg_color=BUTTON_COLOR,
    hover_color=HOVER_COLOR,
    text_color="white")

mass_button.pack(side="left",padx=5)
distancia_button.pack(side="left")
time_button.pack(side="left",padx=5)
temperature_button.pack(side="left")
speed_button.pack(side="left",padx=5)
presion_button.pack(side="left")
volumen_button.pack(side="left",padx=5)
aceleration_button.pack(side="left",pady=5)
density_button.pack(side="left",pady=2)
energy_button.pack(side="left",pady=2,padx=5)
flow_button.pack(side="left",pady= 2)
area_button.pack(side="left",pady=2,padx=5)

input_selection = ctk.CTkOptionMenu(selection_frame,command=update_input_unit,values=options[0],fg_color=BUTTON_COLOR,hover=HOVER_COLOR)
input_selection.set("gramo")
output_selection = ctk.CTkOptionMenu(selection_frame,command=update_output_unit,values=options[0],fg_color=BUTTON_COLOR,hover=HOVER_COLOR)
output_selection.set("gramo")

input_selection.pack(side="left",padx=30)
output_selection.pack(side="right",padx=30)

label_frame = ctk.CTkFrame(app,width=580,height=50,fg_color="transparent")
label_frame.propagate(False)
input_frame = ctk.CTkFrame(label_frame,width=100,height=35)
input_frame.propagate(False)
output_frame = ctk.CTkFrame(label_frame,width=100,height=35)
output_frame.propagate(False)
input_label = ctk.CTkLabel(input_frame,text="Input",text_color="white",font=("Helvetica",16))
label_frame.pack(padx =10 ,pady=10)
input_frame.pack(side = "left",padx = 50)
output_frame.pack(side = "right", padx=60)
input_label.pack(pady = 4)
input_label = ctk.CTkLabel(output_frame,text="Output",text_color="white",font=("Helvetica",16))
input_label.pack(pady=4)

entry_frame = ctk.CTkFrame(app,width=580,height=40)
entry_frame.propagate(False)
entry_frame.pack()
input_entry = ctk.CTkEntry(entry_frame,textvariable=variable_texto)
input_entry.pack(side="left",padx= 30)
output_label_frame = ctk.CTkFrame(entry_frame,width=160,height=30,border_width=2)
output_label_frame.propagate(False)
output_label = ctk.CTkLabel(output_label_frame,text="")
output_label.pack(pady=6)
output_label_frame.pack(side="right",pady=5,padx=30)

name_frame = ctk.CTkFrame(app,height=25,width=580,fg_color="transparent")
name_frame.propagate(False)
name_frame.pack(pady=10)
name_label = ctk.CTkLabel(name_frame,height=50,text="Made by Andrés Gelmi | 2024",font=("Helvetica",10))
name_label.pack(side="left",padx=5)

convert_button = ctk.CTkButton(entry_frame,
                               command=convert,
                               fg_color=BUTTON_COLOR,
                               hover_color=HOVER_COLOR,
                               width=130,
                               height=30,
                               text="Convert",
                               font=("Helvetica",16))
convert_button.pack(pady=5)

app.mainloop()
