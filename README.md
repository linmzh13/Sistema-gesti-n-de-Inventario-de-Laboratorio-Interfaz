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

## Modelado UML

1. **Diagrama de Casos de Uso:**
   
<img width="399" height="365" alt="Captura de pantalla 2026-10-25 151719" src="https://github.com/user-attachments/assets/f92ae171-6cec-4328-bb1a-78447515e396" />


2. **Diagrama de Clases:**

<img width="338" height="373" alt="Captura de pantalla 2026-10-25 150413" src="https://github.com/user-attachments/assets/c472ecf8-32b5-4add-86bc-06eb0feda120" />


3. **Diagramas de Secuencias:**

**Inicio de sesión**

<img width="524" height="281" alt="Captura de pantalla 2026-10-26 115115" src="https://github.com/user-attachments/assets/3eeec087-ba48-40ce-b5c2-a098328717c9" />

**Solicitar préstamo**

<img width="549" height="329" alt="Captura de pantalla 2026-10-26 115202" src="https://github.com/user-attachments/assets/99d24ad7-6a94-4720-9399-aa2bd6fbc6f6" />


**Devolver equipo**

<img width="527" height="271" alt="Captura de pantalla 2026-10-26 115308" src="https://github.com/user-attachments/assets/f02dd628-afd4-4889-9265-135da014494c" />

