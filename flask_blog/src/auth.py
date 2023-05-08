from flask import Blueprint, render_template, request, session, make_response, url_for, redirect, flash
from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from newsapi import NewsApiClient

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')

    if User.login_valid(email, password):
        User.login(email)
        return redirect(url_for('main.profile'))
    
    flash('Please check your login details and try again')
    return redirect(url_for('auth.login'))


@auth.route('/register')
def register():
    return render_template("register.html")

@auth.route('/register', methods=['POST'])
def register_post():
    # code to validate and add user to database
    email = request.form.get('email')
    password = request.form.get('password')
    
    new_user = User(email, password)
    
    # successfully able to add user to db
    if new_user.register(email, password):
        return redirect(url_for('auth.login'))
    
    flash('Email address already exists') 
    return redirect(url_for("auth.register"))


@auth.route('/logout')
def logout():
    session["email"] = None
    return redirect("/")