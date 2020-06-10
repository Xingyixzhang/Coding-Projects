package com.xingyi;

import java.text.DecimalFormat;

public class Weight{
    private int pounds;
    private double ounces;
    // A private constant defining # of ounces in a pound:
    private final double Ounces_in_Pound = 16;

    // A public constructor to initialize the values:
    public Weight(int p, double o){
        pounds = p;
        ounces = o;
    }

    // A public instance method to judge if the value is less than the supplied parameter value:
    public boolean lessThan(Weight weight){
        return this.toOunces() < weight.toOunces();
    }

    // A public instance method to add on the weight:
    public void addTo(Weight weight){
        this.ounces += weight.toOunces();
        normalize();    // Normalize the result.
    }

    // To divide the weight by the supplied divisor:
    public void divide(int divisor){
        if (divisor != 0){
            pounds /= divisor;
            ounces /= divisor;
            normalize();    // Normalize the result.
        }
    }

    // Override/Format a toString method:
    @Override
    // Limit the decimal digits to 3 after decimal point.
    public String toString(){
        return pounds + " lbs " + String.format("%.3f", ounces) + " oz";
    }

    // A private method to return total weight in ounces:
    private double toOunces(){
        return this.pounds * Ounces_in_Pound + this.ounces;
    }

    // A private method to normalize the results:
    private void normalize(){
        if (ounces >= Ounces_in_Pound){
            pounds += (int)(ounces/Ounces_in_Pound);
            ounces %= Ounces_in_Pound;
        }
    }
}
