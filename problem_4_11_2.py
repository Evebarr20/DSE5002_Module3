#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 20:25:13 2026

@author: evebarr20
"""

# import the turtle library
import turtle

# create a turtle screen, with a yellow background
SCREEN = turtle.Screen()
SCREEN.bgcolor("lightyellow")

# turtle is name Leo(TMNT)

leo = turtle.Turtle()
leo.color("blue")
leo.pensize(6)

# 4.11.2. Exercise
# Write a function called rhombus that draws a rhombus with a given side length
# and a given interior angle.
# For example, here’s a rhombus with side length 50 and an interior angle of 60 degrees.

def rhombus(length, angle):
    """
    Draws a rhombus with the given length and angle

    Parameters
    ----------
    length : int or float
        The length of the rhombus.
    angle : int or float
        The angle of the rhombus.

    Returns
    -------
    None.

    """
    angles = 180 - angle
    for _ in range(2):
        leo.forward(length)
        leo.left(angles)
        leo.forward(length)
        leo.left(angle)

rhombus(50, 60)

turtle.done()
