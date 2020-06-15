package com.xingyi;

/*
    File Name: Electric.java
    Author: Xingyi Zhang
    Date: June 13, 2020
    Purpose of the program: create a subclass of the automobile class,
        with additional instance variable and method override.
 */

public class Electric extends Automobile {
    private int weight; // in pounds.

    // To eliminate "magic numbers" in the program:
    private static final int WEIGHT = 3000;
    private static final int LOWER_DISCOUNT = 150;
    private static final int HIGHER_DISCOUNT = 200;

    // Initialize the make, price, and weight of the automobile:
    public Electric(String make_model, int price, int weight){
        super(make_model, price);
        this.weight = weight;
    }

    // salesTax method overriding the super class method to fit Electric automobiles:
    @Override
    public double salesTax(){
        double salesTax = super.salesTax();
        // Discount when weight is less than 3000 pounds is $200:
        if (weight < WEIGHT)
            return salesTax >= HIGHER_DISCOUNT? (salesTax-HIGHER_DISCOUNT): 0.0;
        // Discount when  weight is equal to or more than 3000 pounds is $150:
        else
            return salesTax >= LOWER_DISCOUNT? (salesTax-LOWER_DISCOUNT): 0.0;
    }

    // toString method to return all info appropriately labeled:
    @Override
    public String toString(){
        return String.format(
                "\nMake and Model: " + this.getMakeAndModel()
                + "\nSales Price: " + this.getPurchasePrice()
                + "\nSales Tax: " + this.salesTax()
                + "\nWeight: " + this.weight
                + "\nElectric Vehicle"
        );
    }
}
