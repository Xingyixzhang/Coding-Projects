﻿using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Linq;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Media.Imaging;
using System.Windows.Controls;

namespace HangmanWPF
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private void Application_StartUp(object sender, StartupEventArgs e)
        {
            MainWindow main = new MainWindow();
            main.Title = "Hangman";
            main.Show();
        }
    }
}
