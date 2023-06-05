from robot import Robot
from search import Search


def main():
    
    ###### Busqueda Exahustiva
    print(f"################## Busqueda Exahustiva ################## ")
    # Crear una lista de posiciones para los bloques
    eblosck_positions = [(5, 5), (1,2), (3,4), (7,6), (0,2)]
    # Crear un nuevo robot en la posición inicial (0, 0)
    erobot = Robot(0, 0)

    for block_position in eblosck_positions:
      # Imprimir la posición inicial del robot
      print(f"Posición inicial del robot: {erobot.get_current_position()}")    
      # Intentar montar el bloque (debería fallar porque el robot no está en la misma posición que el bloque)
      print(f"¿Puede montar el bloque en la posición actual? {erobot.can_mount(block_position)}")
      # Usar la búsqueda exhaustiva para encontrar la posición del bloque
      Search.exhaustive_search(erobot, block_position)
      # Imprimir la posición final del robot después de la búsqueda exhaustiva
      print(f"Posición final del robot después de la búsqueda exhaustiva: {erobot.get_current_position()}")
      # Intentar montar el bloque (ahora debería tener éxito)
      print(f"¿Puede montar el bloque en la nueva posición? {erobot.can_mount(block_position)}")
      print(f"-------------------------------END------------------------------------------ \n\n")



    ####### BUSQUEDA HEURISTICA
    print(f"################## Busqueda Heuristica ################## ")
    # Crear una lista de posiciones para los bloques
    hblock_positions = [(5, 5), (1,2), (3,4), (7,6), (0,2)]
    # Crear un nuevo robot en la posición inicial (0, 0)
    hrobot = Robot(0, 0)

    for block_position in hblock_positions:
      # Imprimir la posición inicial del robot
      print(f"Posición inicial del robot: {hrobot.get_current_position()}")    
      # Intentar montar el bloque (debería fallar porque el robot no está en la misma posición que el bloque)
      print(f"¿Puede montar el bloque en la posición actual? {hrobot.can_mount(block_position)}")
      # Usar la búsqueda exhaustiva para encontrar la posición del bloque
      Search.best_first_search(hrobot, block_position)
      # Imprimir la posición final del robot después de la búsqueda exhaustiva
      print(f"Posición final del robot después de la búsqueda exhaustiva: {hrobot.get_current_position()}")
      # Intentar montar el bloque (ahora debería tener éxito)
      print(f"¿Puede montar el bloque en la nueva posición? {hrobot.can_mount(block_position)}")
      print(f"-------------------------------END------------------------------------------ \n\n")

    

    
    

    


if __name__ == "__main__":
    main()