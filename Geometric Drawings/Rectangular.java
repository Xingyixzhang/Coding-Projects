package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Name: Rectangular class
    Summary: this is a subclass of the Shape class.
*/

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Rectangular extends Shape {
    // Constructor to initialize the shape:
    public Rectangular(Rectangle rect, Color color, boolean isSolid) {
        super(rect, color, isSolid);
    }

    // An overridden method that draws the Rectangular object.
    @Override
    void Draw(Graphics g) {
        setColor(g);
        if (getSolid())
            g.fillRect(this.x, this.y, this.width, this.height);
        else
            g.drawRect(this.x, this.y, this.width, this.height);
    }
}