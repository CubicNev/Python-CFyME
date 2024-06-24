"""
Charts
Autor: Carlos Nevárez - CubicNev
Fecha de creación: Mon 24-Jun-2024

Módulo encargado de generar gráficas.
"""
# Importación con alias
import matplotlib.pyplot as plt

# Función para generar gráfica de barras
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

# Función para generar grafica de pastel
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    # Lo grafica de forma circular
    ax.axis('equal')
    plt.show()

# Ejecución del módulo como script
if __name__ == "__main__":
    # Ejemplo
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels,values)
