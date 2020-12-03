#!/usr/bin/env python3
import node
import solver
import tree

def main():
    colors = ["G", "R", "U", "B", "W", "O"]
    path = []
    answer = []
    for i in range(4):
        answer.append(colors[randint(len(colors))])
    color = colors[randint(len(colors))]
    colors.remove(color)
    string = []
    for i in range(4):
        string.append(color)
    output = solver.output(''.join(string), ''.join(answer))
    Node root = Node(''.join(string), output, colors)
    path.append(root.input)
    while :
        ...
