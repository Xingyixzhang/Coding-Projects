package com.xingyi;

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Simple_Math extends JFrame implements ActionListener {
    JPanel header, body, end;
    GridLayout layout;
    JLabel labelNumber1, labelNumber2;
    JLabel welcome, result;
    JTextField Number1, Number2;
    JButton calculate;

    public Simple_Math(){
        setTitle("Simple Addition Calculator");
        setLayout(null);
        setSize(400, 400);
        layout = new GridLayout(2, 2);

        header = new JPanel(new GridLayout(1, 1));
        body = new JPanel(layout);
        end = new JPanel(new GridLayout(1, 2));

        welcome = new JLabel("Welcome to Simple Addition!");
        welcome.setFont(new Font( "HeaderFont",Font.BOLD, 18));
        welcome.setForeground(Color.MAGENTA);
        header.add(welcome);

        calculate = new JButton("Add Them!");
        calculate.addActionListener(this);
        result = new JLabel("");

        labelNumber1 = new JLabel("Number 1:");
        Number1 = new JTextField(20);
        labelNumber2 = new JLabel("Number 2:");
        Number2 = new JTextField(20);

        body.add(labelNumber1);
        body.add(Number1);
        body.add(labelNumber2);
        body.add(Number2);

        Number1.setEnabled(true);
        Number2.setEnabled(true);

        result.setEnabled(false);
        result.setBorder(BorderFactory.createLineBorder(new Color(132, 141, 149),1));
        result.setForeground(Color.blue);
        result.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 15));
        result.setHorizontalTextPosition(0);

        end.add(calculate);
        end.add(result);

        header.setBounds(50, 50, 270, 70);
        body.setBounds(50, 150, 250, 60);
        end.setBounds(50, 270, 250, 30);

        add(header);
        add(body);
        add(end);
    }

    public boolean isDouble(String number){
        try{
            Double.parseDouble(number);
            return true;
        }
        catch (Exception e){
            return false;
        }
    }

    @Override
    public void actionPerformed(ActionEvent event){
        if (event.getSource() == calculate){
            if (isDouble(Number1.getText()) && isDouble(Number2.getText())){
                double num1 = Double.parseDouble(Number1.getText());
                double num2 = Double.parseDouble(Number2.getText());
                result.setText(String.format("%.2f", num1 + num2));
            }
            else {
                // result.setText("");
                JOptionPane.showMessageDialog(this,
                        "Please enter a valid number.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }

    public static void main(String[] args) {
        Simple_Math additionCalculator = new Simple_Math();
        additionCalculator.setLocationRelativeTo(null);
        additionCalculator.setVisible(true);
        additionCalculator.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
