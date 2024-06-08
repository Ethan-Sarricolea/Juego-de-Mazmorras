"""
Descripcion:
Reglas del grafo 
los nodos vacios, la entrada y la salida deben tener de 1 a 4 conexiones

habitaciones:
1- Entrada
2- Vacio
3- tesoro
4- trampa
5- salida

numero de habitaciones lvl1 = 1E 1S, 3 particulares 3 vacias (8)
lvl2 = 6+6 (mas 2) (14)
lvl3 = 9+9 (mas 2) (20)

habra un limite de habitaciones particulares (cofre o trampa)
un limite de habitaciones vacias

estos limites dependeran del nivel

Autor:
"""

import networkx as nx
import matplotlib.pyplot as plt
import random


class Mazmorras:
    def __init__(self,level) -> None:
        self.nivel = level
        self.aleatorio = random.Random()
        self.mapa = nx.Graph()
        self.salas = ["E","V","C","T","S"]
        self.vacias = []
        self.cofres = []
        self.trampas = []
    
    def set_map_size(self):
        #Crear y añadir los nodos
        if self.nivel==1:
            # Crear vacios y particulares
            self.create_rooms(3,8)
        elif self.nivel==2:
            self.create_rooms(6,14)
        elif self.nivel==3:
            self.create_rooms(9,20)
        # Mostrar grafo
        pos = nx.spring_layout(self.mapa)  # Posiciones de los nodos
        nx.draw(self.mapa,pos,with_labels=True, node_color='lightblue', node_size=500)
        labels = nx.get_node_attributes(self.mapa, 'id')
        nx.draw_networkx_labels(self.mapa, pos, labels=labels)
        plt.show()
            
    def create_rooms(self,maxSize,limit):
        #creacion de la entrada
        salas_cant = 1
        for room in self.salas:
            if room=="E" or room=="S":
                # Agregar una entrada y una salida
                self.mapa.add_node(room)
                salas_cant+=1
            elif (room=="V"):
                # Agregar el numero maximo de salas vacias
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    salas_cant+=1
            elif (room=="C"):
                #Agregar un numero aleatorio de cofres segun el maximo
                cant = self.aleatorio.randrange(1,3)
                maxSize -=cant
                for i in range(1,cant+1):
                    self.mapa.add_node(f"{room}{i}")
                    salas_cant+=1
            elif (room=="T"):
                # Agregar el numero restante de trampas segun el maximo
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    salas_cant+=1

    def get_map_size(self) -> int:
        print("lalalala")

    def conect_rooms(self) -> None:
        print("Conexion de los nodos")
        # Un nodo se puede conectar hasta a 4 salas y debe haber al menor un camino a la salida
        """
            Se puede agregar un proceso para crear x caminos principales segun el nivel (1,2,3)
            Estos se generan primero y despues se conectan los demas nodos a las salas de estso de manera aleatorioa
            Despues de generarse los caminos principales ya no se podra conectar a la entrada o salida
        """

algo = Mazmorras(1)
algo.set_map_size()