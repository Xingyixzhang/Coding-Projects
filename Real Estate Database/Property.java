package com.xingyi;

/**
 * Author: Xingyi Zhang
 * File Name: Property.java
 * Date: July 9, 2020
 * Summary: An generic class that implements the StateChangeable Interface. Store information of the property.
 */

public class Property<T extends Enum<T>> implements StateChangeable<T>  {
    // Five instance variables:
    private String propertyAddress;
    private int numberOfBedrooms;
    private int squareFeet;
    private int price;
    private Status propertyStatus;

    // Constructor that accepts 4 parameters and defines property status as FOR_SALE:
    public Property(String address, int number, int squareFeet, int price) {
        propertyAddress = address;
        numberOfBedrooms = number;
        this.squareFeet = squareFeet;
        this.price = price;
        propertyStatus = Status.FOR_SALE;
    }

    // An Overridden method that changes status of property:
    @Override
    public void changeState(T status) {
        propertyStatus = (Status)status;
    }

    // An overridden method to return a string of the property's information:
    @Override
    public String toString() {
        return new String("Property Address: " +
                propertyAddress + "\nNumber of Bedrooms: " + numberOfBedrooms
                + "\nSquare Feet: " + this.squareFeet + "\nPrice: $" + this.price
                + "\nStatus: " + this.propertyStatus);
    }
}
