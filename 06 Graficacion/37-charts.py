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
    # Figura y coordenadas de inicio
    fig, ax = plt.subplots()

    # Grafica datos (gráfica de barras) recibiendo los labels y valores
    ax.bar(labels, values)
    # Muestra la gráfica
    plt.show()

# Función para generar grafica de pastel
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    # Grafica datos (Los argumentos se ponen así porque así lo dicen las reglas del método)
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
