
from flask import Flask,render_template,session,url_for,request,redirect
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask import jsonify,json
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'sec_b'
app.config['MONGO_URI'] = 'mongodb://attendance:attendance123@ds041178.mlab.com:41178/sec_b'

mongo = PyMongo(app)
bcrypt = Bcrypt(app)



@app.route('/')
def index_main():

    return redirect(url_for('index',message="true"))



@app.route('/index')
def index():

    if 'usernameF' in session:


        print(session['usernameF'] +"oo")

        return  redirect(url_for('faculty_login'))

    if 'usernameS' in session:

        print(session['usernameS'])

        return  redirect(url_for('student_login'))



    message="true"
    message = request.args['message']
    return render_template('index.html',message=message)



@app.route('/student_login', methods = ['POST','GET'])
def student_login():

    print(session.get('usernameS'))

    if  session.get('usernameS'):


        students = mongo.db.students
        login_user = students.find_one(

            # "$and":[
                    {
                        "ID" : session.get('usernameS')
                    }

            # ]


        )

        courses = login_user['courses']
        courses1 = mongo.db.courses
        obj = courses1.find_one(

                        # "$and":[
                                {
                                    "courses" : courses[0]
                                }

                        # ]


                    )
        print(obj )
        link=obj['link']
        print(link +"www")

        session['selected_course']=courses[0]
        return render_template('view_attendance.html',courses=courses,link=link,x="Student",user=login_user['ID'])





    if request.method == 'POST':


        username = request.form['usernameS']
        pwd = request.form['pwdS']
        print(username)
        print(pwd)
        #password = bcrypt.generate_password_hash(request.form['pwd']).decode('utf-8')
        #print(password)
        students = mongo.db.students
        login_user = students.find_one(

            # "$and":[
                    {
                        "ID" : username
                    }

            # ]


        )
        print(login_user)


        if login_user:

            password = login_user['password']
            if bcrypt.check_password_hash( password , pwd ):
                print("eee")
                session['usernameS'] = username

                courses = login_user['courses']
                courses1 = mongo.db.courses
                obj = courses1.find_one(

                        # "$and":[
                                {
                                    "courses" : courses[0]
                                }

                        # ]


                    )
                print(obj )
                link=obj['link']
                print(link +"www")
                session['selected_course']=courses[0]
                return render_template('view_attendance.html',courses=courses,link=link,x="Student",user=login_user['ID'])





       # return redirect(url_for('index'))


    return redirect(url_for('index',message = "wrong"))
    #return render_template('view_attendance.html',courses=['r'])




####################################################################################



@app.route('/faculty_login', methods = ['POST','GET'])
def faculty_login():


    print(session.get('usernameF'))

    if  session.get('usernameF'):


        professors = mongo.db.professor
        login_user = professors.find_one(

            # "$and":[
                    {
                        "ID" : session.get('usernameF')
                    }

            # ]


        )

        courses = login_user['courses']
        courses1 = mongo.db.courses
        obj = courses1.find_one(

                # "$and":[
                        {
                            "courses" : courses[0]
                        }

                # ]


            )
        print(obj )
        link=obj['link']
        print(link +"www")
        session['selected_course']=courses[0]
        return render_template('mark_attendance.html',courses=courses,link=link,x="Faculty",user=login_user['ID'])



    if request.method == 'POST':

        username = request.form['usernameF']
        pwd = request.form['pwdF']
        print(username)
        print(pwd)
        #password = bcrypt.generate_password_hash(request.form['pwd']).decode('utf-8')
        #print(password)
        professors = mongo.db.professor
        login_user = professors.find_one(

            # "$and":[
                    {
                        "ID" : username
                    }

            # ]


        )
        print(login_user)

        if login_user:

            password = login_user['password']
            if bcrypt.check_password_hash( password , pwd ):
                print("eee")
                session['usernameF'] = username
                courses = login_user['courses']

                courses1 = mongo.db.courses
                obj = courses1.find_one(

                        # "$and":[
                                {
                                    "courses" : courses[0]
                                }

                        # ]


                    )
                print(obj )
                link=obj['link']
                print(link +"www")
                session['selected_course']=courses[0]
                return render_template('mark_attendance.html',courses=courses,link=link,x="Faculty",user=login_user['ID'])




        #return redirect(url_for('index'))

    return redirect(url_for('index',message = "wrong"))
    #return render_template('mark_attendance.html',courses=['l'])

@app.route('/getlink', methods=['POST','GET'])
def getlink():

    if request.method == 'GET':



        selected_course=request.args["selected_course"]

        session['selected_course']=selected_course
        print(selected_course +"select")
        courses = mongo.db.courses
        obj = courses.find_one(

                # "$and":[
                        {
                            "courses" : selected_course
                        }

                # ]


            )
        print(obj)
        link=obj['link']
        print(link)
        obj={
            'courses':selected_course,
            'link':link
        }
        return jsonify(obj)
    return 0

@app.route('/start_attendance')
def start_attendance():
    from flask import session
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pprint
    import datetime
    import argparse
    import pickle
    today = datetime.date.today()
    formatted_date = today.strftime("%m-%d-%Y")
    print(formatted_date)

    present_students = open('present.pickle','rb')
    students = pickle.load(present_students)
    present_students.close()


    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)


    # sheet = client.open('face-attendance').sheet1
    if session['usernameS']:
        sheet = client.open(session['usernameS']).session['selected_course']
    if session['usernameF']:
        sheet = client.open(session['usernameF']).session['selected_course']

    result = sheet.get_all_records()
    # before attendance
    pp = pprint.PrettyPrinter()
    pp.pprint(result)
    # date-> col
    date_col_list = sheet.findall(formatted_date)
    date_col = date_col_list[0].col
    print(date_col)

    #roll_no_list ->row
    for student in students:
        cell_list = sheet.findall(student)
        for cell in cell_list:
            roll_number_row = cell.row
            sheet.update_cell(roll_number_row,date_col,'P')

    #Show sheet
    result = sheet.get_all_records()
    pp.pprint(result)


@app.route('/stop_attendance')
def stop_attendance():
    import cv2
    cv2.destroyAllWindows()






@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('usernameF', None)
   session.pop('usernameS', None)
   return redirect(url_for('index',message="true"))


if __name__ == '__main__':
    app.secret_key='secret'
    app.run(debug=True)
