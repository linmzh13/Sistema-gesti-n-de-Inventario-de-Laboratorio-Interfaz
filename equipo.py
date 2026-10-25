class Equipo:

  def __init__(self, id, nombre, cantidad, estado):
    self.id = id
    self.nombre = nombre
    self.cantidad = cantidad
    self.estado = estado

  def consultar_inventario(self):
    print("ID:", self.id)
    print("Nombre:", self.nombre)
    print("Cantidad:", self.cantidad)
    print("Estado:", self.estado)

  def solicitar_prestamo(self, estudiante):
    if self.cantidad > 0 and self.estado == "Disponible":
      self.cantidad = self.cantidad - 1
      if self.cantidad == 0:
        self.estado = "No disponible"
      return True
    return False

  def actualizar_info(self, nombre, cantidad):
    self.nombre = nombre
    self.cantidad = cantidad
    if self.cantidad > 0:
      self.estado = "Disponible"
    else:
      self.estado = "No disponible"

  def consultar_estado(self):
    print("Estado del equipo:", self.estado)

  def devolver_equipo(self):
    self.cantidad += 1
    if self.cantidad > 0:
      self.estado = "Disponible"