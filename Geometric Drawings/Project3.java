package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Project summary: this project draws two types of shapes, ovals and rectangles in locations determined by users.
*/

import java.awt.*;
import java.awt.Rectangle;
import java.awt.event.*;
import java.lang.reflect.Field;
import javax.swing.*;

public class Project3 extends JFrame implements ActionListener{
    // Variables declaration:
    private JLabel shapeType;
    private JLabel fillType;
    private JLabel colorLbl;
    private JLabel labelX;
    private JLabel labelY;
    private JComboBox<String> shapesCombo;
    private JComboBox<String> fillCombo;
    private JComboBox<String> colorsCombo;
    private JLabel labelWidth;
    private JLabel labelHeight;
    private JPanel contentsPanel;
    private JPanel drawingPanel;
    private JPanel down;
    private JTextField inputX;
    private JTextField inputY;
    private JTextField inputWidth;
    private JTextField inputHeight;
    private JButton buttonDraw;

    public Project3() {
        setTitle("Geometric Drawing");    // javax.swing.JFrame
        setLayout(null);
        setSize(600, 400);

        // Layout set up:
        contentsPanel = new JPanel(new GridLayout(7, 2));
        drawingPanel = new JPanel();
        down = new JPanel();

        // Create the drawing pad's border:
        drawingPanel.setBorder(BorderFactory.createTitledBorder(
                null, "Shape Drawing",
                javax.swing.border.TitledBorder.DEFAULT_JUSTIFICATION,
                javax.swing.border.TitledBorder.DEFAULT_POSITION,
                new Font("Times New Roman", 0, 14),
                new Color(50, 50, 50)));

        // Combo boxes for user choice:
        shapeType = new JLabel();
        shapeType.setText("Shape Type");

        fillType = new JLabel();
        fillType.setText("Fill Type");

        colorLbl = new JLabel();
        colorLbl.setText("Color");

        shapesCombo = new JComboBox<>();
        fillCombo = new JComboBox<>();
        colorsCombo = new JComboBox<>();
        shapesCombo.setModel(new DefaultComboBoxModel<>(new String[] {"Rectangle", "Oval"}));
        fillCombo.setModel(new DefaultComboBoxModel<>(new String[] {"Solid", "Hollow"}));
        colorsCombo.setModel(new DefaultComboBoxModel<>(new String[] {"Black", "Red", "Orange", "Yellow", "Green", "Blue", "Magenta"}));

        // coordinates for user input (with default value displayed):
        inputX = new JTextField();
        inputY = new JTextField();
        inputX.setText("40");
        inputY.setText("30");

        labelX = new JLabel();
        labelY = new JLabel();
        labelX.setText("X Coordinate");
        labelY.setText("Y Coordinate");

        inputWidth = new JTextField();
        inputHeight = new JTextField();
        labelWidth = new JLabel();
        labelHeight = new JLabel();

        inputWidth.setText("100");
        inputHeight.setText("125");
        labelWidth.setText("Width");
        labelHeight.setText("Height");

        contentsPanel.setBounds(60, 30, 200, 250);
        drawingPanel.setBounds(290, 30, 250, 250);
        down.setBounds(230, 300, 100, 50);
        drawingPanel.setPreferredSize(new Dimension(240, 240));

        // Adding components to the contents panel:
        contentsPanel.add(shapeType);
        contentsPanel.add(shapesCombo);
        contentsPanel.add(fillType);
        contentsPanel.add(fillCombo);
        contentsPanel.add(colorLbl);
        contentsPanel.add(colorsCombo);
        contentsPanel.add(labelWidth);
        contentsPanel.add(inputWidth);
        contentsPanel.add(labelHeight);
        contentsPanel.add(inputHeight);
        contentsPanel.add(labelX);
        contentsPanel.add(inputX);
        contentsPanel.add(labelY);
        contentsPanel.add(inputY);

        // Add action listener to the draw button:
        buttonDraw = new JButton();
        buttonDraw.setText("Draw");
        buttonDraw.addActionListener(this);

        // Add the button to the last panel:
        down.add(buttonDraw);

        // Adding panels to the main frame:
        add(contentsPanel);
        add(drawingPanel);
        add(down);
    }

    public void paint(Shape shp) {
        try {
            Drawing drawing = new Drawing();
            drawing.setSize(drawing.getPreferredSize());
            drawing.drawShape(shp);

            // Reset the pane, add the shape and repaint:
            drawingPanel.removeAll();
            drawingPanel.add(drawing);
            drawingPanel.repaint();
        }
        catch (Exception ex) {
            JOptionPane.showMessageDialog(null, "The shape it out of the panel", "Error", JOptionPane.WARNING_MESSAGE);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        int x = 0, y = 0, width = 0, height = 0;

        // check whether any non integer values have been entered in any of the fields that require integers:
        try {
            x = Integer.parseInt(inputX.getText());
            y = Integer.parseInt(inputY.getText());
            width = Integer.parseInt(inputWidth.getText());
            height = Integer.parseInt(inputHeight.getText());
        }
        catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(null,
                    "Please enter a valid integer value in the field",
                    "Error", JOptionPane.WARNING_MESSAGE);
            return;
        }

        Rectangle rect = new Rectangle(x, y, width, height);
        String colorChoosed = colorsCombo.getSelectedItem().toString().toLowerCase();

        // Get the color:
        Color color;
        try {
            Field field = Color.class.getField(colorChoosed);
            color = (Color) field.get(null);
        } catch (Exception ex) {
            color = null;
        }

        // Solid or Hollow:
        boolean fill = true;
        if (fillCombo.getSelectedItem().toString().equals("Hollow")) {
            fill = false;
        }

        //Rectangle or Oval:
        if (shapesCombo.getSelectedItem().toString().equals("Rectangle")) {
            Rectangular rectangular = new Rectangular(rect, color, fill);
            paint(rectangular);
        }
        else {
            Oval oval = new Oval(rect, color, fill);
            paint(oval);
        }
    }

    public static void main(String args[]) {
        Project3 frame = new Project3();

        // Center the main frame on screen:
        frame.setLocationRelativeTo(null);

        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
