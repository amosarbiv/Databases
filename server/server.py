from flask import Flask, render_template, redirect, url_for, request, make_response,session, send_file
import datetime
import LogicInterface
import json

app = Flask(__name__)
logic = LogicInterface.LogicInter("root", "LA1026vi", "test")

@app.route('/sign/loginPage.html', methods=['GET'])
def loginPage():
    if request.method == 'GET':
        return GET_Login(errorLogin=None, errorSign=None)

@app.route('/sign/LoginAction', methods=['POST'])
def LoginAction():
    if request.method == 'POST':
        chkBox = request.form.get("checkbox-1")
        user = request.form['userNameLogin']
        password = request.form['passwordLogin']
        result = logic.HandleLoginAction(chkBox,user,password)
        if ( result ):
            return POST_Login(user, "True", chkBox, True)
        else:
            return render_template('sign/loginPage.html', errorLogin="WrongCredentials", errorSign=None)

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
        result = logic.HandleUserCreation(user, password, firstName, lastName, age, country, radioGender)
        if(result):
            return POST_Login(user, "True", False, False)
        else:
            return render_template('sign/loginPage.html', errorLogin=None, errorSign="UserExists")
            

def GET_Login(errorLogin, errorSign):
    is_successful = request.cookies.get('successful_login')
    if is_successful == 'True':
        user = request.cookies.get('userNameLogin')
        return POST_Login(user,True,True,False)
    else:
        return render_template('sign/loginPage.html', errorLogin=errorLogin, errorSign=errorSign)

def POST_Login(user, isSucces, chkBox, setCookie):
    resp = make_response(redirect(url_for('PrivateZone', name=user)))
    if(chkBox and setCookie):
        resp.set_cookie('successful_login', isSucces)
        resp.set_cookie('userNameLogin', user)
    logic.MakeUserProfileJson(user)
    return resp

@app.route('/PrivateZone.html/<name>', methods=['GET', 'POST'])
def PrivateZone(name):
    if request.method == 'GET':
        return render_template('PrivateZone.html', user=name)

@app.route('/GetUserProfile', methods=['GET'])
def GetUserProfile():
    return logic.GetUserProfile()

@app.route('/ChangePlaylistPrivacy', methods=['POST'])
def ChangePlaylistPrivacy():
    privacy = request.get_json(silent=True)
    result = logic.ChangePlaylistPrivacy(privacy['privacy'])
    return ('', 204)

@app.route('/UpdateUserProfile', methods=['POST'])
def UpdateUserProfile():
    password = request.form['passWord']
    firstName =  request.form['firstName']
    lastName = request.form['lastName']
    country =  request.form['country']
    age = request.form['age']
    currUserName = logic.UpdateUserProfile(password,firstName,lastName,country,age)
    resp = make_response(redirect(url_for('PrivateZone', name=currUserName)))
    return resp

if __name__ == '__main__':
    app.secret_key = 'itsasecret'
    app.run(port=8888, host="0.0.0.0", debug=True)
    






