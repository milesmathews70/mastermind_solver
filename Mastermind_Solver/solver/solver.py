#!/usr/bin/env python3

import node

def output(s, answer):
    score = 0
    string = []
    s_idx = 0
            
    for idx in range(len(answer)):
        if list(s)[s_idx] in list(answer):
            if list(s)[s_idx] == list(answer)[idx]:
                score += 1
                string.append("Y")
                s = delete(s, idx)
                s_idx -= 1
            s_idx += 1
                
    idx = 0
    answer_idx = 0
            
    while(len(s) > 0):
        if list(s)[idx] in list(answer):
            score += .6
            string.append("M")
        s = delete(s, idx)
        answer_idx += 1
    
    return (score, string)

def delete(string, idx):
    ls = list(string)
    ls.pop(idx)
    string = ''.join(ls)
    return string

def checkChildren(root, path):
    best = root.input
    for x in root.children():
        best = solved(x.input, best)
    root.past = best
    path.append(best)

def createChildren(root):
    child = root.input
    color = root.randomColor()
    indices = zerovectorsum(root.past, child)
    goal = determineScore(child)
    x = 0
    for idx in indices:
        while x < goal:
            child[idx + x] = color
            x += 1
        root.addChild(child)
        child = root.input
    root.deleteColor(color)

def zerovectorsum(first, second):
    count = 0
    indices = []
    for idx in range(len(first)):
        if first[idx] != second[idx]:
            indices.append(indices)
    return indices

