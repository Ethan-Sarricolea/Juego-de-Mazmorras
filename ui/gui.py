"""
Descripcion: Interfaz grafica de usuario
Autor: Sarricolea Cortés Ethan Yahel
"""

import tkinter as tk
from tkinter import ttk
from threading import Thread
import time
from services import map_generator

class Game():
    def __init__(self) -> None:
        # ventana menu y carga
        self.puntaje = 0
        self.salas = ["E","V","C","T","S"]
        self.recorrido = 0
        self.openedChests = []
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
                                  "Haz encontrado un tesoro +50 puntos",
                                  "Caiste en una trampa y te haz herido -5 puntos",
                                  "Llegaste al final de la mazmorra"]
        self.descripciones = ["Debes encontrar la salida",
                              "Busca otro camino",
                              "Asi valdra la pena",
                              "Ten mas cuidado",
                              "¿Fin del juego?"]
        self.descripcion = tk.Label(self.window,text="")

        # Pantalla de juego
        # En estos se selecciona la sala a la que ir
        self.camino1 = tk.Button(self.window,image=None,text="1",fg="white",bg="gray15")
        # Aqui va la sala (nodo) a la que lleva la puerta (boton)
        self.camino2 = tk.Button(self.window,image=None,text="2",fg="white",bg="gray15")
        self.camino3 = tk.Button(self.window,image=None,text="3",fg="white",bg="gray15")
        self.camino4 = tk.Button(self.window,image=None,text="4",fg="white",bg="gray15")
        self.volver = tk.Button(self.window,text="Salir",command=self.final)
        self.anterior = None
        self.puertas = [self.camino1,self.camino2,self.camino3,self.camino4]

    def final(self):
        self.clear()
        self.msg.config(text="Lo lograste")
        self.descripcion.config(text=f"Puntaje = {self.puntaje}")
        print("___________")
        print(f"Puntaje = {self.puntaje}")
        print(f"Recorrido: {self.recorrido-1}")
        print(f"Camino mas corto:",len(self.generador.get_camino())-1,self.generador.get_camino())
        self.window.update()
        time.sleep(3)
        self.window.after(2000,self.main_menu)

    def detect(self,event):
        self.go.config(state="normal")

    def clear(self):
        for windget in self.window.winfo_children():
            windget.pack_forget()

    def main_menu(self):
        self.clear()
        tk.Label(self.window,text="Juego de Mazmorras",font=("TkDefaultFont",15)).pack(pady=20)
        self.go.pack(pady=25)
        self.combo.pack(pady=15)
        tk.Button(self.window,text="Salir",bg="red",width=20,command=self.window.destroy).pack(pady=5)
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
        self.game_screen()

    def loading_menu(self):
        self.clear()
        self.msg.pack(pady=60)
        self.msg.config(text="Generando mazmorra")
        self.window.update()
        self.hilo.start()
        self.generador = map_generator.Mazmorras(int(self.combo.get()))
        self.generador.set_map_size()
        self.room = "E"
        time.sleep(1.5)
        self.charge = False
        # Aqui se debe mostrar una imagen de fondo de entrada a una mazmorra y quitar la sig linea (after)
        # self.window.after(2000,self.game_screen)

    def game_screen(self):
        self.charge=False
        self.clear()
        self.show_room(self.room)
        # Aqui ira la cantidad de nodos recorridos, disminuyendo en uno por el anterior
        # self.window.after(2000,self.show_room)

    def show_room(self,sala):
        self.room = sala
        self.charge = False
        habitacion = (self.salas.index(self.room[0])+1 if self.room in self.salas else 0)
        self.clear()
        time.sleep(1)
        self.msg.config(text="",font=("TkDefaultFont",10),fg="white")
        self.msg.pack(pady=60)
        self.descripcion.pack(pady=20)
        # Te da el mensaje de la sala en la que estas
        if (habitacion==5):
            self.msg.config(text=self.mensajes_por_sala[habitacion-1])
            self.descripcion.config(text=self.descripciones[habitacion-1])
            self.window.update()
        elif (habitacion==4):
            self.msg.config(text=self.mensajes_por_sala[habitacion-1])
            self.descripcion.config(text=self.descripciones[habitacion-1])
            self.window.update()
        elif (habitacion==3):
            self.msg.config(text=self.mensajes_por_sala[habitacion-1])
            self.descripcion.config(text=self.descripciones[habitacion-1])
            self.window.update()
        elif (habitacion==2):
            self.msg.config(text=self.mensajes_por_sala[habitacion-1])
            self.descripcion.config(text=self.descripciones[habitacion-1])
            self.window.update()
        elif (habitacion==1):
            self.msg.config(text=(self.mensajes_por_sala[habitacion-1]))
            self.descripcion.config(text=self.descripciones[habitacion-1])
            self.window.update()
        self.window.after(5000,self.show_doors)

    def show_doors(self):
        self.recorrido+=1
        cant = self.generador.get_node_degree(self.room)
        conexiones = list(self.generador.mapa.neighbors(self.room))
        # Se le pasa la cantidad de puertas (nodos) a los que esta conectada la sala actual
        self.clear()
        if self.room[0]=="C":
            if self.room in self.openedChests:
                pass
            else:
                self.puntaje+=50
                self.openedChests.append(self.room)
        if self.room[0]=="T":
            self.puntaje-=10
        if self.room=="S"   :
            self.volver.pack(side="bottom",ipadx=20,pady=10)
        for opcion in range(0,cant):
            self.puertas[opcion].pack(side="left",pady=10,padx=30,ipadx=10,ipady=30)
            self.puertas[opcion].config(command= lambda sala=conexiones[opcion] : self.show_room(sala))
        # print(conexiones)
        print(f"Puntaje = {self.puntaje}")
        print(f"Sala actual: {self.room}")
        self.generador.show_nodes()

    def run(self):
        # Inicia la interfaz
        self.main_menu()
        self.window.mainloop()
"""
En que parte del codigo se genera la mazmorra?
"""