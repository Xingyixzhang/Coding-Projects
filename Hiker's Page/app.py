"""This python file will render page templates for the html files and pass datetime variable."""
from datetime import datetime

from flask import Flask, redirect, render_template, request, session, url_for
from passlib.hash import sha256_crypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '~\x99\x84\xb1\xdf\x99\xbd\x80\xf7Sq3\x1a6\x11U\
    xbf_\xd9\xde\x84\x0b\xbb\xb5\xf2\xdc,\x9b\xf3IV\xeb'

# Create an empty dictionary for future username-password(encrypted) storage.
key_pairs = {}

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    """Render the registration page for user input information. """
    if request.method == 'POST':
        new_user = {request.form['name']: sha256_crypt.encrypt(request.form['password'])}
        key_pairs.update(new_user)
        return redirect(url_for('admin_login'))
    return render_template('register.html', datetime=datetime.now())

@app.route('/login.html', methods=['GET', 'POST'])
def admin_login():
    """Render the log-in page and pass the current date and time. """
    error = None
    if request.method == 'POST':
        username = request.form['name']
        if username in key_pairs:
            if sha256_crypt.verify(request.form['password'], key_pairs.get(username)):
                session['username'] = request.form['name']
                return redirect(url_for('home'))
            error = 'Invalid Username or Password'
        else:
            error = 'Invalid Username or Password'
    return render_template('login.html', datetime=datetime.now(), error=error)

@app.route('/home.html')
def home():
    """Render the page to home.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('admin_login'))
    return render_template('home.html', datetime=datetime.now())

@app.route('/collection.html')
def collection():
    """Render the page to collection.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('admin_login'))
    return render_template('collection.html', datetime=datetime.now())

@app.route('/contact.html')
def contact():
    """Render the page to contact.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('admin_login'))
    return render_template('contact.html', datetime=datetime.now())

@app.route('/logout')
def logout():
    """To delete session in dictionary. """
    session.pop('username', None)
    return redirect(url_for('admin_login'))

if __name__ == "__main__":
    app.run(debug=True)
