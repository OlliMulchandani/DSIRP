import tkinter as tk

class CircuitSimulator(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, width=600, height=400, background="white")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def simulate(self):
        for component in self.components:
            component.update()
        self.after(100, self.simulate)

class Resistor(object):
    def __init__(self, canvas, x1, y1, x2, y2, resistance):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.resistance = resistance
        self.current = 0
        self.voltage = 0
        self.color = "black"

    def update(self):
        self.voltage = (self.x1 - self.x2) / self.resistance
        self.current = self.voltage / self.resistance
        self.color = self.get_color(self.current)
        self.draw()

    def draw(self):
        self.canvas.
