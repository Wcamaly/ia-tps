import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self, image_path, compress = 128):
        self.image_path = image_path
        self.compress = compress

    def load_image(self):
        self.image = Image.open(self.image_path).convert('L') # Convertir a escala de grises
        self.image = self.image.resize((self.compress, self.compress), Image.ANTIALIAS)
        self.image_array = np.array(self.image)

    def process_image(self):
        # Normalizar los valores a 0-1
        self.image_array = self.image_array / 255
        # Convertir los valores a -1 y 1
        self.image_array = (self.image_array - 0.5) * 2
        self.image_array = np.where(self.image_array > 0, 1, -1)
        self.vectorized_image = self.image_array.flatten() # Aplanar a un vector

    def reconstruct_image(self, vector):
        reconstructed_array = vector.reshape(self.image_array.shape) # Volver a la forma original
        reconstructed_array = reconstructed_array * 255 # Desnormalizar
        self.reconstructed_image = Image.fromarray(reconstructed_array.astype(np.uint8)) # Convertir a una imagen

    def save_reconstructed_image(self, path):
        self.reconstructed_image.save(path)

    def show_image(self):
        plt.imshow(self.image_array, cmap='gray')
        plt.show()

    def show_reconstructed_image(self):
        plt.imshow(self.reconstructed_image, cmap='gray')
        plt.show()

    def get_vectorized_image(self):
        return self.vectorized_image