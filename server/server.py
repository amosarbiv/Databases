from flask import Flask, render_template, redirect, url_for, request, make_response,session, send_file
import datetime
import LogicInterface
import json

app = Flask(__name__)
logic = LogicInterface.LogicInter("DbMysql15", "DbMysql15", "DbMysql15")
wrongPatterntSearch = False
tableResult = {}

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

@app.route('/logOut/<userName>', methods=['GET'])
def logOut(userName):
    resp = make_response(redirect(url_for('loginPage')))
    resp.set_cookie('successful_login', 'False')
    resp.set_cookie('userNameLogin', '')
    return resp


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
        playlist = logic.displayPlayList(name)
        global wrongPatterntSearch
        if (wrongPatterntSearch == True):
            SearchErrorPattern = "Wrong"
        else:
            SearchErrorPattern = None
        wrongPatterntSearch = False
        return render_template('PrivateZone.html', user=name, playlist=playlist, playlistLen=len(playlist), SearchError = SearchErrorPattern)

@app.route('/GetUserRating', methods = ['POST'])
def GetUserRating():
    results = request.get_json(silent=True)
    rating = results['rating']
    user = results['name'].split('-')[1].replace(" ","")
    songId = [int(s) for s in results['id'].split() if s.isdigit()][0]
    isInPlaylist = results['isInPlaylist']
    logic.playlistChangeRating(user, rating, songId, isInPlaylist)
    return ('', 204)

@app.route('/AddSongToPlaylist', methods = ['POST'])
def AddSongToPlaylist():
    results = request.get_json(silent=True)
    user = logic.GetUserName()
    songId = [int(s) for s in results['id'].split() if s.isdigit()][0]
    logic.AddSongToPlaylist(user, songId)
    return ('', 204)

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
    firstName =  request.form['firstName']
    lastName = request.form['lastName']
    country =  request.form['country']
    age = request.form['age']
    currUserName = logic.UpdateUserProfile(firstName,lastName,country,age)
    return ('', 204)

@app.route('/GetTableTimeMachine', methods=['GET'])
def GetTableTimeMachine():
     tableJson = logic.GetTableTimeMachine()
     return json.dumps(tableJson)

@app.route('/GetTableTrending', methods=['GET'])
def GetTableTrending():
     tableJson = logic.GetTableTrending()
     return json.dumps(tableJson)

@app.route('/GetUserSearchTerm', methods=['POST'])
def GetUserSearchTerm():
    arguments = request.get_json(silent=True)
    logic.GetUserSearchTerm(arguments)
    return ('', 204)

@app.route('/GetRecommendedData', methods=['GET'])
def GetRecommendedData():
    tableJson = logic.GetRecommendedData()
    return json.dumps(tableJson)

@app.route('/RetrieveSearchInfo', methods=['POST'])
def RetrieveSearchInfo():
    searchTerm = request.form['serachText']
    userName = logic.GetUserName()
    global tableResult
    tableResult = logic.RetrieveSearchInfo(userName, searchTerm)
    if(tableResult == False):
        global wrongPatterntSearch
        wrongPatterntSearch = True
        resp = make_response(redirect(url_for('PrivateZone', name=userName)))
        return resp
    else:
        resp = make_response(redirect(url_for('SearchZone', userName=userName,searchTerm=searchTerm)))
        return resp

@app.route('/SearchZone.html/<userName>/<searchTerm>', methods=['GET'])
def SearchZone(userName, searchTerm):
    global tableResult
    songsCount = len(tableResult['songs'])
    albumsCount = len(tableResult['album'])
    artistsCount = len(tableResult['artist'])
    return render_template('SearchZone.html', userName=userName, searchTerm=searchTerm, SearchResult=tableResult, songsCount=songsCount,albumsCount=albumsCount,artistsCount=artistsCount)

@app.route('/GetInfoPage', methods=['POST'])
def GetInfoPage():
    results = request.get_json(silent=True)
    user = logic.GetUserName()
    songId = [int(s) for s in results['id'].split() if s.isdigit()][0]
    logic.AddSongToPlaylist(user, songId)
    return ('', 204)

if __name__ == '__main__':
    app.secret_key = 'itsasecret'
    app.run(port=40001, host="0.0.0.0", debug=True)