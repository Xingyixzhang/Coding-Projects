package com.xingyi;

/*
    Author: Xingyi Zhang
    Date: June 28, 2020
    Name: OutsideBounds class
    Summary: This class defines a checked exception.
*/

public class OutsideBounds extends Exception {
    private int errorCode;

    public OutsideBounds(int code) {
        super();
        errorCode = code;
    }

    @Override
    public String getMessage() {
        String Message = "";

        if (errorCode == 999){
            Message = "The Shape you draw will be outside bounds";
        }

        return Message;
    }
}