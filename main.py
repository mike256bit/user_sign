from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html', title="User Signup")

@app.route("/", methods=['POST'])
def welcome():

    #collect user data
    user_name = request.form['user']
    password = request.form['pass1']
    pass_ver = request.form['pass2']
    user_email = request.form['email']

    #initialize error messages
    no_user = ""
    no_pass = ""
    match_pass = ""
    bad_email = ""
    error_check = 0
    
    #input validation
    if user_name == "": #no username entered
        no_user = "Please enter a username."
        error_check += 1
    
    if password == "": #no password entered
        no_pass = "Please enter a password."
        error_check += 1
    elif len(password) < 4: #password less than 4 chars
        no_pass = "Password must be at least 4 characters."
        error_check += 1
    elif " " in list(password): #Space in password
        no_pass = "Password may not contain spaces."
        error_check += 1
    
    if password != pass_ver: #No match
        match_pass = "Passwords do not match."
        error_check += 1
    
    if user_email != "" and ("@" not in list(user_email) or "." not in list(user_email) or " " in list(user_email)): #email criteria
        bad_email = "Please enter a valid email."
        error_check += 1
    
    if error_check == 0: #if no errors, render welcome template
        return render_template('welcome.html', title="Welcome!", user=user_name)
    else: #if any errors, render signup with error messages
        return render_template('signup.html', title="User Signup", user_error=no_user, pass1_error=no_pass,pass2_error=match_pass, email_error=bad_email)

app.run()