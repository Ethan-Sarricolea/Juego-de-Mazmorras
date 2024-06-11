# Juego-de-Mazmorras

## Sarricolea Cortés Ethan Yahel

Juego decisiones donde debes recorrer una mazmorra generada de manera aleatoria

## Funcionamiento

Al crear la mazmorra se crean conexiones de manera "aleatoria" entre los nodos, esto basado en ciertas reglas.

- Un nodo entrada ("E") debe tener al menos de 1 a 4 conexiones
- todos los nodos deben tener un maximo de 4 conexiones
- Los nodos de salida ("S") una cantidad aleatoria menor a la cantidad de entradas y no se conectaran a las trampas

### Nivel 1 / facil (recomendado)

Consta de un maximo de 8 salas, 3 de ellas vacias, 1-3 salas de cofre o trampa, una entrada y una salida.

###### Suceptible a errores de generación en 2 de cada 10 ocasiones

### Nivel 2 / intermedio

Consta de un maximo de 14 salas, 6 de ellas vacias, 1-6 salas de cofre o trampa, una entrada y una salida

###### Es suceptible a errores de conexion y de genetracion que exceden el limite extablecido, 4 de cada 10 aproximadamente.

### Nivel 3 / Dificil

Consta de un maximo de 20 salas, 9 de ellas vacias, 1-9 salas de cofre o trampa, una entrada y una salida.

##### Es suceptible a errores y generar una repeticion en la generacion, aproximadamente 1 de cada 5 generaciones genera errores que llevan a la disminucion del nivel o a una generacion excesiva de conexiones entre nodos

## Reglas de juego

El jugador comienza en la sala de entrada, donde debe pasar por la menor cantidad de salas hasta llegar a la salida con la mayor cantidad de puntos posibles.

## Mapa

- Sala de Entrada: Aqui es donde comienza el jugador.

- Salida: En esta sala el jugador tiene la opcion de terminar con la partida o continuar por mas salas

- Sala vacia: Estas salas no tienen ningun efecto o recompensa para el jugador

- Sala de cofre: Al entrar en una de estas salas por primera ves el jugador ganara 50 puntos

- Sala trampa: Al pasar por una de estas salas el jugador perdera 10 puntos


## Como jugar

- Al abrir la aplicacion selecciona el nivel de tamaño de mapa (Recuerda que los niveles 2 y 3 son mas propensos a errores de generacion).

- Inicia el juego con el boton verde

- Se te mostrara el mapa de la mazmorra que debes recorrer, tendras que tratar de guiarte de este para llegar a la salida, pero los caminos a las salas no seran faciles de identificar.

- Selecciona la puerta de creas la indicada para moverte entre las habitaciones

- Al llegar a la salida esto se te indicara en pantalla y podrás decidir si continuar explorando terminar la partida


# Ejecucion

Clona el repositorio con el siguiente comando en terminal:

    git clone https://github.com/Ethan-Sarricolea/Juego-de-Mazmorras.git

Abre la carpeta de descarga y desplazate a esta desde la terminal

    cd Juego-de-Mazmorras

Ejecuta el archivo main.py para abrir el juego:

    python main.py

## Dependencias:

- networkX
- matplotlib