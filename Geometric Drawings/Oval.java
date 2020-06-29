package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Name: Oval class
    Summary: this is a subclass of the Shape class.
*/

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;

public class Oval extends Shape {
    // Constructor to initialize the characteristics of the shape:
    public Oval(Rectangle rect, Color color, boolean isSolid) {
        super(rect, color, isSolid);
    }

    // An overridden method draw that draws the Oval object on the Graphics object passed as a parameter:
    @Override
    void Draw(Graphics g) {
        setColor(g);
        if (getSolid())
            g.fillOval(this.x, this.y, this.width, this.height);
        else
            g.drawOval(this.x, this.y, this.width, this.height);
    }
}
