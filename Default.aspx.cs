using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MyBookShelf_UserProfile
{
    public partial class _Default : Page // The class inherits from System.Web.UI.Page
    {
        /* Every ASP.NET page goes through a loading sequence. 
         * A load results when the client makes a request or post-back.
         * The Page.Load event handler allows pre-setup operations as part of handling the request or post-back.
         */
        protected void Page_Load(object sender, EventArgs e)
        {
            Page
        }

        protected void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        protected void btnLogin_Click(object sender, EventArgs e)
        {
            lbTest.Text = "It has changed!";
            ChangeToGreen(sender, e);
        }

        protected void ChangeToRed(object sender, EventArgs e)
        {
            lbTest.BackColor = System.Drawing.Color.Red;
        }

        protected void ChangeToGreen(object sender, EventArgs e)
        {
            lbTest.BackColor = System.Drawing.Color.Green;
        }
    }
}