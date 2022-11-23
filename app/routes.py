import requests
import json
from pprint import pprint as pp
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app
from app.forms import SignUpForm, LogInForm, WorkoutNotes
from app.models import User, Notes



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        print("Let's get it BRO!")
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(email, username, password)
        check_user = User.query.filter(
            (User.username == username) | (User.email == email)).first()
        
        if check_user is not None:
            flash('User with username and or password already exists', 'danger')
            return redirect(url_for('signup'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user} have successfuly signed up. Sign in to get started", "primary")
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        
        if user is not None and user.check_password(password):
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
    flash("You have been logged out.", 'info')
    return redirect(url_for('index'))


@app.route('/notes')
def notes():
    note = Notes.query.all()
    return render_template('notes.html', note=note)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = WorkoutNotes()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        new_note = Notes(title=title, body=body, user_id=current_user.id)
        flash(f'{new_note.title} has been created.', 'success')
        return redirect(url_for('index'))

    return render_template('create_note.html', form=form)


@app.route('/notes/<note_id>')
def get_post(note_id):
    note = Notes.query.get(note_id)
    
    if not note:
        flash(f"Note with ID #{note_id} does not exist.", 'warning')
        return redirect(url_for('index'))
    return render_template("notes.html", note=note)


@app.route('/notes/<note_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(note_id):
    note = Notes.query.get(note_id)
    
    if not note:
        flash(f"Note with ID #{note_id} does not exist.", 'warning')
        return redirect(url_for('index'))
    
    form = WorkoutNotes()
    
    if form.validate_on_submit():
        new_title = form.title.data
        new_body = form.body.data
        note.update(title=new_title, body=new_body)
        flash(f"{note.title} was altered", 'success')
        return redirect(url_for('get_post', post_id=note.id))

    return render_template("edit_note.html", note=note, form=form)


@app.route('/notes/<note_id>/delete', methods=['GET'])
@login_required
def delete_post(note_id):
    note = Notes.query.get(note_id)
    
    if not note:
        flash(
            f"The note with the ID #{note_id}, does not exist. Please check again.", 'warning')
        return redirect(url_for('index'))
    
    if note.author != current_user:
        flash("You do not have permission to edit this note.", 'danger')
        return redirect(url_for('index'))
    
    note.delete()
    flash(f"{note.title} has been deleted", 'info')
    return redirect(url_for('index'))


@app.route('/workout')
@login_required
def get_workout(*args):
    find = url + str(args)
    headers = {'Accept': 'application/json', 
           'Authorization': f'{API_Key}'}
    r = requests.get(find=find, headers=headers)
    r
    r.content
    pp(json.loads(r.content))
    
    
    
    return render_template("work_out.html",)
