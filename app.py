from flask import Flask, render_template, request
from flask.ext.mysql import MySQL
from datetime import datetime
import hashlib

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'bmanager'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rkdgks*88'
app.config['MYSQL_DATABASE_DB'] = 'qbank'
# app.config['MYSQL_DATABASE_HOST'] = '10.238.129.37'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route("/")
@app.route("/main")
def main():
    return render_template('index.html')


@app.route('/showQuestion')
def showQuestion():
    sqlB="""select big_name from tbl_catBig"""
    cursor.execute(sqlB)
    cat_Big = cursor.fetchall()

    sqlM="""select mid_name from tbl_catMid"""
    cursor.execute(sqlM)
    cat_Mid = cursor.fetchall()

    return render_template('add_question.html', cat_Big= cat_Big, cat_Mid=cat_Mid)


@app.route('/addQuestion', methods=['POST'])
def add_question():
    severity = request.form['severity']
    big = request.form['cat_Big']
    mid = request.form['cat_Mid']
    sentence = request.form['sentence']
    answer = request.form['answer']
    comment = request.form['comment']
    regdate = datetime.today().date()
    rcount = 0
    wcount = 0

    sql = """insert into tbl_question (q_severity, q_catBig, q_catMid, q_sentence, """
    sql = sql + """q_answer, q_comment, q_regdate, q_rcount, q_wcount) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    param = (severity, big, mid, sentence, answer, comment, regdate, rcount, wcount)
    cursor.execute(sql, param)
    conn.commit()

    return render_template('loginsuccess.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = hashlib.md5(str(_password).encode('utf-8')).hexdigest()

    cursor.callproc('sp_createUser',(_name, _email, _hashed_password))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        # json.dumps({'message': '사용자 등록에 성공하였습니다.'})
        return render_template('index.html')
    else:
        # json.dumps({'사용자 등록에 실패하였습니다. 원인:' : str(data[0])})
        return render_template('signup.html')


@app.route('/showLogin')
def showLogin():
    return render_template('showLogin.html')


@app.route('/login', methods=['POST'])
def login():
    # read the posted values from the UI
    _name = request.form['inputName']
    _password = request.form['inputPassword']
    _hashed_password = hashlib.md5(str(_password).encode('utf-8')).hexdigest()

    sql = """select user_name, user_password from tbl_user where user_name=%s and user_password=%s"""
    param = (_name, _hashed_password)
    cursor.execute(sql, param)
    data = cursor.fetchall()

    if len(data) is 0:
        # json.dumps({'message': '로그인에 실패하였습니다. '})
        return render_template('loginfailed.html')
    else:
        # json.dumps({'message': '로그인에 성공하였습니다. '})
        return render_template('loginsuccess.html')

if __name__ =="__main__":
    app.run(host="0.0.0.0", debug=True)