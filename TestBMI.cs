using System;

namespace Tests
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your weight: (in lbs)   ");
            int weight = Convert.ToInt32(Console.ReadLine());

            Console.Write("Enter your height: (in inches)   ");
            int height = Convert.ToInt32(Console.ReadLine());

            float bmi = (weight * 703) / (height*height);
            string classify1, classify2; // classify2 is for the subcategories.
         
            if (bmi < 18.5) 
            {
                classify1 = "Underweight";
                if (bmi < 16)          { classify2 = "Severe thinness"; }
                else if (bmi <= 16.99) { classify2 = "Moderate thinness"; }
                else                   { classify2 = "Mild thinness"; }
            }
            else if (bmi <= 24.9)   // Values between 18.5 and 24.9 (including both ends).
            {
                classify1 = "Normal Weight";
                classify2 = "No sub category available";
            }
            else if (bmi <= 29.9)   // Values between 25 and 29.9 (including both ends).
            {
                classify1 = "Overweight";
                classify2 = "No sub category available";
            }
            else                    // Values bigger than 30. (including 30).
            {
                classify1 = "Obese";
                if (bmi <= 34.9)        { classify2 = "Obese class I"; }
                else if (bmi <= 39.9)   { classify2 = "Obese class II"; }
                else                    { classify2 = "Obese class III"; }
            }

        // Display the BMI value and the Classification to the user.
            Console.WriteLine("Your BMI is: {0}, and you are classified as {1}.",
                bmi, classify1+" ("+classify2+")");
        }
    }
}
