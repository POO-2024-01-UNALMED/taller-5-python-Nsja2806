from zooAnimales.animal import Animal

class Zona:

  def __init__(self, nombre, zoo=None):
    self._nombre = nombre
    self._zoo = zoo
    self._animales = []

  def getNombre(self):
    return self._nombre

  def setNombre(self, nNombre):
    self._nombre = nNombre

  def getZoo(self):
    return self._zoo

  def setZoo(self, Nzoo):
    self._zoo = Nzoo

  def agregarAnimales(self, animal):
    self._animales.append(animal)

  def cantidadAnimales(self):
    return len(self._animales)