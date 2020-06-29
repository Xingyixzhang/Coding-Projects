package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Name: Drawing class
    Summary: This class extends the predefined Java class JPanel and have one
             instance variable that contains the shape that is currently drawn.
*/

import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JPanel;

public class Drawing extends JPanel {
    private Shape shape;
    private static final int CORNER_X = 5, CORNER_Y = 35;
    private static final int WIDTH = 240, HEIGHT = 240;
    private static final int OUTBOUND_ERROR_CODE = 999;

    // Method that draws the current shape and the number of shapes created in the upper left corner:
    @Override
    protected void paintComponent(Graphics g) {
        shape.Draw(g);
        g.drawString("" + shape.getNoOfShapes(), CORNER_X, CORNER_Y);
    }

    // Specifies the dimensions of the drawing panel as 200 pixels wide and 200 pixels high:
    @Override
    public Dimension getPreferredSize() {
        Dimension dimension = new Dimension(WIDTH, HEIGHT);
        return dimension;
    }

    // Instance method to check if the shape can fit in panel and draw the shape using repaint():
    public void drawShape(Shape shape) throws Exception {
        if (contains(shape.x, shape.y) &&
                contains(shape.x + shape.width, shape.y) &&
                contains(shape.x, shape.y + shape.height) &&
                contains(shape.x + shape.width, shape.y + shape.height))
        {
            this.shape = shape;
            repaint();
        }
        else
            throw new OutsideBounds(OUTBOUND_ERROR_CODE);
    }
}