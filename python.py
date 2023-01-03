import re
import datetime

def e_mail(s):
    pat = r"^\D[\w\.]+@([\w-]+\.)+[\w-]{2,4}$"
    if re.match(pat,s):
       return
    else:
       print("exiting the program")
       print(quit())

def start_date():
    try:
        s_date=input("start date as dd-mm-yyyy: ")
        datetime.strptime(s_date, "%d-%m-%y")
        return
    except:
        print("wrong start date format")
        start_date()

def finish_date():
    try:
        f_date=input("finish date as dd-mm-yyyy: ")
        datetime.strptime(f_date, "%d-%m-%y")
    except:
        print("wrong end date format")
        finish_date()

def phnum(phonum):
    pat = r"^01[0125][0-9]{8}$"
    if re.match(pat,phonum):
       return
    else:
       print("exiting the program")
       print(quit())


def first_page():
    first_input=input("1-login\n2-sign up\nenter choice:")
    if int(first_input)==1:
        login()
    elif int(first_input)==2:
        signup()
    else:
        first_page()


def view():
    file_project_r=open("project","r")
    index=0
    index_picked=0
    index_list=[]
    for line in file_project_r:
        if index==0:
            pass
        else:
            print(str(index)+" "+line.split(",")[1])
            index_list.append(line.split(",")[1])
        index+=1
    picked_index=int(input("Please enter index: "))
    file_project_r_1=open("project","r")
    for line in file_project_r_1:
        if index_picked==picked_index:
            print("Title: "+line.split(":")[1])
            print("Details: "+line.split(":")[2])
            print("Total target: "+line.split(":")[3])
            print("Star date: "+line.split(":")[4])
            print("finish date: "+line.split(":")[5])
        else:
            pass
        index_picked+=1



def login():
    global login_email
    login_mail=input("Email: ")
    login_password=input("password here: ")
    file_user_r=open("signup","r")
    for line in file_user_r:
        line_list=line.split(",")
        if line_list[2]==login_mail and line_list[3]==login_password:
            project(login_mail)
        else:
            print("incorrect email or password")
            login()

def signup():
    first_name=input("First name: ")
    last_name=input("Last name: ")
    email=input("email: ")
    (e_mail(email))
    password=input("password: ")
    confirm_pass=input("Confirm: ")
    if password != confirm_pass:
        print("enter password again ")
        first_page()
    mobile=input("Mobile: ")
    (phnum(mobile))
    with open('signup',"a") as f:
            f.write(first_name+','+last_name+','+email+','+password+','+mobile+'\n')
            login()


def project(login_elmail):
    which=input("create-1\nsearch-2\n enter choice: ")
    if int(which) == 1:
        create(login_elmail)
    elif int(which)==2:
        view()
    else:
        project()


def create(login_elmail):
    Title=input("enter your title: ")
    Details=input("enter your details: ")
    total_target=input("your target: ")
    s_date=start_date()
    f_date=finish_date()
    if s_date > f_date:
        print("error in date")
        create()
    else:
        with open('project',"a") as f:
            f.write(login_elmail+','+Title+','+Details+','+total_target+','+s_date+','+f_date+'\n')
            login()





(first_page())