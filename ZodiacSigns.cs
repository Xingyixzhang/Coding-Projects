using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FirstProject
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Your Name: ");
            var name = Console.ReadLine();

            Console.Write("How old are you? ");
            var age = Console.ReadLine();

            Console.Write("What's your birthday? (MM/DD/YYYY) "); // MM/DD/YYYY is the key! OR you can change the format.
            string birthDay = Console.ReadLine();
            DateTime date = new DateTime();
            try 
            { 
                date = Convert.ToDateTime(birthDay);
            }
            catch
            {
                Console.WriteLine("Error, please enter a valid date.");
            }

            // var birthdate = long.Parse(Console.ReadLine());
            // DateTime birth = DateTime.Parse(birthdate);

            var zodiacSign = "";
            switch (date.Month)
            {
                case 1: 
                    if (date.Day < 20)
                        zodiacSign = "Capricorn";
                    else
                        zodiacSign = "Aquarius";
                    break;
                case 2:
                    if (date.Day < 19)
                        zodiacSign = "Aquarius";
                    else
                        zodiacSign = "Pisces";
                    break;
                case 3:
                    if (date.Day < 21)
                        zodiacSign = "Pisces";
                    else
                        zodiacSign = "Aries";
                    break;
                case 4:
                    if (date.Day < 20)
                        zodiacSign = "Aries";
                    else
                        zodiacSign = "Taurus";
                    break;
                case 5:
                    if (date.Day < 21)
                        zodiacSign = "Taurus";
                    else
                        zodiacSign = "Gemini";
                    break;
                case 6:
                    if (date.Day < 21)
                        zodiacSign = "Gemini";
                    else
                        zodiacSign = "Cancer";
                    break;
                case 7:
                    if (date.Day < 23)
                        zodiacSign = "Cancer";
                    else
                        zodiacSign = "Leo";
                    break;
                case 8:
                    if (date.Day < 23)
                        zodiacSign = "Leo";
                    else
                        zodiacSign = "Virgo";
                    break;
                case 9:
                    if (date.Day < 23)
                        zodiacSign = "Virgo";
                    else
                        zodiacSign = "Libra";
                    break;
                case 10:
                    if (date.Day < 23)
                        zodiacSign = "Libra";
                    else
                        zodiacSign = "Scorpio";
                    break;
                case 11:
                    if (date.Day < 22)
                        zodiacSign = "Scorpio";
                    else
                        zodiacSign = "Sagittarius";
                    break;
                case 12:
                    if (date.Day < 22)
                        zodiacSign = "Sagittarius";
                    else
                        zodiacSign = "Capricorn";
                    break;
                default:
                    zodiacSign = "Your zodiac sign was not found. Please enter your birthday again :) ";
                    break;
            }

            Console.WriteLine("Your name is: {0} \nYou are {1} years old.\nAnd you are a(n) {2}!", name, age, zodiacSign);
            
        }
    }
}
