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
        self.nodos = []
        self.dist = []
    
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
        # print(self.nodos)
            
    def create_rooms(self,maxSize,limit):
        #creacion de la entrada
        salas_cant = 1
        for room in self.salas:
            if room=="E" or room=="S":
                # Agregar una entrada y una salida
                self.mapa.add_node(room)
                self.nodos.append(room)
                salas_cant+=1
            elif (room=="V"):
                # Agregar el numero maximo de salas vacias
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
                    salas_cant+=1
            elif (room=="C"):
                #Agregar un numero aleatorio de cofres segun el maximo
                cant = self.aleatorio.randrange(1,3)
                maxSize -=cant
                for i in range(1,cant+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
                    salas_cant+=1
            elif (room=="T"):
                # Agregar el numero restante de trampas segun el maximo
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
                    salas_cant+=1
        self.conect_rooms(limit=limit)

    def show_nodes(self) -> int:
        pos = nx.spring_layout(self.mapa)  # Posiciones de los nodos
        nx.draw(self.mapa,pos,with_labels=True, node_color='lightblue', node_size=500)
        labels = nx.get_node_attributes(self.mapa, 'id')
        nx.draw_networkx_labels(self.mapa, pos, labels=labels)
        plt.show()

    def clear(self):
        nodes_to_remove = [node for node in self.mapa.nodes if self.mapa.degree(node) == 0]
        for node in nodes_to_remove:
            self.mapa.remove_node(node)
            # Eliminar las conexiones de un nodo si tiene mas de 4

    def conect_rooms(self,limit) -> None:
        # print(self.nodos)
        # print(self.dist)
        finInIndex = 4
        for room in self.salas:
            if (room=="E"):
                add = [room]
                for n in range(finInIndex):
                    number = self.aleatorio.randrange(1,limit-1)
                    add.append(self.nodos[number])
                self.dist.append(add)
                last = add[-1]
                print(add)
            elif (room=="S"):
                # Si es una sala vacia se agrega un numero aleatorio de conexiones entre 1 y 3
                add = [room]
                for n in range(finInIndex-1):
                    number = self.aleatorio.randrange(1,limit-1)
                    add.append(self.nodos[number])
                self.dist.append(add)
                print(add)    
            elif (room=="V"):
                for sala in self.nodos:
                    # print(self.nodos)
                    # Si es una sala vacia, de cofre o trampa:
                    if (sala[0]=="V" or sala[0]=="C" or sala[0]=="T"):
                        add = [sala]    # Se crea la estructura de distribucion comenzando por el nodo inicial
                        cant = 3 if sala[0]=="T" else 4     # Si la sala es una trampa la cantidad de conexiones
                        for i in range(1,cant):
                            number = self.aleatorio.randrange(1,limit-1)    # Se determina un numero aleatorio de la sala por conectar
                            status=0
                            for distri in self.dist:
                                for date in distri:     # Revisar si el la sala ya se uso mas de 4 o mas veces
                                    if date == self.nodos[number]:
                                        print(date)
                                        status+=1
                                        continue
                                    else:
                                        continue
                            # print(status)
                            if(status>=4):
                                print("supera los 4")
                                continue    # Si el nodo por agregar ya esta enlistado no se agregara
                            else:
                                if number==self.nodos.index(sala):
                                    break    # Si se intenta agregar el mismo nodo se cancela
                                else:
                                    # Se crea la distribucion del nodo
                                    if self.nodos[number] in add:
                                        i-=1
                                        continue
                                    add.append(self.nodos[number])
                        # Se agrega la distribucion a la lista
                        print(add)
                        self.dist.append(add)
        # Se agregan los nodos en base a las distribuciones
        for nodo in self.dist:
            for i in range(2,len(nodo)):
                self.mapa.add_edge(nodo[0],nodo[i])
        self.clear()


algo = Mazmorras(1)
algo.set_map_size()
print(max(dict(algo.mapa.degree()).values()))
algo.show_nodes()