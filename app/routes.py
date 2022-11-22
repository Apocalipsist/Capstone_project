from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from app.forms import SignUpForm, LogInForm, WorkoutForm
from app.models import User, Workouts

    
# Create a route for our app
@app.route('/')
def index():
    # posts = Workouts.query.order_by(Workouts.date_created.desc()).all()
    return render_template('index.html')

# @app.route('/post')
# def posts():
#     posts = Posts.query.all()
#     return render_template('post.html', posts=posts)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print("Let's get it BRO!")
        # gather the data from form
        email= form.email.data
        username= form.username.data
        password= form.password.data
        print(email,username,password)
        # Check to see if we have a user with username andor password:
        check_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if check_user is not None:
            flash('User with username and or password already exists', 'danger')
            return redirect(url_for('signup'))
        # Add new user to database
        new_user = User(email=email,username=username,password=password)
        # Flash a success message
        flash(f"{new_user} have successfuly signed up", "primary")
        # Redirect back to home
        return redirect(url_for('index'))
    
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        # Get form data
        username = form.username.data
        password= form.password.data
        # Check to see if there is a user with that Username and Password
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            # log in user
            login_user(user)
            flash(f'{user} is now logged in.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username and/or password. Please try again.', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out", 'info')
    return redirect(url_for('index'))
