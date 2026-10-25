# Sistema-Gestion-de-Inventario-de-Laboratorio-Interfaz

Aplicación de escritorio desarrollada en **Python** para la administración eficiente de recursos, control de inventario, registro de usuarios, gestión de préstamos y devoluciones de equipos en un laboratorio de electrónica. El sistema cuenta con una interfaz gráfica moderna (Tkinter) y una versión alternativa por consola, respaldadas por persistencia de datos local mediante **SQLite**.

### Control por Roles
* **Encargado**: 
  * Registro y gestión de equipos en el inventario.
  * Consulta del inventario global y estados de los equipos.
  * Registro de nuevos estudiantes y supervisión de préstamos activos.
* **Estudiante**: 
  * Consulta del catálogo de equipos disponibles.
  * Solicitud de préstamos de equipos.
  * Visualización y devolución de equipos en préstamo (actualizando automáticamente el stock).
  * Actualización de datos personales (correo y teléfono).

## Estructura del Proyecto

El código fuente se encuentra modularizado en los siguientes archivos dentro del directorio del proyecto:

```text
Proyecto-Inventario/
 gui.py              # Interfaz gráfica principal de la aplicación (Tkinter)
 main.py             # Versión alternativa de ejecución por consola
 base_datos.py       # Gestión de conexión, creación de tablas y consultas SQLite
 encargado.py        # Lógica y métodos correspondientes al rol de Encargado
 estudiante.py       # Lógica y métodos correspondientes al rol de Estudiante
 equipo.py           # Lógica y gestión de los equipos de laboratorio
 laboratorio.db      # Archivo de base de datos SQLite (almacena la información)
