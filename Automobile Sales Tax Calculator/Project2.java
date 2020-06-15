package com.xingyi;

/*
    File Name: Project2.java
    Author: Xingyi Zhang
    Date: June 13, 2020
    Purpose of the program: Generate GUI for the Automobile Sales Tax Calculator program.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

public class Project2 extends JFrame implements ActionListener {
    JLabel labelMakeModel, labelSalesPrice;
    JLabel labelMPG, labelWeight;
    JTextField textMakeModel, textSalesPrice;
    JTextField textMPG, textWeight;

    JRadioButton hybrid, electric, other;
    JPanel up, mid, down;
    ButtonGroup group;
    JButton buttonComputeSalesTax, buttonClear, buttonDisplayReport;
    JLabel resultOutput;

    List<Automobile> automobileList;

    public Project2(){
        setTitle("Automobile Sales Tax Calculator");

        // Initialize components. Note that List is an interface and ArrayList is a class.
        automobileList = new ArrayList<>();
        setLayout(null);
        setSize(600, 500);

        // Initialize the panels with grid layouts:
        up = new JPanel(new GridLayout(2, 2));
        mid = new JPanel(new GridLayout(3, 3));
        // Set the border around the Automobile Type section:
        mid.setBorder(BorderFactory.createTitledBorder("Automobile Type"));
        down = new JPanel(new GridLayout(2, 2, 10, 10));

        // Initialize labels with displaying texts:
        labelMakeModel = new JLabel("Make and Model");
        labelSalesPrice = new JLabel("Sales Price");
        // Initialize the Text Fields with columns allowed:
        textMakeModel = new JTextField(20);
        textSalesPrice = new JTextField(20);

        // Adding components (labels and text fields) to the upper panel of the main frame:
        up.add(labelMakeModel);
        up.add(textMakeModel);
        up.add(labelSalesPrice);
        up.add(textSalesPrice);

        // Initialize Radio Buttons with Displaying texts for choice:
        hybrid = new JRadioButton("Hybrid");
        electric = new JRadioButton("Electric");
        other = new JRadioButton("Other");

        // Group the radio buttons together using the ButtonGroup:
        group = new ButtonGroup();
        group.add(hybrid);
        group.add(electric);
        group.add(other);

        // Initialize labels and text fields for the middle section:
        labelMPG = new JLabel("Miles per Gallon");
        labelWeight = new JLabel("Weight in Pounds");
        textMPG = new JTextField(20);
        textWeight = new JTextField(20);

        // Adding the first row of components to the "Automobile Type" section:
        mid.add(hybrid);
        mid.add(labelMPG);
        mid.add(textMPG);

        // Adding second row: -- JPanel.add() method adds components left-right, up-down:
        mid.add(electric);
        mid.add(labelWeight);
        mid.add(textWeight);

        // Adding the last row for the middle section:
        mid.add(other);

        // Initialize buttons with displaying texts for user choice:
        buttonComputeSalesTax = new JButton("Compute Sales Tax");
        buttonClear = new JButton("Clear Fields");
        buttonDisplayReport = new JButton("Display Report");

        resultOutput = new JLabel("");
        // Ensure the output box is visible:
        resultOutput.setBorder(BorderFactory.createLineBorder(new Color(132, 141, 149),1));

        // Adding components in order to the last section.
        down.add(buttonComputeSalesTax);
        down.add(resultOutput);
        down.add(buttonClear);
        down.add(buttonDisplayReport);

        // Setting grid boundaries for the three panels:
        up.setBounds(80, 40, 400, 50);
        mid.setBounds(20, 130, 550, 120);
        down.setBounds(70, 300, 400, 100);

        // Adding panels to the main frame:
        add(up);
        add(mid);
        add(down);

        // Add Action Listeners to the buttons for user interactions:
        buttonComputeSalesTax.addActionListener(this);
        buttonClear.addActionListener(this);
        buttonDisplayReport.addActionListener(this);

        hybrid.addActionListener(this);
        electric.addActionListener(this);
        other.addActionListener(this);

        // Set the result to be non-editable:
        resultOutput.setEnabled(false);
        other.doClick();    // Show pre-select option.

        // Style the result box:
        resultOutput.setForeground(Color.blue);
        resultOutput.setFont(new Font(Font.SANS_SERIF, Font.BOLD, 15));
    }

    // Adding vehicle to the list while maintaining only the last 5 in list:
    public  void addAutomobile(Automobile vehicle){
        if (automobileList.size() >= 5)
            automobileList.remove(0);
        automobileList.add(vehicle);
    }

    // Checking if a value is a valid integer value:
    public int isIntValid(String number){
        try {
            Integer val = Integer.parseInt(number.trim());
            if (val <= 0)
                val = -1;
            return val;
        }
        catch (Exception e){
            return -1;
        }
    }

    // Print Error Messages based on false input types,
    // Avoids the duplication of code:
    public void printErrorMessage(String name){
        JOptionPane.showMessageDialog(this, "Invalid " + name +
                " Price Input, please enter an integer value.", "Error", JOptionPane.ERROR_MESSAGE);
    }

    // Save reports using different methods since the types will differ:
    // 1. Save report for hybrid automobiles:
    public void saveHybrid(){
        int price = isIntValid(textSalesPrice.getText());
        if (price != -1){
            int mpg = isIntValid(textMPG.getText());
            if (mpg == -1)
                printErrorMessage("miles-per-gallon");
            else{
                Hybrid vehicle = new Hybrid(textMakeModel.getText(), price, mpg);
                resultOutput.setText(String.format("%.2f", vehicle.salesTax()));
                addAutomobile(vehicle);
            }
        }
        else
            printErrorMessage("price");
    }

    public void saveElectric(){
        int price = isIntValid(textSalesPrice.getText());
        if (price != -1){
            int weight = isIntValid(textWeight.getText());
            if (weight == -1)
                printErrorMessage("weight");
            else{
                Electric vehicle = new Electric(textMakeModel.getText(), price, weight);
                resultOutput.setText(String.format("%.2f", vehicle.salesTax()));
                addAutomobile(vehicle);
            }
        }
        else
            printErrorMessage("price");
    }

    // 3. Save report for other types of automobiles:
    public void saveOther(){
        int price = isIntValid(textSalesPrice.getText());
        if (price == -1)
            printErrorMessage("price");
        else{
            Automobile vehicle = new Automobile(textMakeModel.getText(), price);
            resultOutput.setText(String.format("%.2f", vehicle.salesTax()));
            addAutomobile(vehicle);
        }
    }

    // Prepare for user input and save the vehicle upon selection action:
    public void actionPerformed(ActionEvent event){
        // When "Hybrid" is selected, prepare for user input:
        if (event.getSource() == hybrid){
            textMPG.setEnabled(true);
            textWeight.setEnabled(false);
            resultOutput.setText("");
            textWeight.setText("");
        }
        // When "Electric" is selected, prepare for user input:
        else if (event.getSource() == electric){
            textMPG.setEnabled(false);
            textWeight.setEnabled(true);
            textMPG.setText("");
            resultOutput.setText("");
        }
        // When "Other" is selected, prepare for user input:
        else if (event.getSource() == other){
            textMPG.setEnabled(false);
            textWeight.setEnabled(false);
            textWeight.setText("");
            textMPG.setText("");
            resultOutput.setText("");
        }
        // When "Compute Sales Tax" is selected, save and compute accordingly:
        else if (event.getSource() == buttonComputeSalesTax){
            if (hybrid.isSelected())
                saveHybrid();
            else if (electric.isSelected())
                saveElectric();
            else
                saveOther();
        }
        // When "Clear Fields" is selected, reset the form:
        else if (event.getSource() == buttonClear){
            resetForm();
        }
        // When "Display Report" is selected:
        else if (event.getSource() == buttonDisplayReport)
            displayReport();
    }

    // Clear out the input/output of the form, reset to default stance:
    public void resetForm(){
        textMakeModel.setText("");
        textSalesPrice.setText("");
        textMPG.setText("");
        textWeight.setText("");
        other.setSelected(true);
        resultOutput.setText("");
        other.doClick();
    }

    // Console displays the report:
    public void displayReport(){
        String report = "";
        for (Automobile vehicle: automobileList)
            report += vehicle.toString() + '\n';
        System.out.println(report);
    }

    // Initialize the main frame:
    public static void main(String[] args) {
        Project2 frame = new Project2();

        // Center the mainFrame on screen:
        frame.setLocationRelativeTo(null);

        // To display the frame:
        frame.setVisible(true);

        // Ensure that the program exits when the user close the frame:
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
