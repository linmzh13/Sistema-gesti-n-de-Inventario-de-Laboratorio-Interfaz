import sqlite3

def crear_base_datos():
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            cantidad INTEGER,
            estado TEXT
        )
    """)

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            password TEXT,
            correo TEXT,
            rol TEXT,
            telefono TEXT
        )
    """)

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS encargados (
            id TEXT PRIMARY KEY,
            cuenta TEXT,
            password TEXT,
            correo TEXT,
            rol TEXT
        )
    """)

  # Nueva tabla para registrar qué estudiante tiene qué equipo
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS prestamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_estudiante TEXT,
            id_equipo TEXT,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            estado TEXT DEFAULT 'Activo'
        )
    """)

  conn.commit()
  conn.close()


def guardar_equipo(equipo):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT OR REPLACE INTO equipos (id, nombre, cantidad, estado)
        VALUES (?, ?, ?, ?)
    """,
      (equipo.id, equipo.nombre, equipo.cantidad, equipo.estado),
  )
  conn.commit()
  conn.close()


def actualizar_equipo(equipo):
  guardar_equipo(equipo)


def guardar_estudiante(estudiante):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT OR REPLACE INTO estudiantes (id, nombre, password, correo, rol, telefono)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
      (
          estudiante.id,
          estudiante.nombre,
          estudiante.password,
          estudiante.correo,
          estudiante.rol,
          estudiante.telefono,
      ),
  )
  conn.commit()
  conn.close()


def actualizar_estudiante(estudiante):
  guardar_estudiante(estudiante)


def guardar_encargado(encargado):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT OR REPLACE INTO encargados (id, cuenta, password, correo, rol)
        VALUES (?, ?, ?, ?, ?)
    """,
      (
          encargado.id,
          encargado.cuenta,
          encargado.password,
          encargado.correo,
          encargado.rol,
      ),
  )
  conn.commit()
  conn.close()


def registrar_prestamo_bd(id_estudiante, id_equipo):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT INTO prestamos (id_estudiante, id_equipo, estado)
        VALUES (?, ?, 'Activo')
    """,
      (id_estudiante, id_equipo),
  )
  conn.commit()
  conn.close()


def cargar_equipos():
  from equipo import Equipo

  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id, nombre, cantidad, estado FROM equipos")
  filas = cursor.fetchall()
  conn.close()
  return [Equipo(f[0], f[1], f[2], f[3]) for f in filas]


def cargar_estudiantes():
  from estudiante import Estudiante

  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      "SELECT id, nombre, password, correo, rol, telefono FROM estudiantes"
  )
  filas = cursor.fetchall()
  conn.close()
  return [Estudiante(f[0], f[1], f[2], f[3], f[4], f[5]) for f in filas]


def cargar_encargados():
  from encargado import Encargado

  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute("SELECT id, cuenta, password, correo, rol FROM encargados")
  filas = cursor.fetchall()
  conn.close()
  return [Encargado(f[0], f[1], f[2], f[3], f[4]) for f in filas]


def cargar_prestamos_activos():
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute("""
        SELECT p.id, p.id_estudiante, e.nombre, p.id_equipo, eq.nombre, p.fecha 
        FROM prestamos p
        JOIN estudiantes e ON p.id_estudiante = e.id
        JOIN equipos eq ON p.id_equipo = eq.id
        WHERE p.estado = 'Activo'
    """)
  filas = cursor.fetchall()
  conn.close()
  return filas

def cargar_prestamos_por_estudiante(id_estudiante):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        SELECT p.id, p.id_equipo, eq.nombre, p.fecha 
        FROM prestamos p
        JOIN equipos eq ON p.id_equipo = eq.id
        WHERE p.id_estudiante = ? AND p.estado = 'Activo'
    """,
      (id_estudiante,),
  )
  filas = cursor.fetchall()
  conn.close()
  return filas

def devolver_prestamo_bd(id_prestamo):
  conn = sqlite3.connect("laboratorio.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        UPDATE prestamos SET estado = 'Devuelto' WHERE id = ?
    """,
      (id_prestamo,),
  )
  conn.commit()
  conn.close()