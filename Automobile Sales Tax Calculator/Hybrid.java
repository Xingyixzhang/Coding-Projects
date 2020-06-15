package com.xingyi;

/*
    File Name: Hybrid.java
    Author: Xingyi Zhang
    Date: June 14, 2020
    Purpose of the program: create a subclass of the automobile class,
        with additional instance variable and method override.
 */

public class Hybrid extends Automobile {
    // Additional instance variable for mpg:
    private int milesPerGallon = 0;
    // To eliminate "magic numbers" in the program:
    private static final int MILES_PER_GALLON = 40;
    private static final int DISCOUNT_WHEN_LESS = 100;
    private static final int DISCOUNT_PER_EXCESS_MILE = 2;

    // Initialize the make and model, price, and mpg:
    public Hybrid(String make_model, int price, int miles){
        super(make_model, price);
        milesPerGallon = miles;
    }

    // salesTax method override the one in super class to fit in Hybrid automobile cases:
    @Override
    public double salesTax(){
        double salesTaxPrice = super.salesTax();
        if (milesPerGallon < MILES_PER_GALLON){
            if (salesTaxPrice >= DISCOUNT_WHEN_LESS)
                return salesTaxPrice - DISCOUNT_WHEN_LESS;
            else
                return 0.0;
        }
        else{
            int discount = (milesPerGallon - MILES_PER_GALLON) * DISCOUNT_PER_EXCESS_MILE;
            if (salesTaxPrice - discount >= DISCOUNT_WHEN_LESS)
                return salesTaxPrice - discount - DISCOUNT_WHEN_LESS;
            else
                return 0.0;
        }
    }

    // toString method to return all information appropriately labeled:
    @Override
    public String toString(){
        return String.format(
                "\nMake and Model: " + this.getMakeAndModel()
                + "\nSales Price: " + this.getPurchasePrice()
                + "\nSales Tax: " + this.salesTax()
                + "\nHybrid Vehicle"
                + "\nMPG: " + milesPerGallon + '\n'
        );
    }
}
