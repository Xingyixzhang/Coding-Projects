using System;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            // Ask the user to enter a date and store the data as DATETIME.
            System.Console.Write("Enter a date (mm-dd-yyyy): \t");
            string date = Console.ReadLine();

            // Ask the user for the number of days they want to add.
            System.Console.Write("How many days do you want to add?: \t");
            int daysToAdd = int.Parse(Console.ReadLine());  // Convert the input to integer value for desired number of days to add.

            // Store variables for month, day, and year.
            int month = int.Parse(date.Substring(0, 2));    // Convert the first 2 characters to integer for month.
            int day = int.Parse(date.Substring(3, 2));      // Convert the second 2 characters after the '-' to integer for day.
            int year = int.Parse(date.Substring(6, 4));     // Convert the last 4 characters to integer for year.

            // Declare a newDate variable as the final date after addition.
            string newDate = "Your new Date is: {0}-{1}-{2}.";
            int daysInTotal = daysToAdd + day;

            if (daysInTotal <= daysInMonth(month, year))
                day = daysInTotal;
            else
            {
                // Check if there is remaining days to add.
                while (daysInTotal > daysInMonth(month, year))
                {
                    if (month <= 12)
                    {
                        daysInTotal -= daysInMonth(month, year);
                        month++;
                    }
                    else
                    {
                        month -= 12;    //Set the month to 1;
                        year++;         // Start a new year.
                    }

                    day = daysInTotal;  // store the remainding days in the current month.
                }
            }

            Console.WriteLine(newDate, month, day, year);
        }

        static int daysInMonth(int month, int year)     // Specify how many days are in each month.
        {
            switch (month)
            {
                case 1:     return 31;
                case 2:        // Depend on weather the year is leap year or not.
                    if (year % 4 == 0)  return 29;
                    else    return 28;
                case 3:     return 31;
                case 4:     return 30;
                case 5:     return 31;
                case 6:     return 30;
                case 7:     return 31;
                case 8:     return 31;
                case 9:     return 30;
                case 10:    return 31;
                case 11:    return 30;
                case 12:    return 31;

                default:    return 0;   // Set a default value in case of other number's appearance.
            }
        }
    }
}
