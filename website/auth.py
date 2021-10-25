from flask import Blueprint,render_template,request,flash
auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return"<p>logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password=request.form.get('password')
        password2=request.form.get('password2')
        if len(email)<4:
            flash('Email must be greater than 3 characters',category='error')
        elif len(firstName)<2:
            flash('First name must be greater than 1 character',category='error')
        elif password!=password2:
            flash('Passwords dont match',category='error')
        elif len(password)<7:
            flash('Passwords must be atleast 7 characters ',category='error')
        else:
            
            flash('Account Created Successfully',category='success')
            #add user to Database

    return render_template("register.html")