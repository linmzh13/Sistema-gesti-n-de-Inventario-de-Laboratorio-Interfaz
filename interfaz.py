import tkinter as tk
from tkinter import messagebox, ttk

from base_datos import (
    actualizar_equipo,
    actualizar_estudiante,
    cargar_encargados,
    cargar_estudiantes,
    cargar_equipos,
    cargar_prestamos_activos,
    cargar_prestamos_por_estudiante,
    crear_base_datos,
    devolver_prestamo_bd,
    guardar_encargado,
    guardar_equipo,
    guardar_estudiante,
)
from encargado import Encargado
from equipo import Equipo
from estudiante import Estudiante

crear_base_datos()
equipos = cargar_equipos()
estudiantes = cargar_estudiantes()
encargados = cargar_encargados()


def buscar_equipo(id_equipo):
  for equipo in equipos:
    if equipo.id == id_equipo:
      return equipo
  return None


class AppInventario:

  def __init__(self, root):
    self.root = root
    self.root.title("Sistema de Gestión - Lab de Electrónica")
    self.root.geometry("900x640")
    self.root.config(bg="#95A7B8")

    self.style = ttk.Style()
    self.style.theme_use("clam")

    self.COLOR_BG = "#004F9D"
    self.COLOR_PRIMARY = "#9f6cdd"
    self.COLOR_SUCCESS = "#C364D0"
    self.COLOR_DANGER = "#50001f"
    self.COLOR_DARK = "#05060A"

    self.style.configure("TNotebook", background=self.COLOR_BG, borderwidth=0)
    self.style.configure(
        "TNotebook.Tab",
        font=("Segoe UI", 10, "bold"),
        padding=[14, 8],
        background="#af7fea",
        foreground="#000000",
    )
    self.style.map(
        "TNotebook.Tab",
        background=[("selected", self.COLOR_PRIMARY)],
        foreground=[("selected", "#ffffff")],
    )

    self.style.configure(
        "Treeview",
        font=("Segoe UI", 10),
        rowheight=28,
        background="#ffffff",
        fieldbackground="#ffffff",
        foreground=self.COLOR_DARK,
    )
    self.style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        background="#e2e8f0",
        foreground=self.COLOR_DARK,
        relief="flat",
    )

    self.mostrar_menu_principal()

  def limpiar_ventana(self):
    for widget in self.root.winfo_children():
      widget.destroy()

  def mostrar_menu_principal(self):
    self.limpiar_ventana()

    card = tk.Frame(
        self.root, bg="#ffffff", bd=0, highlightbackground="#e2e8f0", highlightthickness=1
    )
    card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=380)

    tk.Label(
        card,
        text="LABORATORIO DE ELECTRÓNICA",
        font=("Segoe UI", 18, "bold"),
        bg="#ffffff",
        fg="#093c83",
    ).pack(pady=(35, 5))
    tk.Label(
        card,
        text="Sistema de Gestión de Inventario",
        font=("Segoe UI", 10),
        bg="#ffffff",
        fg="#093c83",
    ).pack(pady=(0, 25))

    tk.Button(
        card,
        text="Acceso Encargado",
        font=("Segoe UI", 12, "bold"),
        bg=self.COLOR_PRIMARY,
        fg=self.COLOR_DARK,
        activebackground="#6b05a1",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        width=26,
        height=2,
        command=lambda: self.mostrar_login("Encargado"),
    ).pack(pady=8)

    tk.Button(
        card,
        text="Acceso Estudiante",
        font=("Segoe UI", 12, "bold"),
        bg=self.COLOR_SUCCESS,
        fg=self.COLOR_DARK,
        activebackground="#8c0091",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        width=26,
        height=2,
        command=lambda: self.mostrar_login("Estudiante"),
    ).pack(pady=8)

    tk.Button(
        card,
        text="Salir",
        font=("Segoe UI", 9),
        bg=self.COLOR_DANGER,
        fg="white",
        activebackground="#740034",
        bd=0,
        cursor="hand2",
        width=26,
        height=1,
        command=self.root.quit,
    ).pack(pady=(12, 0))

  def mostrar_login(self, tipo_usuario):
    self.limpiar_ventana()

    card = tk.Frame(
        self.root, bg="#ffffff", bd=0, highlightbackground="#e2e8f0", highlightthickness=1
    )
    card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=500)

    tk.Button(
        card,
        text="← Volver",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#64748b",
        bd=0,
        cursor="hand2",
        command=self.mostrar_menu_principal,
    ).pack(anchor="w", padx=30, pady=(15, 0))

    tk.Label(
        card,
        text=f"Iniciar Sesión\n{tipo_usuario}",
        font=("Segoe UI", 14, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
        justify="center",
    ).pack(pady=(5, 10))

    tk.Label(
        card,
        text="ID de Usuario",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#475569",
    ).pack(anchor="w", padx=45)
    entry_id = tk.Entry(
        card, font=("Segoe UI", 11), bg="#f1f5f9", bd=0, relief="flat"
    )
    entry_id.pack(fill="x", padx=45, ipady=5, pady=(2, 8))

    tk.Label(
        card,
        text="Contraseña",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#475569",
    ).pack(anchor="w", padx=45)

    pass_frame = tk.Frame(card, bg="#f1f5f9")
    pass_frame.pack(fill="x", padx=45, pady=(2, 10))

    entry_pass = tk.Entry(
        pass_frame,
        font=("Segoe UI", 11),
        show="*",
        bg="#f1f5f9",
        bd=0,
        relief="flat",
    )
    entry_pass.pack(
        side="left", fill="both", expand=True, ipady=5, padx=(8, 0)
    )

    pass_visible = [False]

    def toggle_password():
      if pass_visible[0]:
        entry_pass.config(show="*")
        btn_toggle.config(text="👁")
        pass_visible[0] = False
      else:
        entry_pass.config(show="")
        btn_toggle.config(text="👁")
        pass_visible[0] = True

    btn_toggle = tk.Button(
        pass_frame,
        text="👁",
        font=("Segoe UI", 10),
        bg="#f1f5f9",
        fg=self.COLOR_DARK,
        bd=0,
        cursor="hand2",
        command=toggle_password,
    )
    btn_toggle.pack(side="right", padx=8)

    def validar():
      uid = entry_id.get().strip()
      pwd = entry_pass.get().strip()

      if tipo_usuario == "Encargado":
        usuario = next(
            (e for e in encargados if e.id == uid and e.password == pwd), None
        )
      else:
        usuario = next(
            (s for s in estudiantes if s.id == uid and s.password == pwd), None
        )

      if usuario:
        if tipo_usuario == "Encargado":
          self.mostrar_panel_encargado(usuario)
        else:
          self.mostrar_panel_estudiante(usuario)
      else:
        messagebox.showerror("Error", "ID o contraseña incorrectos.")

    tk.Button(
        card,
        text="Ingresar",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_PRIMARY,
        fg="white",
        activebackground="#6b05a1",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=validar,
    ).pack(fill="x", padx=45, ipady=5, pady=(2, 5))

    tk.Button(
        card,
        text="Crear nuevo usuario",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        activebackground="#8c0091",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=lambda: self.mostrar_registro(tipo_usuario),
    ).pack(fill="x", padx=45, ipady=5, pady=(2, 5))

  def mostrar_registro(self, tipo_usuario):
    self.limpiar_ventana()

    card = tk.Frame(
        self.root, bg="#ffffff", bd=0, highlightbackground="#e2e8f0", highlightthickness=1
    )
    card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=540)

    tk.Label(
        card,
        text=f"Registro de {tipo_usuario}",
        font=("Segoe UI", 13, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(pady=(15, 10))

    form_frame = tk.Frame(card, bg="#ffffff")
    form_frame.pack(fill="x", padx=35)

    tk.Label(
        form_frame,
        text="ID:",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#475569",
    ).pack(anchor="w")
    e_id = tk.Entry(
        form_frame, font=("Segoe UI", 10), bg="#f1f5f9", bd=0, relief="flat"
    )
    e_id.pack(fill="x", ipady=4, pady=(2, 6))

    if tipo_usuario == "Encargado":
      tk.Label(
          form_frame,
          text="Nombre de usuario (Alias):",
          font=("Segoe UI", 9, "bold"),
          bg="#ffffff",
          fg="#475569",
      ).pack(anchor="w")
      e_extra = tk.Entry(
          form_frame, font=("Segoe UI", 10), bg="#f1f5f9", bd=0, relief="flat"
      )
      e_extra.pack(fill="x", ipady=4, pady=(2, 6))
    else:
      tk.Label(
          form_frame,
          text="Nombre completo:",
          font=("Segoe UI", 9, "bold"),
          bg="#ffffff",
          fg="#475569",
      ).pack(anchor="w")
      e_extra = tk.Entry(
          form_frame, font=("Segoe UI", 10), bg="#f1f5f9", bd=0, relief="flat"
      )
      e_extra.pack(fill="x", ipady=4, pady=(2, 6))

    tk.Label(
        form_frame,
        text="Contraseña:",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#475569",
    ).pack(anchor="w")

    pass_reg_frame = tk.Frame(form_frame, bg="#f1f5f9")
    pass_reg_frame.pack(fill="x", pady=(2, 6))

    e_pass = tk.Entry(
        pass_reg_frame,
        font=("Segoe UI", 10),
        show="*",
        bg="#f1f5f9",
        bd=0,
        relief="flat",
    )
    e_pass.pack(
        side="left", fill="both", expand=True, ipady=4, padx=(6, 0)
    )

    pass_reg_visible = [False]

    def toggle_reg_password():
      if pass_reg_visible[0]:
        e_pass.config(show="*")
        btn_reg_toggle.config(text="👁")
        pass_reg_visible[0] = False
      else:
        e_pass.config(show="")
        btn_reg_toggle.config(text="👁")
        pass_reg_visible[0] = True

    btn_reg_toggle = tk.Button(
        pass_reg_frame,
        text="👁",
        font=("Segoe UI", 10),
        bg="#f1f5f9",
        fg=self.COLOR_DARK,
        bd=0,
        cursor="hand2",
        command=toggle_reg_password,
    )
    btn_reg_toggle.pack(side="right", padx=6)

    tk.Label(
        form_frame,
        text="Correo:",
        font=("Segoe UI", 9, "bold"),
        bg="#ffffff",
        fg="#475569",
    ).pack(anchor="w")
    e_correo = tk.Entry(
        form_frame, font=("Segoe UI", 10), bg="#f1f5f9", bd=0, relief="flat"
    )
    e_correo.pack(fill="x", ipady=4, pady=(2, 6))

    if tipo_usuario == "Estudiante":
      tk.Label(
          form_frame,
          text="Teléfono:",
          font=("Segoe UI", 9, "bold"),
          bg="#ffffff",
          fg="#475569",
      ).pack(anchor="w")
      e_tel = tk.Entry(
          form_frame, font=("Segoe UI", 10), bg="#f1f5f9", bd=0, relief="flat"
      )
      e_tel.pack(fill="x", ipady=4, pady=(2, 6))

    def guardar():
      uid = e_id.get().strip()
      extra = e_extra.get().strip()
      pwd = e_pass.get().strip()
      correo = e_correo.get().strip()

      if not uid or not pwd:
        messagebox.showerror(
            "Error", "El ID y la contraseña son obligatorios."
        )
        return

      if tipo_usuario == "Encargado":
        nuevo = Encargado(uid, extra, pwd, correo, "Encargado")
        encargados.append(nuevo)
        guardar_encargado(nuevo)
      else:
        tel = e_tel.get().strip()
        nuevo = Estudiante(uid, extra, pwd, correo, "Estudiante", tel)
        estudiantes.append(nuevo)
        guardar_estudiante(nuevo)

      messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
      self.mostrar_login(tipo_usuario)

    tk.Button(
        card,
        text="Registrarse",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        activebackground="#8c0091",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        command=guardar,
    ).pack(fill="x", padx=35, ipady=5, pady=(8, 4))

    tk.Button(
        card,
        text="← Volver al menú principal",
        font=("Segoe UI", 9),
        bg="#ffffff",
        fg="#64748b",
        bd=0,
        cursor="hand2",
        command=self.mostrar_menu_principal,
    ).pack(pady=2)

  def mostrar_panel_encargado(self, encargado):
    self.limpiar_ventana()

    container = tk.Frame(self.root, bg=self.COLOR_BG)
    container.pack(fill="both", expand=True)

    top_bar = tk.Frame(container, bg="#ffffff", height=45)
    top_bar.pack(fill="x", side="top")
    tk.Label(
        top_bar,
        text=f"Panel de Encargado: {encargado.cuenta}",
        font=("Segoe UI", 10, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(side="left", padx=15)
    tk.Button(
        top_bar,
        text="Cerrar Sesión",
        font=("Segoe UI", 9),
        bg=self.COLOR_DANGER,
        fg="white",
        bd=0,
        cursor="hand2",
        command=self.mostrar_menu_principal,
    ).pack(side="right", padx=15, pady=8)

    notebook = ttk.Notebook(container)
    notebook.pack(fill="both", expand=True, padx=15, pady=15)

    tab_inv = ttk.Frame(notebook)
    notebook.add(tab_inv, text="Inventario de Equipos")

    tree = ttk.Treeview(
        tab_inv, columns=("ID", "Nombre", "Cantidad", "Estado"), show="headings"
    )
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre del Equipo")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Estado", text="Estado")
    tree.pack(fill="both", expand=True, padx=15, pady=15)

    def cargar_tabla_equipos():
      for row in tree.get_children():
        tree.delete(row)
      for eq in equipos:
        tree.insert("", "end", values=(eq.id, eq.nombre, eq.cantidad, eq.estado))

    cargar_tabla_equipos()
    tk.Button(
        tab_inv,
        text="Actualizar Vista",
        font=("Segoe UI", 9, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=cargar_tabla_equipos,
    ).pack(pady=(0, 15))

    tab_reg_eq = ttk.Frame(notebook)
    notebook.add(tab_reg_eq, text="Registrar Equipo")

    form_eq = tk.Frame(tab_reg_eq, bg="#ffffff", padx=25, pady=25)
    form_eq.place(relx=0.5, rely=0.5, anchor="center", width=400, height=320)

    tk.Label(
        form_eq,
        text="Nuevo Equipo",
        font=("Segoe UI", 12, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(anchor="w", pady=(0, 15))

    tk.Label(form_eq, text="ID del Equipo:", bg="#ffffff", font=("Segoe UI", 9)).pack(
        anchor="w"
    )
    e_ideq = tk.Entry(form_eq, font=("Segoe UI", 10), bg="#f1f5f9", bd=0)
    e_ideq.pack(fill="x", ipady=4, pady=(2, 8))

    tk.Label(
        form_eq, text="Nombre del Equipo:", bg="#ffffff", font=("Segoe UI", 9)
    ).pack(anchor="w")
    e_nomeq = tk.Entry(form_eq, font=("Segoe UI", 10), bg="#f1f5f9", bd=0)
    e_nomeq.pack(fill="x", ipady=4, pady=(2, 8))

    tk.Label(form_eq, text="Cantidad:", bg="#ffffff", font=("Segoe UI", 9)).pack(
        anchor="w"
    )
    e_canto = tk.Entry(form_eq, font=("Segoe UI", 10), bg="#f1f5f9", bd=0)
    e_canto.pack(fill="x", ipady=4, pady=(2, 12))

    def guardar_eq():
      try:
        id_e = e_ideq.get().strip()
        nom = e_nomeq.get().strip()
        cant = int(e_canto.get().strip())
        nuevo_eq = Equipo(id_e, nom, cant, "Disponible")
        encargado.registrar_equipo(equipos, nuevo_eq)
        guardar_equipo(nuevo_eq)
        messagebox.showinfo("Éxito", "Equipo registrado correctamente.")
        cargar_tabla_equipos()
        e_ideq.delete(0, tk.END)
        e_nomeq.delete(0, tk.END)
        e_canto.delete(0, tk.END)
      except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")

    tk.Button(
        form_eq,
        text="Guardar Equipo",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=guardar_eq,
    ).pack(fill="x", ipady=6)

    tab_reg_est = ttk.Frame(notebook)
    notebook.add(tab_reg_est, text="Registrar Estudiante")

    form_st = tk.Frame(tab_reg_est, bg="#ffffff", padx=25, pady=20)
    form_st.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

    tk.Label(
        form_st,
        text="Nuevo Estudiante",
        font=("Segoe UI", 12, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(anchor="w", pady=(0, 10))

    campos = [
        ("ID Estudiante:", False),
        ("Nombre completo:", False),
        ("Contraseña:", True),
        ("Correo electrónico:", False),
        ("Teléfono:", False),
    ]
    entries = {}

    for label, is_pwd in campos:
      tk.Label(form_st, text=label, bg="#ffffff", font=("Segoe UI", 9)).pack(
          anchor="w"
      )
      e = tk.Entry(
          form_st,
          font=("Segoe UI", 10),
          show="*" if is_pwd else "",
          bg="#f1f5f9",
          bd=0,
      )
      e.pack(fill="x", ipady=3, pady=(1, 6))
      entries[label] = e

    def guardar_est_desde_encargado():
      uid = entries["ID Estudiante:"].get().strip()
      nom = entries["Nombre completo:"].get().strip()
      pwd = entries["Contraseña:"].get().strip()
      correo = entries["Correo electrónico:"].get().strip()
      tel = entries["Teléfono:"].get().strip()

      if not uid or not nom or not pwd:
        messagebox.showerror(
            "Error", "ID, Nombre y Contraseña son obligatorios."
        )
        return

      nuevo_estudiante = Estudiante(uid, nom, pwd, correo, "Estudiante", tel)
      encargado.registrar_persona(estudiantes, nuevo_estudiante)
      guardar_estudiante(nuevo_estudiante)
      messagebox.showinfo("Éxito", "Estudiante registrado correctamente.")

      for e in entries.values():
        e.delete(0, tk.END)

    tk.Button(
        form_st,
        text="Guardar Estudiante",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=guardar_est_desde_encargado,
    ).pack(fill="x", ipady=6, pady=(10, 0))

    tab_prest = ttk.Frame(notebook)
    notebook.add(tab_prest, text="Préstamos Activos")

    tree_prestamos = ttk.Treeview(
        tab_prest,
        columns=("ID Préstamo", "ID Est.", "Estudiante", "ID Eq.", "Equipo"),
        show="headings",
    )
    tree_prestamos.heading("ID Préstamo", text="#")
    tree_prestamos.heading("ID Est.", text="ID Estudiante")
    tree_prestamos.heading("Estudiante", text="Nombre Estudiante")
    tree_prestamos.heading("ID Eq.", text="ID Equipo")
    tree_prestamos.heading("Equipo", text="Nombre Equipo")
    tree_prestamos.pack(fill="both", expand=True, padx=15, pady=15)

    def cargar_tabla_prestamos():
      for row in tree_prestamos.get_children():
        tree_prestamos.delete(row)
      prestamos = cargar_prestamos_activos()
      for p in prestamos:
        tree_prestamos.insert(
            "", "end", values=(p[0], p[1], p[2], p[3], p[4])
        )

    cargar_tabla_prestamos()
    tk.Button(
        tab_prest,
        text="Actualizar Préstamos",
        font=("Segoe UI", 9, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=cargar_tabla_prestamos,
    ).pack(pady=(0, 15))

  def mostrar_panel_estudiante(self, estudiante):
    self.limpiar_ventana()

    container = tk.Frame(self.root, bg=self.COLOR_BG)
    container.pack(fill="both", expand=True)

    top_bar = tk.Frame(container, bg="#ffffff", height=45)
    top_bar.pack(fill="x", side="top")
    tk.Label(
        top_bar,
        text=f"Panel de Estudiante: {estudiante.nombre}",
        font=("Segoe UI", 10, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(side="left", padx=15)
    tk.Button(
        top_bar,
        text="Cerrar Sesión",
        font=("Segoe UI", 9),
        bg=self.COLOR_DANGER,
        fg="white",
        bd=0,
        cursor="hand2",
        command=self.mostrar_menu_principal,
    ).pack(side="right", padx=15, pady=8)

    notebook = ttk.Notebook(container)
    notebook.pack(fill="both", expand=True, padx=15, pady=15)

    tab_inv = ttk.Frame(notebook)
    notebook.add(tab_inv, text="Inventario y Préstamos")

    tree = ttk.Treeview(
        tab_inv, columns=("ID", "Nombre", "Cantidad", "Estado"), show="headings"
    )
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre del Equipo")
    tree.heading("Cantidad", text="Cantidad")
    tree.heading("Estado", text="Estado")
    tree.pack(fill="both", expand=True, padx=15, pady=15)

    def cargar_tabla_est():
      for row in tree.get_children():
        tree.delete(row)
      for eq in equipos:
        tree.insert("", "end", values=(eq.id, eq.nombre, eq.cantidad, eq.estado))

    cargar_tabla_est()

    def pedir_prestamo():
      selected_item = tree.selection()
      if not selected_item:
        messagebox.showwarning(
            "Advertencia", "Seleccione un equipo de la tabla."
        )
        return
      item_data = tree.item(selected_item)
      id_eq = item_data["values"][0]
      eq = buscar_equipo(id_eq)

      if eq:
        exito = estudiante.solicitar_prestamo(eq)
        if exito:
          actualizar_equipo(eq)
          messagebox.showinfo("Éxito", f"Préstamo registrado para {eq.nombre}")
          cargar_tabla_est()
          cargar_tabla_mis_prestamos()
        else:
          messagebox.showerror("Error", "El equipo no se encuentra disponible.")

    tk.Button(
        tab_inv,
        text="Solicitar Préstamo de Equipo Seleccionado",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=pedir_prestamo,
    ).pack(pady=(0, 15), ipady=6)

    tab_devol = ttk.Frame(notebook)
    notebook.add(tab_devol, text="Mis Préstamos y Devoluciones")

    tree_mis_prestamos = ttk.Treeview(
        tab_devol,
        columns=("ID Préstamo", "ID Equipo", "Equipo", "Fecha"),
        show="headings",
    )
    tree_mis_prestamos.heading("ID Préstamo", text="# Préstamo")
    tree_mis_prestamos.heading("ID Equipo", text="ID Equipo")
    tree_mis_prestamos.heading("Equipo", text="Nombre del Equipo")
    tree_mis_prestamos.heading("Fecha", text="Fecha de Préstamo")
    tree_mis_prestamos.pack(fill="both", expand=True, padx=15, pady=15)

    def cargar_tabla_mis_prestamos():
      for row in tree_mis_prestamos.get_children():
        tree_mis_prestamos.delete(row)
      prestamos_est = cargar_prestamos_por_estudiante(estudiante.id)
      for p in prestamos_est:
        tree_mis_prestamos.insert("", "end", values=(p[0], p[1], p[2], p[3]))

    cargar_tabla_mis_prestamos()

    def devolver_equipo_estudiante():
      selected_item = tree_mis_prestamos.selection()
      if not selected_item:
        messagebox.showwarning(
            "Advertencia",
            "Seleccione de la tabla el préstamo que desea devolver.",
        )
        return

      item_data = tree_mis_prestamos.item(selected_item)
      id_prestamo = item_data["values"][0]
      id_equipo = item_data["values"][1]

      eq = buscar_equipo(id_equipo)
      if eq:
        eq.devolver_equipo()
        actualizar_equipo(eq)
        devolver_prestamo_bd(id_prestamo)
        messagebox.showinfo("Éxito", f"Equipo {eq.nombre} devuelto con éxito.")
        cargar_tabla_est()
        cargar_tabla_mis_prestamos()

    tk.Button(
        tab_devol,
        text="Devolver Equipo Seleccionado",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=devolver_equipo_estudiante,
    ).pack(pady=(0, 15), ipady=6)

    tab_info = ttk.Frame(notebook)
    notebook.add(tab_info, text="Actualizar Mis Datos")

    form_info = tk.Frame(tab_info, bg="#ffffff", padx=25, pady=25)
    form_info.place(relx=0.5, rely=0.5, anchor="center", width=380, height=280)

    tk.Label(
        form_info,
        text="Mis Datos Personales",
        font=("Segoe UI", 12, "bold"),
        bg="#ffffff",
        fg=self.COLOR_DARK,
    ).pack(anchor="w", pady=(0, 15))

    tk.Label(form_info, text="Nuevo Correo:", bg="#ffffff", font=("Segoe UI", 9)).pack(
        anchor="w"
    )
    e_correo = tk.Entry(form_info, font=("Segoe UI", 10), bg="#f1f5f9", bd=0)
    e_correo.insert(0, estudiante.correo)
    e_correo.pack(fill="x", ipady=4, pady=(2, 8))

    tk.Label(
        form_info, text="Nuevo Teléfono:", bg="#ffffff", font=("Segoe UI", 9)
    ).pack(anchor="w")
    e_tel = tk.Entry(form_info, font=("Segoe UI", 10), bg="#f1f5f9", bd=0)
    e_tel.insert(0, estudiante.telefono)
    e_tel.pack(fill="x", ipady=4, pady=(2, 12))

    def guardar_cambios():
      nuevo_c = e_correo.get().strip()
      nuevo_t = e_tel.get().strip()
      estudiante.actualizar_info(nuevo_c, nuevo_t)
      actualizar_estudiante(estudiante)
      messagebox.showinfo("Éxito", "Información actualizada correctamente.")

    tk.Button(
        form_info,
        text="Guardar Cambios",
        font=("Segoe UI", 10, "bold"),
        bg=self.COLOR_SUCCESS,
        fg="white",
        bd=0,
        cursor="hand2",
        command=guardar_cambios,
    ).pack(fill="x", ipady=6)


if __name__ == "__main__":
  root = tk.Tk()
  app = AppInventario(root)
  root.mainloop()