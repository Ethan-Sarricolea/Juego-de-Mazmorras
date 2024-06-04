"""
Descripcion: Iniciador de proyecto
Autor: Ethan Yahel Sarricolea Cortés Ethan
"""

from ui import gui

try:
    if __name__=="__main__":
        app = gui.Game()
        app.run()
except Exception as e:
    print("Error al ejecutar: ",e)
finally:
    print("Fin de la ejecución")