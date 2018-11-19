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

#,'https://www.googleapis.com/auth/drive'

def mark_attendance(students,course):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    print(course +"ggggggg")
    
    sheet = client.open(course).sheet1


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

# mark_attendance(students,args['course'])
#
