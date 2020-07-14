package com.xingyi;

/**
 * Author: Xingyi Zhang
 * File Name: Project4.java
 * Date: July 9, 2020
 * Summary: The class that contains the main method and generates the GUI,
 *          allowing users to modify and display information of properties
 *          in the real estate database.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.TreeMap;

public class Project4 {
    public static class mainPanel extends JPanel {
        private JLabel lblTransaction = new JLabel("Transaction No:");
        private JLabel lblAddress = new JLabel("Address:");
        private JLabel lblBedrooms = new JLabel("Bedrooms:");
        private JLabel lblSqft = new JLabel("Square Footage:");
        private JLabel lblPrice = new JLabel("Price:");

        private JTextField txtTransaction = new JTextField("");
        private JTextField txtAddress = new JTextField("");
        private JTextField txtBedrooms = new JTextField("");
        private JTextField txtSqft = new JTextField("");
        private JTextField txtPrice = new JTextField("");

        private String[] operations = {"Insert", "Delete", "Find"};
        private JComboBox operationsList = new JComboBox(operations);

        private Status[] statuses = {Status.FOR_SALE, Status.UNDER_CONTRACT, Status.SOLD};
        private JComboBox statusList = new JComboBox(statuses);

        TreeMap<Integer, Property> propertyTreeMap = new TreeMap<>();

        public mainPanel() {
            setLayout(new GridLayout(7,2,10,10));
            this.add(lblTransaction);
            this.add(txtTransaction);
            this.add(lblAddress);
            this.add(txtAddress);
            this.add(lblBedrooms);
            this.add(txtBedrooms);
            this.add(lblSqft);
            this.add(txtSqft);
            this.add(lblPrice);
            this.add(txtPrice);

            JButton btnProcess = new JButton(new AbstractAction("Process") {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String operationChoice = String.valueOf(operationsList.getSelectedItem());
                    try {
                        switch (operationChoice) {
                            case "Insert":
                                checkDups(getTransactionValue());
                                propertyTreeMap.put(getTransactionValue(), getInfo());
                                JOptionPane.showMessageDialog(null, "Property information successfully stored in the database.");
                                break;
                            case "Delete":
                                checkExisting(getTransactionValue());
                                propertyTreeMap.remove(getTransactionValue());
                                JOptionPane.showMessageDialog(null, "Property information successfully removed from the database.");
                                break;
                            case "Find":
                                checkExisting(getTransactionValue());
                                Property propertyFound = propertyTreeMap.get(getTransactionValue());
                                JOptionPane.showMessageDialog(null, getInfo().toString());
                                break;
                        }
                    }
                    catch (NumberFormatException ex){
                        JOptionPane.showMessageDialog(null, "The input has a wrong format.");
                    }
                    catch (DuplicateExists ex){ // Catch exception thrown by checkDups().
                        JOptionPane.showMessageDialog(null, "The property already exists.");
                    }
                    catch (PropertyNotFound ex){
                        JOptionPane.showMessageDialog(null, "This property is not found in the database.");
                    }
                }
            });

            JButton btnStatus = new JButton(new AbstractAction("Change Status") {
                @Override
                public void actionPerformed(ActionEvent e) {
                    try {
                        Status statusChoice = (Status) statusList.getSelectedItem();
                        checkExisting(getTransactionValue());

                        Property newProperty = propertyTreeMap.get(getTransactionValue());
                        newProperty.changeState(statusChoice);

                        propertyTreeMap.put(getTransactionValue(), newProperty);
                        JOptionPane.showMessageDialog(null, "The property's status has been successfully changed.");
                    }
                    catch (NumberFormatException ex){
                        JOptionPane.showMessageDialog(null, "The input has a wrong format.");
                    }
                    catch (PropertyNotFound ex){
                        JOptionPane.showMessageDialog(null, "This property is not found in the database.");
                    }
                }
            });

            this.add(btnProcess);
            this.add(operationsList);
            this.add(btnStatus);
            this.add(statusList);
        }

        // Convert input string to integer, check for invalid input:
        private int getInputValue(JTextField inputTextField) throws NumberFormatException {
            String inputString = inputTextField.getText();
            return Integer.parseInt(inputString);
        }

        // Check the format of input value:
        private int getTransactionValue() throws NumberFormatException {
            return getInputValue(txtTransaction);
        }

        // The exception when property already exists (For insertion):
        private class DuplicateExists extends Exception {
            public DuplicateExists() {
                super();    // Message will show when caught in the operation
            }
        }

        // The exception when there's no property found (for deletion and find):
        private class PropertyNotFound extends Exception {
            public PropertyNotFound() {
                super("The property was not found.");
            }
        }

        // Check whether to throw the duplication exception:
        private void checkDups(int transaction) throws DuplicateExists{
            if (propertyTreeMap.containsKey(transaction)){
                throw new DuplicateExists();
            }
        }

        // Check whether to throw the PropertyNotFound exception:
        private void checkExisting(int transaction) throws PropertyNotFound {
            if(!propertyTreeMap.containsKey(transaction)) {
                throw new PropertyNotFound();
            }
        }

        // Read input information and throw exception when wrong format detected:
        private Property getInfo() throws NumberFormatException {
            String address = txtAddress.getText();
            int bedroom = getInputValue(txtBedrooms);
            int squareFT = getInputValue(txtSqft);
            int price = getInputValue(txtPrice);
            return new Property(address, bedroom, squareFT, price);
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Real Estate Database");
        frame.setSize(500,450);
        frame.add(new mainPanel());
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}