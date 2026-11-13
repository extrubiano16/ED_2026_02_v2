import matplotlib.pyplot as plt
import math

class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    # ── Sube el elemento en la posición i mientras sea menor que su padre
    def _sift_up(self, i):
        padre = i // 2
        while self.arreglo[i] < self.arreglo[padre]:
            self.arreglo[i], self.arreglo[padre] = self.arreglo[padre], self.arreglo[i]
            i = padre
            padre = i // 2

    # ── Baja el elemento en la posición i hacia su hijo mínimo
    def _sift_down(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            izq = 2 * i
            der = 2 * i + 1

            # elegir el hijo más pequeño
            if der <= n and self.arreglo[der] < self.arreglo[izq]:
                hijo_min = der
            else:
                hijo_min = izq

            # si ya está en su lugar, parar
            if self.arreglo[i] <= self.arreglo[hijo_min]:
                break

            self.arreglo[i], self.arreglo[hijo_min] = self.arreglo[hijo_min], self.arreglo[i]
            i = hijo_min

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        self._sift_up(len(self.arreglo) - 1)
        if imagen:
            self._mostrar_imagen()

    def remove_smallest(self, imagen=False):
        n = len(self.arreglo) - 1
        if n == 0:
            return None
        if n == 1:
            return self.arreglo.pop()
        minimo = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()
        self._sift_down(1)
        if imagen:
            self._mostrar_imagen()
        return minimo

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        ultimo_interno = (len(self.arreglo) - 1) // 2

        for i in range(ultimo_interno, 0, -1):
            self._sift_down(i)

        if imagen:
            self._mostrar_imagen()

    def _calcular_posiciones(self):
        n = len(self.arreglo) - 1

        # contar niveles sumando potencias de 2: nivel 0→1 nodo, nivel 1→2, nivel 2→4...
        niveles = 0
        while 2 ** niveles <= n:
            niveles += 1

        ancho = 2 ** (niveles - 1)
        pos = {}

        for i in range(1, n + 1):
            # encontrar en qué nivel está el nodo i
            nivel = 0
            while 2 ** (nivel + 1) <= i:
                nivel += 1

            pos_en_nivel = i - 2 ** nivel
            espaciado = ancho / 2 ** nivel
            x = (pos_en_nivel + 0.5) * espaciado
            y = niveles - nivel - 1
            pos[i] = (x, y)

        return pos, niveles

    def _mostrar_imagen(self):
        n = len(self.arreglo) - 1
        if n == 0:
            print("El heap está vacío.")
            return
        pos, niveles = self._calcular_posiciones()
        ancho_total = 2 ** (niveles - 1)
        radio = 0.35
        fig, ax = plt.subplots(figsize=(max(6, ancho_total + 1), max(4, niveles * 1.8)))
        ax.set_xlim(0, ancho_total)
        ax.set_ylim(-0.8, niveles - 0.2)
        ax.axis('off')
        for i in range(1, n + 1):
            x1, y1 = pos[i]
            for hijo in (2 * i, 2 * i + 1):
                if hijo <= n:
                    x2, y2 = pos[hijo]
                    ax.plot([x1, x2], [y1, y2], color='#555555', linewidth=1.5, zorder=1)
        for i in range(1, n + 1):
            x, y = pos[i]
            circulo = plt.Circle((x, y), radio, facecolor='#AED6F1',
                                  edgecolor='#2471A3', linewidth=2, zorder=2)
            ax.add_patch(circulo)
            ax.text(x, y, str(self.arreglo[i]),
                    ha='center', va='center', fontsize=11, fontweight='bold', zorder=3)
        plt.title(f"Min-Heap  ({n} nodo{'s' if n != 1 else ''})", fontsize=13)
        plt.tight_layout()
        plt.show()
