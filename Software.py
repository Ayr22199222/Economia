import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Función para calcular el interés simple
def calcular_interes_simple():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100
    t = float(entry_tiempo.get())
    interes_simple = P * r * t
    resultado.set(f"Interés simple: {interes_simple:.2f}")

# Función para calcular el interés compuesto
def calcular_interes_compuesto():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100
    t = float(entry_tiempo.get())
    n = float(entry_compuesto.get())
    monto_total = P * (1 + r / n) ** (n * t)
    interes_compuesto = monto_total - P
    resultado.set(f"Interés compuesto: {interes_compuesto:.2f}")

# Función para mostrar el gráfico comparativo
def mostrar_grafico():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100
    t = int(entry_tiempo.get())
    n = float(entry_compuesto.get())
    
    tiempo = np.arange(1, t + 1)
    interes_simple = P * r * tiempo
    interes_compuesto = P * (1 + r / n) ** (n * tiempo) - P
    
    plt.plot(tiempo, interes_simple, label="Interés Simple", color='blue')
    plt.plot(tiempo, interes_compuesto, label="Interés Compuesto", color='green')
    plt.title("Comparación entre Interés Simple y Compuesto")
    plt.xlabel("Tiempo (años)")
    plt.ylabel("Interés acumulado")
    plt.legend()
    plt.grid(True)
    plt.show()

# Función para calcular la amortización francesa
def calcular_amortizacion_francesa():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100 / 12  # Tasa mensual
    t = int(entry_tiempo.get()) * 12        # Tiempo en meses
    cuota = P * r / (1 - (1 + r) ** -t)     # Fórmula para calcular la cuota fija

    # Limpiar la tabla antes de mostrar nuevos datos
    for row in tree.get_children():
        tree.delete(row)

    saldo_pendiente = P
    for i in range(1, t + 1):
        interes = saldo_pendiente * r
        principal = cuota - interes
        saldo_pendiente -= principal
        tree.insert('', 'end', values=(i, f"{cuota:.2f}", f"{interes:.2f}", f"{principal:.2f}", f"{saldo_pendiente:.2f}"))

# Función para calcular la amortización alemana
def calcular_amortizacion_alemana():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100 / 12  # Tasa mensual
    t = int(entry_tiempo.get()) * 12        # Tiempo en meses
    amortizacion_principal = P / t          # Amortización constante del principal

    # Limpiar la tabla antes de mostrar nuevos datos
    for row in tree.get_children():
        tree.delete(row)

    saldo_pendiente = P
    for i in range(1, t + 1):
        interes = saldo_pendiente * r
        cuota = amortizacion_principal + interes
        saldo_pendiente -= amortizacion_principal
        tree.insert('', 'end', values=(i, f"{cuota:.2f}", f"{interes:.2f}", f"{amortizacion_principal:.2f}", f"{saldo_pendiente:.2f}"))

# Función para calcular la amortización americana
def calcular_amortizacion_americana():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100 / 12  # Tasa mensual
    t = int(entry_tiempo.get()) * 12        # Tiempo en meses

    # Limpiar la tabla antes de mostrar nuevos datos
    for row in tree.get_children():
        tree.delete(row)

    saldo_pendiente = P
    for i in range(1, t + 1):
        interes = saldo_pendiente * r
        cuota = interes
        tree.insert('', 'end', values=(i, f"{cuota:.2f}", f"{interes:.2f}", "0.00", f"{saldo_pendiente:.2f}"))
    # Agregar el pago del principal al final
    tree.insert('', 'end', values=("Final", f"{P:.2f}", "0.00", f"{P:.2f}", "0.00"))

# Función para calcular la anualidad vencida
def calcular_anualidad_vencida():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100
    t = float(entry_tiempo.get())
    anualidad = P * r / (1 - (1 + r) ** -t)
    resultado.set(f"Anualidad Vencida: {anualidad:.2f}")

# Función para calcular el gradiente aritmético
def calcular_gradiente_aritmetico():
    P = float(entry_principal.get())
    r = float(entry_tasa.get()) / 100
    t = float(entry_tiempo.get())
    gradiente = P * r * (t + 1) / 2
    resultado.set(f"Gradiente Aritmético: {gradiente:.2f}")

# Función para calcular la depreciación por línea recta
def calcular_depreciacion():
    P = float(entry_principal.get())
    t = int(entry_tiempo.get())
    depreciacion = P / t
    resultado.set(f"Depreciación Anual: {depreciacion:.2f}")

# Función para calcular el VAN
def calcular_van():
    P = float(entry_principal.get())
    t = int(entry_tiempo.get())
    r = float(entry_tasa.get()) / 100
    flujos = [P] + [float(entry_principal.get()) for _ in range(t)]
    van = sum(flujos[i] / (1 + r) ** i for i in range(t + 1))
    resultado.set(f"VAN: {van:.2f}")

# Función para calcular la TIR
def calcular_tir():
    P = float(entry_principal.get())
    t = int(entry_tiempo.get())
    r = float(entry_tasa.get()) / 100
    flujos = [P] + [float(entry_principal.get()) for _ in range(t)]
    fsolve(lambda r: sum(flujos[i] / (1 + r) ** i for i in range(t + 1)), 0.1)
    resultado.set(f"TIR: {r * 100:.2f}%")

# Función para calcular el PER
def calcular_per():
    P = float(entry_principal.get())
    t = int(entry_tiempo.get())
    flujo_operativo = float(entry_principal.get())
    per = P / flujo_operativo
    resultado.set(f"PER: {per:.2f}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Financiera")

# Personalizar colores y fuentes
root.configure(bg='#f1f1f1')
root.option_add("*Font", "Helvetica 10")
root.option_add("*Button*bg", "#4CAF50")
root.option_add("*Button*fg", "white")
root.option_add("*Button*relief", "flat")
root.option_add("*TButton*bg", "#4CAF50")
root.option_add("*TButton*fg", "white")

# Variables
resultado = tk.StringVar()

# Elementos de la interfaz gráfica
ttk.Label(root, text="Principal (P):", background="#f1f1f1").grid(column=0, row=0, padx=10, pady=5)
entry_principal = ttk.Entry(root)
entry_principal.grid(column=1, row=0, padx=10, pady=5)

ttk.Label(root, text="Tasa de interés (%):", background="#f1f1f1").grid(column=0, row=1, padx=10, pady=5)
entry_tasa = ttk.Entry(root)
entry_tasa.grid(column=1, row=1, padx=10, pady=5)

ttk.Label(root, text="Tiempo (años):", background="#f1f1f1").grid(column=0, row=2, padx=10, pady=5)
entry_tiempo = ttk.Entry(root)
entry_tiempo.grid(column=1, row=2, padx=10, pady=5)

ttk.Label(root, text="Compuesto (veces al año):", background="#f1f1f1").grid(column=0, row=3, padx=10, pady=5)
entry_compuesto = ttk.Entry(root)
entry_compuesto.grid(column=1, row=3, padx=10, pady=5)

# Botones
ttk.Button(root, text="Calcular Interés Simple", command=calcular_interes_simple).grid(column=0, row=4, padx=10, pady=10)
ttk.Button(root, text="Calcular Interés Compuesto", command=calcular_interes_compuesto).grid(column=1, row=4, padx=10, pady=10)
ttk.Button(root, text="Mostrar Gráfico Comparativo", command=mostrar_grafico).grid(column=0, row=5, columnspan=2, padx=10, pady=10)
ttk.Button(root, text="Amortización Francesa", command=calcular_amortizacion_francesa).grid(column=0, row=6, columnspan=2, padx=10, pady=10)
ttk.Button(root, text="Amortización Alemana", command=calcular_amortizacion_alemana).grid(column=0, row=7, columnspan=2, padx=10, pady=10)
ttk.Button(root, text="Amortización Americana", command=calcular_amortizacion_americana).grid(column=0, row=8, columnspan=2, padx=10, pady=10)

# Funciones adicionales
ttk.Button(root, text="Anualidad Vencida", command=calcular_anualidad_vencida).grid(column=0, row=9, padx=10, pady=10)
ttk.Button(root, text="Gradiente Aritmético", command=calcular_gradiente_aritmetico).grid(column=1, row=9, padx=10, pady=10)
ttk.Button(root, text="Depreciación Línea Recta", command=calcular_depreciacion).grid(column=0, row=10, padx=10, pady=10)
ttk.Button(root, text="VAN", command=calcular_van).grid(column=1, row=10, padx=10, pady=10)
ttk.Button(root, text="TIR", command=calcular_tir).grid(column=0, row=11, padx=10, pady=10)
ttk.Button(root, text="PER", command=calcular_per).grid(column=1, row=11, padx=10, pady=10)

ttk.Label(root, textvariable=resultado, background="#f1f1f1").grid(column=0, row=12, columnspan=2, padx=10, pady=10)

# Crear Treeview para mostrar la tabla de amortización
tree = ttk.Treeview(root, columns=("Mes", "Cuota", "Interés", "Principal", "Saldo Pendiente"), show='headings')
tree.heading("Mes", text="Mes")
tree.heading("Cuota", text="Cuota")
tree.heading("Interés", text="Interés")
tree.heading("Principal", text="Principal")
tree.heading("Saldo Pendiente", text="Saldo Pendiente")

# Estilo de Treeview
tree.tag_configure('even', background="#f9f9f9")
tree.tag_configure('odd', background="#ffffff")

# Colocar el Treeview debajo del menú
tree.grid(column=0, row=13, columnspan=2, padx=10, pady=10)

# Iniciar la interfaz gráfica
root.mainloop()
