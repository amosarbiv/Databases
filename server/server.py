from flask import Flask, render_template, redirect, url_for, request, make_response,session, send_file
import datetime
import DBapi

app = Flask(__name__)
FB = ""
dataBase = DBapi.DB("root", "LA1026vi", "test")

@app.route('/sign/loginPage.html', methods=['GET'])
def loginPage():
    if request.method == 'GET':
        return GET_Login()

@app.route('/sign/LoginAction', methods=['POST'])
def LoginAction():
    if request.method == 'POST':
        chkBox = request.form.get("checkbox-1")
        user = request.form['userNameLogin']
        password = request.form['passwordLogin']
        result = dataBase.CheckUserLogin(user, password)
        if ( result == -1 ):
             return render_template('sign/loginPage.html')
        else:
            if ( result ):
                return POST_Login(user, "True", chkBox)
            else:
                return render_template('sign/loginPage.html')

@app.route('/sign/SignUpAction', methods=['POST'])
def SignUpAction():
    if request.method == 'POST':
        user = request.form['userNameSignUp']
        password = request.form['passwordSignUp']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        age = request.form['age']
        country = request.form['country']
        radioGender = request.form.get("radioGender")
        if(radioGender == "Male"):
            radioGender = "M"
        if(radioGender == "Female"):
            radioGender = "F"
        else:
            radioGender = "N"

        result = dataBase.CreateUser(user, password, firstName, lastName, age, country, radioGender)
        if(result):
            return POST_Login(user, "True", False)
        else:
            return render_template('sign/loginPage.html')
            

def GET_Login():
    is_successful = request.cookies.get('successful_login')
    if is_successful == 'True':
        user = request.cookies.get('userNameLogin')
        return PrivateZone(user)
    else:
        return render_template('sign/loginPage.html')

def POST_Login(user, isSucces, chkBox):
    resp = make_response(redirect(url_for('PrivateZone', name=user)))
    if(chkBox):
        resp.set_cookie('successful_login', isSucces)
        resp.set_cookie('userNameLogin', user)
    return resp

@app.route('/PrivateZone.html/<name>', methods=['GET', 'POST'])
def PrivateZone(name):
    return render_template('PrivateZone.html', user=name)

if __name__ == '__main__':
    app.secret_key = 'itsasecret'
    app.run(port=8888, host="0.0.0.0", debug=True)
    






