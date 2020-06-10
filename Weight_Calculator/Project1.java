package com.xingyi;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import javax.swing.JFileChooser;

public class Project1{

    public static void main(String []args)
    throws FileNotFoundException, IOException{
        File file = null;

        JFileChooser fileChooser = new JFileChooser();

        int res = fileChooser.showOpenDialog(null);
        if (res == JFileChooser.APPROVE_OPTION){
            file = fileChooser.getSelectedFile();
        }

        Weight[] weights = new Weight[25];  // Initiate the size(25) for Weights file storage.
        BufferedReader br = new BufferedReader(new FileReader(file)); // Read the file.

        int i = 0;
        String line = br.readLine();

        while (line != null){
            if (i == 25)    // Terminates the program and display error message
            {
                System.out.println("Error -- You have exceeded the limit.");
                return;
            }
            else{
                int pounds = Integer.parseInt(line.split(",")[0]);
                double ounces = Double.parseDouble(line.split(",")[1]);
                weights[i] = new Weight(pounds, ounces);
                i++;
            }
            line = br.readLine();
        }

        System.out.println("Minimum weight: " + findMinimum(weights, i).toString());
        System.out.println("Maximum weight: " + findMaximum(weights, i).toString());
        System.out.println("Average weight: " + findAverage(weights, i).toString());
    }

    // A private method to find the min weight in a weights array:
    private static Weight findMinimum(Weight[] weights, int weightCount){
        Weight min = weights[0];
        for(int i = 1; i < weightCount; i++){
            if (weights[i].lessThan(min)){
                min = weights[i];
            }
        }
        return min;
    }

    // A private method to find the max weight in a weights array:
    private static Weight findMaximum(Weight[] weights, int weightCount){
        Weight max = weights[0];
        for(int i = 1; i < weightCount; i++){
            if (!weights[i].lessThan(max)){
                max = weights[i];
            }
        }
        return max;
    }

    // A private method to find the average weight in a weights array:
    private static Weight findAverage(Weight[] weights, int weightCount){
        Weight avg = new Weight(0, 0.0);
        for(int i = 0; i < weightCount; i++){
            avg.addTo(weights[i]);
        }
        avg.divide(weightCount);
        return avg;
    }
}