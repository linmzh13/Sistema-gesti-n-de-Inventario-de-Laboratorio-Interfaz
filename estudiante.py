from base_datos import registrar_prestamo_bd


class Estudiante:

  def __init__(self, id, nombre, password, correo, rol, telefono):
    self.id = id
    self.nombre = nombre
    self.password = password
    self.correo = correo
    self.rol = rol
    self.telefono = telefono

  def consultar_inventario(self, equipos):
    print("\n--- INVENTARIO ---")
    for equipo in equipos:
      equipo.consultar_inventario()

  def solicitar_prestamo(self, equipo):
    exito = equipo.solicitar_prestamo(self)
    if exito:
      registrar_prestamo_bd(self.id, equipo.id)
      print(
          f"Préstamo del equipo {equipo.nombre} registrado para {self.nombre}."
      )
    else:
      print("El equipo no está disponible para préstamo.")
    return exito

  def actualizar_info(self, correo, telefono):
    self.correo = correo
    self.telefono = telefono
    print("Información actualizada correctamente.")

  def consultar_equipo(self, equipo):
    equipo.consultar_estado()