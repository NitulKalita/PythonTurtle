import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

input_color = "#0000FF"  # Blue
hidden_color = "#808080"  # Grey
output_color = "#000000"  # Black
connection_colors = ["#FF5733", "#33FF57", "#3357FF",
                     "#F333FF", "#FFD633", "#33FFF5", "#FF33C4"]

def draw_neuron(x, y, color, radius=20):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_connection(x1, y1, x2, y2):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.color(random.choice(connection_colors))
    pen.goto(x2, y2)

def calculate_layer_positions(neurons, center_y, y_gap):
    return [center_y - (neurons - 1) * y_gap /
            2 + i * y_gap for i in range(neurons)]

def draw_layer(x, y_positions, color):
    positions = []
    for y in y_positions:
        draw_neuron(x, y, color)
        positions.append((x, y))
    return positions

def connect_layers(layer1, layer2):
    for x1, y1 in layer1:
        for x2, y2 in layer2:
            draw_connection(x1 + 20, y1, x2 - 20, y2)

input_neurons = 3
hidden_neurons_1 = 5
hidden_neurons_2 = 5
output_neurons = 2

x_positions = {
    'input': -300,
    'hidden_1': -100,
    'hidden_2': 100,
    'output': 300
}

center_y_hidden = 100
y_gap_hidden = 75

y_hidden_1 = calculate_layer_positions(hidden_neurons_1,
                                       center_y_hidden, y_gap_hidden)
y_hidden_2 = calculate_layer_positions(hidden_neurons_2,
                                       center_y_hidden, y_gap_hidden)


y_input = calculate_layer_positions(input_neurons,
                                    center_y_hidden, 100)
y_output = calculate_layer_positions(output_neurons,
                                     center_y_hidden, 100)


input_positions = draw_layer(x_positions['input'], y_input, input_color)
hidden_1_positions = draw_layer(x_positions['hidden_1'], y_hidden_1, hidden_color)
hidden_2_positions = draw_layer(x_positions['hidden_2'], y_hidden_2, hidden_color)
output_positions = draw_layer(x_positions['output'], y_output, output_color)


connect_layers(input_positions, hidden_1_positions)
connect_layers(hidden_1_positions, hidden_2_positions)
connect_layers(hidden_2_positions, output_positions)


pen.penup()
pen.goto(0, -250)
pen.pendown()
pen.color("black")
pen.write("@coding_nitul", align="center", font=("Arial", 16, "normal"))


pen.hideturtle()
turtle.done()
