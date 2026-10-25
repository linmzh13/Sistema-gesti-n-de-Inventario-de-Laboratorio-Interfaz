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

El código fuente se encuentra los siguientes archivos dentro del directorio del proyecto:

 interfaz.py              # Interfaz gráfica principal de la aplicación (Tkinter)
 main.py             # Versión alternativa de ejecución por consola
 base_datos.py       # Gestión de conexión, creación de tablas y consultas SQLite
 encargado.py        # Lógica y métodos correspondientes al rol de Encargado
 estudiante.py       # Lógica y métodos correspondientes al rol de Estudiante
 equipo.py           # Lógica y gestión de los equipos de laboratorio
 laboratorio.db      # Archivo de base de datos SQLite (almacena la información)

## Instalación y Ejecución

Descarga este repositorio asegurándote de mantener todos los archivos fuente en una misma carpeta.

Abre tu terminal o entorno de desarrollo (por ejemplo, VS Code) apuntando al directorio del proyecto.

 * Ejecuta la Interfaz Gráfica con el siguiente archivo: interfaz.py

 * Si deseas probar la versión basada en consola de texto, ejecuta: main.py

 * El archivo laboratorio.db contiene la persistencia de los datos registrados (usuarios, equipos y préstamos).
   Los datos registrados se pueden visualizar al abrir el archivo en la aplicación de SQLite.
