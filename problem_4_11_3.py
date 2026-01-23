#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:57:27 2026

@author: evebarr20
"""

# import the turtle library
import turtle

# create a turtle screen, with a yellow background
SCREEN = turtle.Screen()
SCREEN.bgcolor("lightyellow")

# turtle is name Mikey (TMNT)

mikey = turtle.Turtle()
mikey.color("yellow")
mikey.pensize(6)

def parallelogram(bottom, slanted, angle):
    for _ in range(4):
        mikey.forward(bottom)
        mikey.left(angle)
        mikey.forward(slanted)
        mikey.left(180 - angle)
    