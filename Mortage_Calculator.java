package com.xingyi;

import java.text.Format;
import java.text.NumberFormat;
import java.util.Currency;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final byte MON_IN_YEAR = 12;
        final byte PERCENT = 100;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Principal: ");
        int principal = Integer.parseInt(scanner.next());

        System.out.print("Annual Interest Rate: ");
        float monthlyInterest = Float.parseFloat(scanner.next()) / MON_IN_YEAR / PERCENT;

        System.out.print("Period (Years): ");
        byte year = Byte.parseByte(scanner.next());
        int numberOfPayments = year * MON_IN_YEAR;

        double mortgage = principal * monthlyInterest
                * Math.pow(1 + monthlyInterest, MON_IN_YEAR*year)
                / (Math.pow(1 + monthlyInterest, MON_IN_YEAR*year) - 1);

        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);

        System.out.print("Mortgage: " + mortgageFormatted);
    }
}
