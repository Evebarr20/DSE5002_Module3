#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 19:45:13 2026

@author: evebarr20
"""
# import the turtle library
import turtle

# create a turtle screen, with a yellow background
SCREEN = turtle.Screen()
SCREEN.bgcolor("lightyellow")

# turtle is name Ralph(TMNT)

ralph = turtle.Turtle()
ralph.color("red")
ralph.pensize(6)

# 4.11.1. Exercise
# Write a function called rectangle that draws a rectangle with given side lengths.
# For example, here’s a rectangle that’s 80 units wide and 40 units tall.
def rectangle(wide, tall):
    """
    Draws a rectangle with the given width and height

    Parameters
    ----------
    wide : int or float
        The width of the rectangle
    tall : int or float
        The height of the rectangle.

    Returns
    -------
    None.

    """
    for _ in range(2):
        ralph.forward(wide)
        ralph.left(90)
        ralph.forward(tall)
        ralph.left(90)


rectangle(80, 40)

turtle.done()
