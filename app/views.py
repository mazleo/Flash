
from flask import render_template, url_for, redirect, request, flash
from app import app
from app.database import User, Message, db
from sqlalchemy.exc import IntegrityError

@app.route('/')
@app.route('/index')
def index():
    user = db.session.query(User).filter_by(logged_in = True).first()
    if user is not None:
        return redirect(url_for('room_code'))
    else:
        return render_template('index.html')

@app.route('/room-code')
def room_code():
    current_user = db.session.query(User).filter_by(logged_in = True).first()
    if current_user is not None:
        return render_template('roomCode.html', user = current_user)
    else:
        return redirect(url_for('/'))

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    current_user = db.session.query(User).filter_by(logged_in = True).first()
    form_room_code = request.form['room-code']
    messages = db.session.query(Message).filter_by(room_code = form_room_code).all()
    room_users = db.session.query(User).all()
    if current_user is not None:
        return render_template('chat.html', user = current_user, room_code = form_room_code, messages = messages, users = room_users)
    else:
        return redirect(url_for('/'))


@app.route('/signin', methods = ['POST'])
def signin():
    form_email = request.form['email']
    form_password = request.form['password']
    validate_email = db.session.query(User).filter_by(email = form_email).first() is not None
    validate_password = db.session.query(User).filter_by(password = form_password).first() is not None
    current_user = db.session.query(User).filter_by(email = form_email).first()
    if request.method == 'POST':
        if validate_email and validate_password:
            current_user.logged_in = True
            db.session.commit()
            return redirect(url_for('room_code'))
        elif not validate_email:
            flash('This login does not exist')
            return redirect(url_for('/'))
        elif not validate_password:
            flash('Incorrect password')
            return redirect(url_for('/'))
        
@app.route('/logout')
def logout():
    user = db.session.query(User).filter_by(logged_in = True).first()
    user.logged_in = False
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/signup', methods = ['POST'])
def signup():
    signup_error = None
    form_email = request.form['email']
    form_username = request.form['username']
    form_password = request.form['password']
    if request.method == 'POST':
        try:
            if not form_email or not form_username or not form_password:
                flash('Required fields are missing', 'error')
            else:
                user = User(email=form_email, username=form_username, password=form_password, logged_in=True)
                db.session.add(user)
                db.session.commit()

                flash('User successfully added')
                return redirect(url_for('room_code'))
        except IntegrityError:
            if db.session.query(User).filter_by(email = form_email).first() is not None:
                signup_error = 'This email already exists'
                return render_template('index.html', error = signup_error)
            if db.session.query(User).filter_by(username = form_username).first() is not None:
                signup_error = 'This username already exists'
                return render_template('index.html', error = signup_error)
    return redirect(url_for('room_code'))

@app.route('/show-data')
def show_data():
    return render_template('show-data.html', User = User.query.all(), Message = Message.query.all())

@app.route('/chat_msg', methods=['GET', 'POST'])
def chat_msg():
    if request.method == 'POST':
        form_message = request.form['message']
        form_room_code = request.form['room_code']
        current_user = db.session.query(User).filter_by(logged_in = True).first()
        room_users = db.session.query(User).all()

        message = Message(room_code = form_room_code, chat_msg = form_message, user = current_user)
        db.session.add(message)
        db.session.commit()
        
        current_messages = db.session.query(Message).filter_by(room_code = form_room_code).all()
        return render_template('chat.html', user = current_user, room_code = form_room_code, messages = current_messages, users = room_users)
