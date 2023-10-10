from flask import Flask,render_template,redirect,request
import os
import mysql.connector
app1=Flask(__name__)
db=mysql.connector.connect(host="localhost",user="root",password="",database="cart")
app1.config['TEMPLATES_AUTO_RELOAD'] = True
app1.template_folder = os.path.abspath('templates')
app1.config['SECRET_KEY'] = 'your_secret_key_here'


@app1.route('/')
def index():
    return "Login"

@app1.route('/contact/con')
def contact():
    return "hello using contact"


@app1.route('/name/<uname>')
def name(uname):
    html="<html><body><form method='post' action='/gett'>"
    html+="<input type='text' name='name'><br><input type='text' name='idd'><input type='submit'></form></body></html>"
    return html

@app1.route('/gett',methods=['POST','GET'])
def gett():
    name=request.form['name']
    id=request.form['idd']
    cursor=db.cursor()
    sql="insert into auser (name,password) values (%s,%s)"
    values=(name,id)
    cursor.execute(sql,values)
    db.commit()
    cursor.close()
    return "welcome "+name

@app1.route('/df')
def df():
    sql="select * from auser"
    cursor=db.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    html="<html><body><table><tr><th>name</th><th>Email</th><th>Password</th></tr>"
    for h,g,j in data:
        html+="<tr>"
        html+=f'<td>{h}</td><td>{g}</td><td>{j}</td>'
        html+="</tr>"
    return html

if __name__=='__main__':
    app1.run(host='0.0.0.0',debug=True)