from flask import Blueprint,render_template
from flask_login import login_required,current_user,LoginManager


views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@views.route('/home',methods=['GET','POST'])
@login_required
def home():
        return render_template("home.html",user=current_user)

@views.route('/playVid',methods=['GET','POST'])
@login_required
def playVid():
        return render_template("playVid.html",user=current_user)        