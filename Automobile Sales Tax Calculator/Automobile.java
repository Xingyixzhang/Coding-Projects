package com.xingyi;
/*
    File Name: Automobile.java
    Author: Xingyi Zhang
    Date: June 13, 2020
    Purpose of the program -- The Automobile Class:
        1. Contains: automobile's make and model;
                     purchase price in whole dollars;
                     constructor to initialize the make and price;
                     salesTax method to return the base sales tax of 5% * price;
                     toString method to return a string containing all info properly labeled.
        2. Subclasses: Electric + Hybrid
 */
public class Automobile {
    private String makeAndModel = "";
    private int purchasePrice = 0;
    private static final double SALE_TAX_PERCENT = 0.05;

    // Initialize the make and price of the automobile:
    public Automobile(String make, int price){
        makeAndModel = make;
        purchasePrice = price;
    }

    // Calculate the base sales tax:
    public double salesTax(){
        return purchasePrice * SALE_TAX_PERCENT;
    }

    // toString method to return the information appropriately labeled:
    public String toString(String make_model, int price){
        return String.format("\nMake and Model: " + makeAndModel
                            + "\nSales Price: " + purchasePrice
                            + "\nSales Tax: %.2f\n", salesTax());
    }

    // For information retrieval from the subclasses:
    // NOT PUBLIC, only available to classes in the same package:
    String getMakeAndModel(){
        return makeAndModel;
    }

    int getPurchasePrice() {
        return purchasePrice;
    }
}