import numpy as np


class HopfieldNetwork:
    def __init__(self, dim):
        self.dim = dim
        self.weights = np.zeros((dim, dim))

    def getWeight (self): 
      print(self.weights)

    def train(self, data):
        for i in range(self.dim):
            for j in range(i, self.dim):
                if i == j:
                    self.weights[i, j] = 0
                else:
                    weight = np.sum([image[i] * image[j] for image in data])
                    self.weights[i, j] = weight
                    self.weights[j, i] = weight

    def predict(self, data, iterations=10):
      for iteration in range(iterations):
          for i in range(self.dim):
              output = np.dot(self.weights[i], data)
              data[i] = 1 if output >= 0 else -1
      return data