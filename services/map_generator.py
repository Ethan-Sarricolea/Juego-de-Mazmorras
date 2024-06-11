"""
Descripcion: Clase generadora de la mazmorra.
Autor: Sarricolea Cortés Ethan Yahel
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import gc


class Mazmorras:
    def __init__(self,level) -> None:
        self.nivel = level
        self.aleatorio = random.Random()
        self.mapa = nx.Graph()
        self.salas = ["E","S","V","C","T"]
        self.nodos = []
        self.dist = []
        self.errorCount = 0
    
    def set_map_size(self):
        #Crear y añadir los nodos
        if self.nivel==1:
            # Crear vacios y particulares
            self.create_rooms(3)
        elif self.nivel==2:
            self.create_rooms(6)
        elif self.nivel==3:
            self.create_rooms(9)
        fig, ax = plt.subplots()
        pos = nx.spring_layout(self.mapa)  # Posiciones de los nodos
        nx.draw(self.mapa,pos,with_labels=True, node_color='lightblue', node_size=500)
        labels = nx.get_node_attributes(self.mapa, 'id')
        fig.canvas.manager.set_window_title('Mapa')
        nx.draw_networkx_labels(self.mapa, pos, labels=labels)
            
    def create_rooms(self,maxSize):
        try:
            self.mapa.clear()
        except:
            print("mapa vacio")
        #creacion de la entrada
        for room in self.salas:
            if room=="E" or room=="S":
                # Agregar una entrada y una salida
                self.mapa.add_node(room)
                self.nodos.append(room)
            elif (room=="V"):
                # Agregar el numero maximo de salas vacias
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
            elif (room=="C"):
                #Agregar un numero aleatorio de cofres segun el maximo
                cant = self.aleatorio.randrange(1,3)
                maxSize -=cant
                for i in range(1,cant+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
            elif (room=="T"):
                # Agregar el numero restante de trampas segun el maximo
                for i in range(1,maxSize+1):
                    self.mapa.add_node(f"{room}{i}")
                    self.nodos.append(f"{room}{i}")
        self.conect_rooms(maxSize)

    def show_nodes(self) -> int:
        plt.show()

    def conect_rooms(self,level):
        try:
            size = 4
            clon = self.nodos[2:]
            mapa = dict()
            for data in clon:
                mapa.setdefault(data)
            # print(clon,mapa)
            for roomType in self.salas:
                if(roomType=="E"):
                    secondClon = clon
                    # print(secondClon)
                    for n in range(size):
                        sala = self.aleatorio.choice(secondClon)
                        mapa[sala] = 1 if mapa[sala]==None else mapa[sala]+1
                        secondClon.remove(sala)
                        # print(secondClon)
                        self.mapa.add_edge(roomType,sala)
                if roomType=="S":
                    lim = self.aleatorio.randrange(0,len(secondClon))
                    lim = 2 if lim>=size else lim
                    for n in range(-1,lim):
                        sala = self.aleatorio.choice(secondClon)
                        if sala[0]=="T":
                            secondClon.remove(sala)
                            sala = self.aleatorio.choice(secondClon)
                            mapa[sala] = 1 if mapa[sala]==None else mapa[sala]+1
                            # print(secondClon)
                            self.mapa.add_edge(roomType,sala)
                        else:
                            mapa[sala] = 1 if mapa[sala]==None else mapa[sala]+1
                            secondClon.remove(sala)
                            # print(secondClon)
                            self.mapa.add_edge(roomType,sala)
                elif roomType=="V":
                    clon = self.nodos[2:]
                    nodes = self.mapa.nodes
                    for node in nodes:
                        if self.mapa.degree(node)<4:
                            other = self.aleatorio.choice(clon)
                            if other!=node and self.mapa.degree(other)<4:
                                self.mapa.add_edge(node,other)
            nodos = self.mapa.nodes
            for nodes in nodos:
                if self.mapa.degree(nodes)==0:
                    self.mapa.remove_node(nodes)
            if max(dict(self.mapa.degree()).values())>4:
                raise TypeError
        except Exception as e:
            self.errorCount+=1
            gc.collect()    # Evitar saturar la memoria
            print(f"Error de generacion {e}")
            print("Realizando otro intento...")
            if self.errorCount>5:   # por mas de 5 intentos se disminuye el nivel
                self.nivel = ((level/3)-1)
                self.set_map_size()
            else:
                self.conect_rooms(level)
        # self.show_nodes()

    def get_camino(self):
        return nx.shortest_path(self.mapa, source='E', target='S', weight='weight')

    def get_node_degree(self,node="E"):
        return self.mapa.degree(node)

"""    def conect_rooms(self,limit) ->None:
        print("Coneccion")
        size = 4
        clon = self.nodos
        usos = []
        for data in clon:
            usos.append(0)
        print(clon,usos)
        # crear un clon del clon sin las los nodos innecesarios
        for roomType in self.nodos:
            if roomType=="E":
                extras = ["E","S"]
                key = [x for x in clon if x not in extras]
                number = self.aleatorio.randrange(0,len(key))
                adds = []
                for options in key:
                    #???

        print(clon,usos)"""
        
"""
        hacer un clon de la lista de nodos
        eliminar de la lista el nodo que tenga un grado igual o mayor a 4
        la entrada no puede conectarse a mas de una trampa
        la salida no puede conectarse a trampas

        agregar aristas individualmente
        
        """

"""    def clear(self):
        nodes_to_remove = [node for node in self.mapa.nodes if self.mapa.degree(node) == 0]
        for node in nodes_to_remove:
            self.mapa.remove_node(node)
            # Eliminar las conexiones de un nodo si tiene mas de 4

    def conect_rooms(self,limit) -> None:
        # print(self.nodos)
        # print(self.dist)
        finInIndex = 4
        for room in self.salas:
            print("ROOM:",room)
            if (room=="E"):
                add = [room]
                for n in range(finInIndex):
                    number = self.aleatorio.randrange(1,limit-1)
                    if self.nodos[number] in add:
                        while (self.nodos[number] in add):
                            number = self.aleatorio.randrange(1,limit-1)
                    add.append(self.nodos[number])
                # add = list(set(add))
                self.dist.append(add)
                print(add)
            elif (room=="S"):
                # Si es una sala vacia se agrega un numero aleatorio de conexiones entre 1 y 3
                add = [room]
                for n in range(finInIndex-1):
                    number = self.aleatorio.randrange(1,limit-1)
                    if self.nodos[number] in add:
                        while (self.nodos[number] in add):
                            number = self.aleatorio.randrange(1,limit-1)
                    add.append(self.nodos[number])
                self.dist.append(add)
                print(add)    
            elif (room=="V"):
                for sala in self.nodos:
                    print("sala:",sala)
                    # Si es una sala vacia, de cofre o trampa:
                    if (sala[0]=="V" or sala[0]=="C" or sala[0]=="T"):
                        add = [sala]
                        # cant = 3 if sala[0]=="T" else 4
                        cant = finInIndex
                        for i in range(1,cant):
                            number = self.aleatorio.randrange(1,limit-1)    # Se determina un numero aleatorio de la sala por conectar
                            status=0
                            for distri in self.dist:
                                for date in distri:     # Revisar si el la sala ya se uso mas de 4 o mas veces
                                    if date == self.nodos[number]:
                                        # print(date)
                                        status+=1
                                        continue
                                    else:
                                        continue
                            # print(status)
                            if(status>=4):
                                # print("supera los 4")
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
                        # print(add)
                        # add = list(set(add))
                        self.dist.append(add)
        print(self.dist)
        # Se agregan los nodos en base a las distribuciones
        for nodo in self.dist:
            for i in range(1,(len(nodo)-1 if len(nodo)>3 else len(nodo))):
                self.mapa.add_edge(nodo[0],nodo[i])
        self.clear()"""
    
"""algo = Mazmorras(1)
algo.set_map_size()
print("Grado maximo: ",max(dict(algo.mapa.degree()).values()))
print("Camino:",len(algo.get_camino())-1,algo.get_camino())
algo.show_nodes()"""