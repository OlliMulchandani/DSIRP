import tkinter as tk
import numpy as np

# create the main window
root = tk.Tk()
root.title("Graphing Calculator")

# create a canvas to draw the graph on
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# create a function to draw the graph
def draw_graph(expression):
    # parse the expression and evaluate it at each point on the graph
    x_values = np.linspace(-10, 10, num=100)
    y_values = eval(expression)
    # scale the x and y values to fit the canvas
    x_scale = canvas.winfo_width() / (max(x_values) - min(x_values))
    y_scale = canvas.winfo_height() / (max(y_values) - min(y_values))
    x_values = [x * x_scale for x in x_values]
    y_values = [y * y_scale for y in y_values]
    # draw the x and y axes with tick marks
    x_axis_y = y_scale * min(y_values)
    y_axis_x = x_scale * min(x_values)
    canvas.create_line(x_axis_x, 0, x_axis_x, canvas.winfo_height(), fill="black")
    canvas.create_line(0, x_axis_y, canvas.winfo_width(), x_axis_y, fill="black")
    for x in range(min(x_values), max(x_values), 10):
        canvas.create_line(x, x_axis_y - 5, x, x_axis_y + 5, fill="black")
    for y in range(min(y_values), max(y_values), 10):
        canvas.create_line(y_axis_x - 5, y, y_axis_x + 5, y, fill="black")
    # draw the graph using the x and y values
    canvas.create_line(x_values, y_values, fill="black")

# create an input field for the user to enter the expression
expression_input = tk.Entry(root)
expression_input.pack()

# create a button to draw the graph
