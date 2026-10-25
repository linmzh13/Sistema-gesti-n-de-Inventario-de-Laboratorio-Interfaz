class Encargado:

  def __init__(self, id, cuenta, password, correo, rol):
    self.id = id
    self.cuenta = cuenta
    self.password = password
    self.correo = correo
    self.rol = rol

  def consultar_inventario(self, equipos):
    print("\n--- INVENTARIO (ENCARGADO) ---")
    for equipo in equipos:
      equipo.consultar_inventario()

  def registrar_equipo(self, equipos, equipo):
    equipos.append(equipo)
    print("Equipo registrado exitosamente.")

  def registrar_persona(self, lista_personas, persona):
    lista_personas.append(persona)
    print("Persona registrada exitosamente.")

  def consultar_estudiante(self, estudiantes):
    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for est in estudiantes:
      print(
          f"ID: {est.id} | Nombre: {est.nombre} | Correo: {est.correo} |"
          f" Teléfono: {est.telefono}"
      )