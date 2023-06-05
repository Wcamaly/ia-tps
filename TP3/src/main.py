import os
from datetime import datetime
# Cargar y procesar la imagen
from hopfield_network import HopfieldNetwork
from image import ImageProcessor

directory = os.path.join(os.getcwd(), 'assets/train')


images = os.listdir(directory)
images = filter(lambda f: f.lower().endswith(('.jpg', '.jpeg', '.png')), images)


size = 50 # puede cambiarse por el valor que guste

# Inicializar la red de Hopfield debe tomar el tamano de la matriz de la imagen aplanada es decir M x N
hopfield_network = HopfieldNetwork(size*size)


print(f"Comienzo de entrenamiento {datetime.now()}")
## Entrenamiento de la red de hopfiel
for image in images:
  processor = ImageProcessor(os.path.join(directory, image), size )
  processor.load_image()
  processor.process_image()
  vector = processor.get_vectorized_image()
  # Entrenar la red de Hopfield
  hopfield_network.train([vector]) # Nota: El método 'train' espera una lista de imágenes
print (f"Finalizado de entrenamiento {datetime.now()} ")
print (f"Matriz pivot")
print (hopfield_network.getWeight())

## Comienzo de prediccion 
processor = ImageProcessor(os.path.join(os.getcwd(), 'assets/predict/borrador-lapis.png'), size )
processor.load_image()
processor.process_image()
vector = processor.get_vectorized_image()

# Predecir utilizando la red de Hopfield
output_vector = hopfield_network.predict(vector)

# Reconstruir la imagen
processor.reconstruct_image(output_vector)
processor.save_reconstructed_image(os.path.join(os.getcwd(), 'assets/output/output.png'))

processor.show_image()
processor.show_reconstructed_image() 