using System;

namespace InClass_Assignment
{
    public class Person
    {
        // Properties referenced from https://docs.microsoft.com/en-us/dotnet/csharp/properties
        public string firstName { get; set; }
        private string middlename;
        private string lastname;
        public string middleName
        {
            get => middlename;
            set => middlename = value; // expression-bodied members.
        }
        
        public string lastName
        {
            get { return lastname; }
            set
            {
                // set => lastname = (!string.IsNullOrWhiteSpace(value)) ? value : throw new ArgumentException("Last name must not be blank");
                if (string.IsNullOrWhiteSpace(value))
                    throw new ArgumentException("Last name must not be blank.");
                lastname = value;
            }
        }
        public string fullName => $"{firstName} {lastName}";
    }
    class ThrowTest3
    {
        static void ProcessString(string s)
        {
            if (s == null)
            {
                throw new ArgumentNullException();
            }
        }

        static void Main()
        {
            Person person1 = new Person();
            person1.firstName = "Xingyi";
            person1.lastName = "Zhang";
            Console.WriteLine(person1.fullName);
            // Reference from https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/try-catch
            try
            {
                string s = null;
                ProcessString(s);
            }
            // Most specific:
            catch (ArgumentNullException e)
            {
                Console.WriteLine("\n{0} First exception caught.", e);
            }
            // Least specific:
            catch (Exception e)
            {
                Console.WriteLine("\n{0} Second exception caught.", e);
            }

            Console.WriteLine("\nPress Enter to continue...");
            Console.WriteLine();
        }
    }
    /*
     Output:
     System.ArgumentNullException: Value cannot be null.
     at Test.ThrowTest3.ProcessString(String s) ... First exception caught.
    */
}
