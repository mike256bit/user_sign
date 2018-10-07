from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="User Signup")
    
app.run()

@app.route("/", methods=['POST'])
def welcome():
    user_name = request.form['user']
    # password = request.form['pass1']
    # pass_ver = request.form['pass2']
    # user_email = request.form['email']

    return render_template('welcome.html', user=user_name)