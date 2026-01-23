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

don = turtle.Turtle()
don.color("purple")
don.pensize(6)

def parallelogram(bottom, slanted, angle = 90):
    for _ in range(2):
        don.forward(bottom)
        don.left(angle)
        don.forward(slanted)
        don.left(180 - angle)

def rectangle(wide, tall):
    parallelogram(wide, tall)

def rhombus(length, angle):
    parallelogram(length, length, angle)

rectangle(80, 40)
rhombus(50, 60)

turtle.done()
