# Hangman WPF Game
## User Interface Design 
#### MainWindow.xaml
1. The initial UI layout (the word spots do not appear until you run the app and a random word has been generated):
```xaml
        <Label Name="spots" HorizontalAlignment="Center" Margin="0,250,0,0" />
```
![Initial UI](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Hangman/images/IniUI.png "Initial UI(without word line")
2. The Use of Grid.Resources to format buttons in one place, reducing code redundancy:
```xaml
<Grid.Resources>
    <Style TargetType="Button">
         <Setter Property="Background" Value="White" />
         <Setter Property="FontSize" Value="25" />
         <Setter Property="FontWeight" Value="Bold" />
         <Setter Property="Width" Value="40" />
         <Setter Property="Height" Value="40" />
    </Style>
</Grid.Resources>

<!-- ...(Hangman images and the label for empty char spots) -->

<Button x:Name="A" Content="A" HorizontalAlignment="Left" Margin="60,320,0,0" VerticalAlignment="Top" Click="A_Click" />
<Button x:Name="B" Content="B" HorizontalAlignment="Left" Margin="110,320,0,0" VerticalAlignment="Top" Click="B_Click" />
<Button x:Name="C" Content="C" HorizontalAlignment="Left" Margin="160,320,0,0" VerticalAlignment="Top" Click="C_Click"/>
<!-- ...(More buttons 'D' - 'Z') -->
```
## Logic Behind the Scene:
#### GetWords.cs
1. Created an array of strings as the words library.
2. Use System.Random class to generate random word from the library when the method WordGetter() is called.
```cs
static class GetWord
{
    public static string[] mySecretWords = { "Bananas", "Island", "homework", "Family", "hangman", "robot", "president",
                                   "Crab", "stanley", "Harbor", "Noodles", "", "Learning", "Savages", "Teakwood",
                                   "Chocolate", "Runner", "huskey", "Hiking", "Microsoft", "military"};
    public static string WordGetter()
    {
        Random rand = new Random();
        int index = rand.Next(mySecretWords.Length);
        string word = mySecretWords[index];
        // TESTING: word = "Rachel";
        return word;
    }
}
```
#### MainWindow.xaml.cs
1. Initialize **fields** for the partial class MainWindow: Window.
```cs
public int remainingAttempt;                        // Total attempts: 6.
public string secretWord;        // The random word, based on which the # of guessing spots are determined.
public List<string> lblSpots;      // spots for guessing the word.
public List<Image> hangmanBody;
```
2. In the default constructor public MainWindow(), **Initialize the components and Reset the game**.
![game start page](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Hangman/images/GameBegin.png "game begin page")
```cs
public MainWindow()
{
        InitializeComponent();
        GameReset();
}
```
3. In the **GameReset** method: 
- Assign values to the fields; 
- Hide hangman body components; 
- Enable all buttons.
![random word generated](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Hangman/images/newWordMsg.png "new word generated message")
```cs
        public void GameReset()
        {
          // Assign Values to the values:
            secretWord = GetWord.WordGetter();
            remainingAttempt = 6;
            hangmanBody = new List<Image>();
            lblSpots = new List<string>();
          // Inform the User that a random word has been generated:
            MessageBox.Show("A new Secret word has been generated!", "Hangman");
            hangmanBody.Add(head);
            hangmanBody.Add(body);
            hangmanBody.Add(left_arm);
            hangmanBody.Add(right_arm);
            hangmanBody.Add(left_leg);
            hangmanBody.Add(right_leg);
            
            hideHangman();
            EnableButtons();
            for (int i = 0; i < secretWord.Length; i++)
            {
                lblSpots.Add("____");
            }
            string temp = "";
            foreach (string s in lblSpots) temp += s + " ";
            spots.Content = temp;
        }
```
4. Ask the User after each game for **restart/quit** option:
```cs
        public void RestartOrNot()
        {
            if (MessageBox.Show("Restart?", "Hangman", MessageBoxButton.YesNo, MessageBoxImage.Question) == MessageBoxResult.Yes)
            {
                GameReset();
            }
            else
            {
                App.Current.MainWindow.Close();
            }
        }
```
5. Generate **event handlers** for each button:
![Game in Progress](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Hangman/images/Ingame.png "A screenshot when game is in progress")
```cs
        public void A_Click(object sender, RoutedEventArgs e)
        {
            A.IsEnabled = false;
            UserGuess(A.Name, lblSpots);
        }
        private void B_Click(object sender, RoutedEventArgs e)
        {
            B.IsEnabled = false;
            UserGuess(B.Name, lblSpots);
        }
        private void C_Click(object sender, RoutedEventArgs e)
        {
            C.IsEnabled = false;
            UserGuess(C.Name, lblSpots);
        }
        // ... D_Click --- C_Click
```
6. In the **UserGuess** method:
- Check if/where the letter is in the word; 
- Display the char in position / Body component in order;
- Check if you have running out of attempts(lost)/ won;
- Reveal the secret word on spots (if failed);
- Disable all buttons;
- Display Result message;
- Ask the User for restart/quit.
```cs
        public void UserGuess(string guessLetter, List<string> lblSpots)
        {
            int len = secretWord.Length;
            for (int i = 0; i < len; i++)
            {
                if (secretWord.Substring(i, 1).ToUpper() == guessLetter)
                {
                    lblSpots[i] = guessLetter;
                }
            }
            string temp = "";
            foreach (string s in lblSpots)
            {
                temp += s + " ";
            }
            if (temp == (string)spots.Content)
            {
                hangmanBody[6 - remainingAttempt].Visibility = Visibility.Visible;
                remainingAttempt--;
            }
            spots.Content = temp;

            if (remainingAttempt <= 0)
            {
                DisableButtons();
                spots.Content = secretWord.ToUpper();
                MessageBox.Show($"You Lost\nThe word is: {secretWord}", "Hangman", MessageBoxButton.OK, MessageBoxImage.Information);
                RestartOrNot();
            } // Lost
            else
            {
                string wordTemp = "";
                foreach (var ch in temp)
                {
                    if (Char.IsLetter(ch)) wordTemp += ch;
                }
                // MessageBox.Show(wordTemp);
                if (wordTemp == secretWord.ToUpper())
                {
                    DisableButtons();
                    MessageBox.Show("You Won!", "Hangman", MessageBoxButton.OK, MessageBoxImage.Information);
                    RestartOrNot();
                }
            } // Won
        }
```
