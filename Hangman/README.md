# Hangman WPF Game
## User Interface Design 
#### MainWindow.xaml
1. The initial UI layout (the word spots do not appear until you run the app and a random word has been generated):
```xaml
        <Label Name="spots" HorizontalAlignment="Center" Margin="0,250,0,0" />
```
![Initial UI](https://github.com/Xingyixzhang/Coding-Projects/blob/master/Hangman/images/IniUI.png "Initial UI(without word line")
2. The Use of Grid.Resources to help prevent (letter buttons) code redundancy:
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
## 
