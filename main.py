import matplotlib.pyplot as plt
import numpy as np

def generate_L_system(n, axiom, rules):
    current_string = axiom
    for i in range(n):
        new_string = ""
        for symbol in current_string:
            if symbol in rules:
                new_string += rules[symbol]
            else:
                new_string += symbol
        current_string = new_string
    return current_string

axiom = "X"
rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
n = 5 

print(generate_L_system(n, axiom, rules))

def draw_L_system(ax, instructions, angle, distance):
    stack = []
    current_angle = 0.0
    x, y = 0.0, 0.0
    lines = []

    for command in instructions:
        if command == 'F':
            dx = distance * np.cos(current_angle)
            dy = distance * np.sin(current_angle)
            lines.append(((x, y), (x + dx, y + dy)))
            x += dx
            y += dy
        elif command == '+':
            current_angle += angle
        elif command == '-':
            current_angle -= angle
        elif command == '[':
            stack.append((x, y, current_angle))
        elif command == ']':
            x, y, current_angle = stack.pop()

    for line in lines:
        ax.plot(*zip(*line), color='green')

axiom = "X"
rules = {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}
n = 5

instructions = generate_L_system(n, axiom, rules)

fig, ax = plt.subplots()

draw_L_system(ax, instructions, np.radians(25), 0.1)

plt.axis('off')
plt.show()