using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace HangmanWPF
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public int remainingAttempt = 6;
        public static string secretWord = GetWord.WordGetter();
        public List<string> lblSpots = new List<string>();
        public void UserGuess(string guessLetter, List<string> lblSpots)
        {
            int len = secretWord.Length;
            for (int i = 0; i < len; i++)
            {
                if (secretWord.Substring(i, 1) == guessLetter) lblSpots[i] = guessLetter;
            }
            string temp = "";
            foreach (string s in lblSpots) temp += s;
            if (temp == (string)spots.Content) remainingAttempt--;
            spots.Content = temp;
            if (remainingAttempt <= 0)
            {
                DisableButtons();
                MessageBox.Show("You Lost", "Hangman", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else if (temp == secretWord)
            {
                DisableButtons();
                MessageBox.Show("You Won!", "Hangman", MessageBoxButton.OK, MessageBoxImage.Information);
            }
        }
        private void GameReset()
        {
            MessageBox.Show("A new Secret word has been generated!", "Hangman", MessageBoxButton.OK, MessageBoxImage.Information);
            EnableButtons();
            for (int i = 0; i < secretWord.Length; i++)
            {
                lblSpots.Add("___ ");
            }
            string temp = "";
            foreach (string s in lblSpots) temp += s;
            spots.Content = temp;
        }
        private void DisableButtons()
        {
            A.IsEnabled = false;
            B.IsEnabled = false;
            C.IsEnabled = false;
            D.IsEnabled = false;
            E.IsEnabled = false;
            F.IsEnabled = false;
            G.IsEnabled = false;
            H.IsEnabled = false;
            I.IsEnabled = false;
            J.IsEnabled = false;
            K.IsEnabled = false;
            L.IsEnabled = false;
            M.IsEnabled = false;
            N.IsEnabled = false;
            O.IsEnabled = false;
            P.IsEnabled = false;
            Q.IsEnabled = false;
            R.IsEnabled = false;
            S.IsEnabled = false;
            T.IsEnabled = false;
            U.IsEnabled = false;
            V.IsEnabled = false;
            W.IsEnabled = false;
            X.IsEnabled = false;
            Y.IsEnabled = false;
            Z.IsEnabled = false;
        }
        private void EnableButtons()
        {
            A.IsEnabled = true;
            B.IsEnabled = true;
            C.IsEnabled = true;
            D.IsEnabled = true;
            E.IsEnabled = true;
            F.IsEnabled = true;
            G.IsEnabled = true;
            H.IsEnabled = true;
            I.IsEnabled = true;
            J.IsEnabled = true;
            K.IsEnabled = true;
            L.IsEnabled = true;
            M.IsEnabled = true;
            N.IsEnabled = true;
            O.IsEnabled = true;
            P.IsEnabled = true;
            Q.IsEnabled = true;
            R.IsEnabled = true;
            S.IsEnabled = true;
            T.IsEnabled = true;
            U.IsEnabled = true;
            V.IsEnabled = true;
            W.IsEnabled = true;
            X.IsEnabled = true;
            Y.IsEnabled = true;
            Z.IsEnabled = true;
        }
        public MainWindow()
        {
            InitializeComponent();
            GameReset();
        }
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
        private void D_Click(object sender, RoutedEventArgs e)
        {
            D.IsEnabled = false;
            UserGuess(D.Name, lblSpots);
        }
        private void E_Click(object sender, RoutedEventArgs e)
        {
            E.IsEnabled = false;
            UserGuess(E.Name, lblSpots);
        }
        private void F_Click(object sender, RoutedEventArgs e)
        {
            F.IsEnabled = false;
            UserGuess(F.Name, lblSpots);
        }
        private void G_Click(object sender, RoutedEventArgs e)
        {
            G.IsEnabled = false;
            UserGuess(G.Name, lblSpots);
        }
        private void H_Click(object sender, RoutedEventArgs e)
        {
            H.IsEnabled = false;
            UserGuess(H.Name, lblSpots);
        }
        private void I_Click(object sender, RoutedEventArgs e)
        {
            I.IsEnabled = false;
            UserGuess(I.Name, lblSpots);
        }
        private void J_Click(object sender, RoutedEventArgs e)
        {
            J.IsEnabled = false;
            UserGuess(J.Name, lblSpots);
        }
        private void K_Click(object sender, RoutedEventArgs e)
        {
            K.IsEnabled = false;
            UserGuess(K.Name, lblSpots);
        }
        private void L_Click(object sender, RoutedEventArgs e)
        {
            L.IsEnabled = false;
            UserGuess(L.Name, lblSpots);
        }
        private void M_Click(object sender, RoutedEventArgs e)
        {
            M.IsEnabled = false;
            UserGuess(M.Name, lblSpots);
        }
        private void N_Click(object sender, RoutedEventArgs e)
        {
            N.IsEnabled = false;
            UserGuess(N.Name, lblSpots);
        }
        private void O_Click(object sender, RoutedEventArgs e)
        {
            O.IsEnabled = false;
            UserGuess(O.Name, lblSpots);
        }
        private void P_Click(object sender, RoutedEventArgs e)
        {
            P.IsEnabled = false;
            UserGuess(P.Name, lblSpots);
        }
        private void Q_Click(object sender, RoutedEventArgs e)
        {
            Q.IsEnabled = false;
            UserGuess(Q.Name, lblSpots);
        }
        private void R_Click(object sender, RoutedEventArgs e)
        {
            R.IsEnabled = false;
            UserGuess(R.Name, lblSpots);
        }
        private void S_Click(object sender, RoutedEventArgs e)
        {
            S.IsEnabled = false;
            UserGuess(S.Name, lblSpots);
        }
        private void T_Click(object sender, RoutedEventArgs e)
        {
            T.IsEnabled = false;
            UserGuess(T.Name, lblSpots);
        }
        private void U_Click(object sender, RoutedEventArgs e)
        {
            U.IsEnabled = false;
            UserGuess(U.Name, lblSpots);
        }
        private void V_Click(object sender, RoutedEventArgs e)
        {
            V.IsEnabled = false;
            UserGuess(V.Name, lblSpots);
        }
        private void W_Click(object sender, RoutedEventArgs e)
        {
            W.IsEnabled = false;
            UserGuess(W.Name, lblSpots);
        }
        private void X_Click(object sender, RoutedEventArgs e)
        {
            X.IsEnabled = false;
            UserGuess(X.Name, lblSpots);
        }
        private void Y_Click(object sender, RoutedEventArgs e)
        {
            Y.IsEnabled = false;
            UserGuess(Y.Name, lblSpots);
        }
        private void Z_Click(object sender, RoutedEventArgs e)
        {
            Z.IsEnabled = false;
            UserGuess(Z.Name, lblSpots);
        }
    }
}