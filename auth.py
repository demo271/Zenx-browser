from flask import Blueprint, render_template, request, redirect, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'pass':
            session['user'] = username
            return redirect('/dashboard')
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
