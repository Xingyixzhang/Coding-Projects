using System;
using System.Collections.Generic;
using System.Text;

namespace Hangman
{
    static class GetWord
    {
        public static string WordGetter()
        {
            string[] mySecretWords = { "Bananas", "Island", "homework", "Family", "hangman", "robot", "president",
                                       "Crab", "stanley", "Harbor", "Noodles", "", "Learning", "Savages", "Teakwood",
                                       "Chocolate", "Runner", "huskey", "Hiking", "Microsoft", "military"};
            Random rand = new Random();
            int index = rand.Next(mySecretWords.Length);
            string word = mySecretWords[index];
            // word = "Rachel";
            return word;
        }
    }
}
