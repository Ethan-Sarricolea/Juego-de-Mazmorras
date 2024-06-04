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
            self.create_rooms(3)
            # pos = nx.spring_layout(self.mapa)  # Posiciones de los nodos
            # nx.draw(self.mapa,pos,with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
            # nx.draw_networkx_labels(self.mapa, pos)
            # plt.show()
            
    def create_rooms(self,maxSize):
        mainmaxSize = maxSize
        for room_type in self.salas:
            if (room_type=="E" or room_type=="S"):
                continue
            else:
                maxSize = mainmaxSize
                size = self.aleatorio.randrange(1,maxSize-1)
                maxSize-=size
                for i in range(1,size):
                    self.mapa.add_node(i,name=room_type)

    def get_map_size(self) -> int:
        print("lalalala")

# algo = Mazmorras(1)
# algo.set_map_size()