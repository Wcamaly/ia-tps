import heapq


class Search:
  @staticmethod
  def exhaustive_search(robot, block_position, limit=(0,10)):
    for x in range(limit[0], limit[1]):
        for y in range(limit[0], limit[1]):
            robot.set_position(x,y)
            if robot.can_mount(block_position):
                print(f"Encontrado el bloque en la posición {block_position}!")
                return
    print("No se encontró el bloque.")

  @staticmethod
  def best_first_search(robot, block_position, limit=(0,10)):
      # Inicializar la cola de prioridad con la posición actual del robot
      queue = [(Search.manhattan_distance(robot.get_current_position(), block_position), robot.get_current_position())]
      
      # Para evitar visitar una posición que ya hemos visitado
      visited = set()
      
      # Mientras haya posiciones sin visitar en la cola
      while queue:
          # Obtener la posición con el menor valor heurístico
          _, current_position = heapq.heappop(queue)
          
          # Si ya hemos visitado esta posición, la ignoramos
          if current_position in visited:
            continue
          
          # Marcamos la posición actual como visitada
          visited.add(current_position)
          
          # Mover el robot a la posición actual
          robot.set_position(*current_position)
          
          # Si el robot puede montar el bloque en esta posición, hemos terminado
          if robot.can_mount(block_position):
            print(f"Encontrado el bloque en la posición {block_position}!")
            return
          
          # Si no, agregar todas las posiciones vecinas a la cola
          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_position = (current_position[0] + dx, current_position[1] + dy)
            
            # Solo considerar posiciones dentro del límite y que aún no hayamos visitado
            if limit[0] <= new_position[0] < limit[1] and limit[0] <= new_position[1] < limit[1]:
              # El valor heurístico es la distancia de Manhattan hasta el bloque
              heuristic_value = Search.manhattan_distance(new_position, block_position)
              heapq.heappush(queue, (heuristic_value, new_position))
      
      print("No se encontró el bloque.")

  @staticmethod
  def manhattan_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])
