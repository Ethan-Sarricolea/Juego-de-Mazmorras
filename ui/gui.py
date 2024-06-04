"""
Descripcion: Interfaz grafica de usuario
Autor: Sarricolea Cortés Ethan Yahel
"""

import tkinter as tk
from tkinter import ttk,messagebox
from threading import Thread
import time
from services import map_generator

class Game():
    def __init__(self) -> None:
        # ventana menu y carga
        self.window = tk.Tk()
        self.window.geometry("400x300")
        self.window.title("Juego de mazmorras")
        self.window.resizable(0,0)
        self.window.config(bg="gray30")
        self.go = tk.Button(self.window,text="Comenzar",state="disabled",
                            bg="green",width=20,fg="black",command=self.loading_menu)
        self.combotext = tk.StringVar(value="Nivel de mazmorra")
        self.combo = ttk.Combobox(self.window,textvariable=self.combotext,
                                  values=(1,2,3),state="readonly")
        self.hilo = Thread(target=self.points)
        self.charge = True
        self.msg = tk.Label(self.window,text="",font=("TkDefaultFont",18),bg="gray30",fg="white")
        self.mensajes_por_sala = ["La entrada esta bloqueada",
                                  "Al parecer aqui no hay nada...",
                                  "Haz encontrado un tesoro +X puntos",
                                  "Caiste en una trampa haz muerto...",
                                  "Lograste salir de la mazmorra"]
        self.descripciones = ["Debes encontrar la salida",
                              "Busca otro camino",
                              "Asi valdra la pena",
                              "Mejor suerte la proxima",
                              "Fin del juego"]
        self.descripcion = tk.Label(self.window,text="")

        # Pantalla de juego
        # En estos se selecciona la sala a la que ir
        self.camino1 = tk.Button(self.window,image=None,text="1",fg="white",bg="gray15")
        # Aqui va la sala (nodo) a la que lleva la puerta (boton)
        self.ruta1 = None
        self.camino2 = tk.Button(self.window,image=None,text="2",fg="white",bg="gray15")
        self.ruta2 = None
        self.camino3 = tk.Button(self.window,image=None,text="3",fg="white",bg="gray15")
        self.ruta3 = None
        self.camino4 = tk.Button(self.window,image=None,text="4",fg="white",bg="gray15")
        self.ruta4 = None
        self.volver = tk.Button(self.window,text="Volver")
        self.anterior = None
        self.puertas = [self.camino1,self.camino2,self.camino3,self.camino4]
        self.rutas = [self.ruta1,self.ruta2,self.ruta3,self.ruta4]

    def detect(self,event):
        self.go.config(state="normal")

    def clear(self):
        for windget in self.window.winfo_children():
            windget.pack_forget()

    def main_menu(self):
        tk.Label(self.window,text="Juego de Mazmorras",font=("TkDefaultFont",15)).pack(pady=20)
        self.go.pack(pady=25)
        self.combo.pack(pady=15)
        tk.Button(self.window,text="Salir",bg="red",width=20).pack(pady=5)
        self.combo.bind("<<ComboboxSelected>>",self.detect)

    def points(self):
        while self.charge:
            self.msg.config(text="Generando mazmorra.")
            self.window.update()
            time.sleep(0.1)
            self.msg.config(text="Generando mazmorra..")
            self.window.update()
            time.sleep(0.1)
            self.msg.config(text="Generando mazmorra...")
            self.window.update()
            time.sleep(0.1)

    def loading_menu(self):
        self.clear()
        self.msg.pack(pady=60)
        self.msg.config(text="Generando mazmorra")
        self.window.update()
        self.hilo.start()
        # Aqui se debe mostrar una imagen de fondo de entrada a una mazmorra y quitar la sig linea (after)
        self.window.after(2000,self.game_screen)

    def game_screen(self):
        self.charge=False
        self.clear()
        # Aqui ira la cantidad de nodos recorridos, disminuyendo en uno por el anterior
        self.window.after(2000,self.show_room)

    def show_room(self,room=1):
        self.charge = False
        self.clear()
        time.sleep(1)
        self.msg.config(text="",font=("TkDefaultFont",10))
        self.msg.pack(pady=60)
        self.descripcion.pack(pady=20)
        if (room==5):
            self.msg.config(text=self.mensajes_por_sala[room-1])
            self.descripcion.config(text=self.descripciones[room-1])
            self.window.update()
        elif (room==4):
            self.msg.config(text=self.mensajes_por_sala[room-1])
            self.descripcion.config(text=self.descripciones[room-1])
            self.window.update()
        elif (room==3):
            self.msg.config(text=self.mensajes_por_sala[room-1])
            self.descripcion.config(text=self.descripciones[room-1])
            self.window.update()
        elif (room==2):
            self.msg.config(text=self.mensajes_por_sala[room-1])
            self.descripcion.config(text=self.descripciones[room-1])
            self.window.update()
        elif (room==1):
            self.msg.config(text=(self.mensajes_por_sala[room-1]))
            self.descripcion.config(text=self.descripciones[room-1])
            self.window.update()
        self.window.after(5000,self.show_doors)

    def show_doors(self,cant=4):
        self.clear()
        self.volver.pack(side="bottom",ipadx=20,pady=10)
        for opcion in range(0,cant):
            self.puertas[opcion].pack(side="left",pady=10,padx=30,ipadx=10,ipady=30)

    def run(self):
        self.main_menu()
        self.window.mainloop()