from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="testing", bollean = False)

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 charcter.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 charcter.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password is too short.', category='error')
        else:
            flash('Account created successfully.', category='success')


    return render_template("sign_up.html")

