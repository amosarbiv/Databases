from flask import Flask, render_template, redirect, url_for, request, make_response,session, send_file
import datetime
import DBapi
import json

app = Flask(__name__)
FB = ""
dataBase = DBapi.DB("root", "LA1026vi", "test")

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
        result = dataBase.CheckUserLogin(user, password)
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
        if(radioGender == "Male"):
            radioGender = "M"
        if(radioGender == "Female"):
            radioGender = "F"
        else:
            radioGender = "N"

        result = dataBase.CreateUser(user, password, firstName, lastName, age, country, radioGender)
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
    dataBase.MakeJsonUserDetails(user)
    return resp

@app.route('/PrivateZone.html/<name>', methods=['GET', 'POST'])
def PrivateZone(name):
    if request.method == 'GET':
        return render_template('PrivateZone.html', user=name)

@app.route('/UserDetails', methods=['GET','PUT'])
def UserDetails():
    if(request.method == 'GET'):
        f = open("server//tmpFiles//userDetails.json", "r")
        details = json.load(f)
        stringDetails = str(details)
        f.close()
        return json.dumps(details)
    #if(request.method == 'PUT'):
        #print(data)
        #return render_template('UserDetails.html',userDetails=stringDetails)

if __name__ == '__main__':
    app.secret_key = 'itsasecret'
    app.run(port=8888, host="0.0.0.0", debug=True)
    






