from flask import Flask, render_template, redirect, url_for, request, make_response,session, send_file
import datetime
app = Flask(__name__)

@app.route('/sign/loginPage.html', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'GET':
        return GET_Login()

    if request.method == 'POST':
        user = request.form['userNameLogin']
        password = request.form['passwordLogin']
        if user == 'lavi' and password == '1234':
            POST_Login(user, 'False')
        else:
            POST_Login('fail', 'True')

def GET_Login():
    is_successful = request.cookies.get('successful_login')
    if is_successful == 'True':
        user = request.cookies.get('userNameLogin')
        return 'welcome %s' % user
    else:
        return render_template('sign/loginPage.html')

def POST_Login(user, isSucces):
    resp = make_response(redirect(url_for('post_login2', name = user)))
    resp.set_cookie('successful_login', isSucces)
    resp.set_cookie('userNameLogin', user)
    return resp

@app.route('/after_login2/<name>')
def post_login2(name):
    is_successful = request.cookies.get('successful_login')
    if is_successful == 'True':
        return 'welcome %s' % name
    else:
        return 'failedddddddd'

if __name__ == '__main__':
    app.secret_key = 'itsasecret'
    app.run(port=8888, host="0.0.0.0", debug=True)







