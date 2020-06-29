package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Name: Shape class
    Summary: this is an abstract class that extends the predefined Java class Rectangle.
*/

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public abstract class Shape extends Rectangle {
    // instance variables:
    private Color color;
    private boolean isSolid;
    private static int NUMBER_OF_SHAPES;

    public Shape(Rectangle rect, Color color, boolean isSolid) {
        this.color = color;
        this.isSolid = isSolid;

        // setRect from the java.awt.Rectangle class.
        this.setRect(rect.x, rect.y, rect.width, rect.height);

        // Update the number of shapes created:
        NUMBER_OF_SHAPES++;
    }

    // Instance method to set the color of the shape:
    public void setColor(Graphics g) {
        g.setColor(this.color);
    }

    // Instance method to determine weather the shape is solid or hollow:
    public boolean getSolid() {
        return this.isSolid;
    }

    // Class method to return the number of shapes created so far:
    public int getNoOfShapes() {
        return NUMBER_OF_SHAPES;
    }

    // Abstract method:
    abstract void Draw(Graphics g);
}