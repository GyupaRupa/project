from flask import Flask, render_template, request, redirect, session
from models import db, Fcuser
from flask_wtf.csrf import CSRF, CSRFProtect
from forms import RegisterForm, LoginForm

app = Flask(__name__)

@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html', userid=userid)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        fcuser = Fcuser()
        fcuser.userid = form.data.get('userid')
        fcuser.username = form.data.get('username')
        fcuser.password = form.data.get('password')

        db.session.add(fcuser)
        db.session.commit()
        print('Success!')

        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['userid'] = form.data.get('userid')

        return redirect('/')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1q2w3e4r!@testdb.chnyz3y8a4jr.ap-northeast-2.rds.amazonaws.com:3306/testdb2'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost/testdb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'adqdasdqddasdqw'

csrf = CSRFProtect()    # 사이트위조공격 방지
csrf.init_app(app)

db.init_app(app)
db.app = app
db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)