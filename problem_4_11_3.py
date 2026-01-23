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
    """
    Draws a parallelogram using a turtle.

    Parameters
    ----------
    bottom : int or float
        The length of the bottom and top sides.
    slanted : int or float
        The length of the slanted sides.
    angle : int or float, optional
        The interior angle between the bottom and slanted side. The default is 90.

    Returns
    -------
    None.

    """
    for _ in range(2):
        don.forward(bottom)
        don.left(angle)
        don.forward(slanted)
        don.left(180 - angle)

def rectangle(wide, tall):
    """
    Draws a rectangle  using the parallelogram function.
    
    Parameters
    ----------
    wide : int or float
        The width of the rectangle.
    tall : int or float
        The height of the rectangle.

    Returns
    -------
    None.

    """
    parallelogram(wide, tall)

def rhombus(length, angle):
    """
    Draws a rhombus using the parallelogram function.

    Parameters
    ----------
    length : int or float
        The length of each side of the rhombus.
    angle : int or float
        The interior angle of the rhombus.

    Returns
    -------
    None.

    """
    parallelogram(length, length, angle)

rectangle(80, 40)
rhombus(50, 60)

turtle.done()
