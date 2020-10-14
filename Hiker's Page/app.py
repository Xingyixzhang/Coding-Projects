"""This python file will render page templates for the html files and pass datetime variable."""
from datetime import datetime
import logging
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, request, session, url_for
from passlib.hash import sha256_crypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '~\x99\x84\xb1\xdf\x99\xbd\x80\xf7Sq3\x1a6\x11U\
    xbf_\xd9\xde\x84\x0b\xbb\xb5\xf2\xdc,\x9b\xf3IV\xeb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'

logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# db = SQLAlchemy(app)

# # Create a User model:
# class User(db.Model):
#     # Create columns and data type:
#     # user_id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), primary_key=True)
#     gender = db.Column(db.String(7), unique=False, nullable=False)
#     state = db.Column(db.String(10), unique=False, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=True)
#     password = db.Column(db.String(50), nullable=False)

#     # Create a 1-to-many relationship with the Post objects:
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         """ Define a way to print any User object. """
#         return f"User('{self.username}', '{self.gender}', '{self.state}')"

# # Create an Attempt object for User login logging purpose.
# class Attempts(db.Model):
#     attempt_id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     ipaddress = db.Column(db.String(20), nullable=False)
#     username = db.Column(db.String(20), db.ForeignKey('user.name'), nullable=False)

#     def __repr__(self):
#         """ Define a way to print any User object. """
#         return f"Post('{self.title}', '{self.post_date}', '{self.ipaddress}')"

# Create an empty dictionary for future username-password(encrypted) storage.
key_pairs = {}

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    """Render the registration page for user input information. """
    common_pwds = open('Common Passwords.txt', 'r').read()
    if request.method == 'POST':
        if request.form['password'] in common_pwds:
            error = "This password is too common, please choose another one."
            return render_template('register.html', datetime=datetime.now(), error=error)
        new_user = {request.form['name']: sha256_crypt.encrypt(request.form['password'])}
        key_pairs.update(new_user)
        return redirect(url_for('login'))
    return render_template('register.html', datetime=datetime.now())

@app.route('/login.html', methods=['GET', 'POST'])
def login():
    """Render the log-in page and pass the current date and time. """
    error = None
    time = datetime.utcnow()
    if request.method == 'POST':
        # app.logger('-- At %s', time)
        username = request.form['name']
        if username in key_pairs:
            if sha256_crypt.verify(request.form['password'], key_pairs.get(username)):
                session['username'] = request.form['name']
                app.logger.info('-- At %s, %s logged in successfully.', time, username)
                return redirect(url_for('home'))
            # Log failed attempts:
            app.logger.info('-- At %s, %s failed to log in.', time, username)
            error = 'Invalid Username or Password'
        else:
            # Log failed attempts:
            app.logger.info('-- At %s, %s failed to log in.', time, username)
            error = 'Invalid Username or Password'
    return render_template('login.html', datetime=time, error=error)

@app.route('/home.html')
def home():
    """Render the page to home.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', datetime=datetime.now())

@app.route('/collection.html')
def collection():
    """Render the page to collection.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('collection.html', datetime=datetime.now())

@app.route('/contact.html')
def contact():
    """Render the page to contact.html and pass the variable of current date and time. """
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('contact.html', datetime=datetime.now())

@app.route('/logout')
def logout():
    """To delete session in dictionary. """
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/pwupdate.html', methods=['GET', 'POST'])
def reset_pwd():
    """Page for user to reset password"""
    error = None
    if request.method == 'POST':
        username = request.form['name']
        if username in key_pairs:
            if sha256_crypt.verify(request.form['password'], key_pairs.get(username)):
                session['username'] = request.form['name']
                user = {request.form['name']: sha256_crypt.encrypt(request.form['new_pwd'])}
                key_pairs.update(user)
                return redirect(url_for('login'))
            error = 'Invalid Username or Password'
        else:
            error = 'Invalid Username or Password'
    return render_template('pwupdate.html', datetime=datetime.now(), error=error)

if __name__ == "__main__":
    app.run(debug=True)
