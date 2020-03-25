using System;
using System.Collections.Generic;
using System.Text;

namespace HangmanWPF
{
    static class GetWord
    {
        public static string WordGetter()
        {
            string[] mySecretWords = { "pretty", "implement", "homework", "programming", "hangman",
                                       "assembly", "stanley", "michael", "maggie", "princess", "samuel",
                                       "laptop", "picture", "huskey", "construction", "desktop", "military"};
            Random rand = new Random();
            int index = rand.Next(mySecretWords.Length);
            string word = mySecretWords[index];
            return word;
        }
    }
}
