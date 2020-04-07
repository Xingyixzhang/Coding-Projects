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
1. Declare fields for the partial class MainWindow: Window.
```cs
public int remainingAttempt = 6;                        // Total attempts: 6.
public string secretWord = GetWord.WordGetter();        // The random word, based on which the # of guessing spots are determined.
public List<string> lblSpots = new List<string>();      // spots for guessing the word.
public List<Image> hangmanBody = new List<Image>();
```
2. In the default constructor public MainWindow(), Initialize the components and Reset the game.
```cs
public MainWindow()
{
        InitializeComponent();
        GameReset();
}
```
3. 
