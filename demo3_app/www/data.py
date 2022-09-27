# import frappe
# from distutils.spawn import find_executable
# # data=[]
# # def get_context(context):
# #     context.users = data

# no_cache=1
# @frappe.whitelist(allow_guest=True)
# def userdata(user_email="hello"):
#     # global data
#     print(user_email)
#     # data = frappe.db.sql(f"SELECT firstname FROM `tabRegistration` WHERE email='{user_email}'")
#     # print(data)
    

import frappe
from distutils.spawn import find_executable
datalist=[]
def get_context(context):
    for data in datalist:
       context.userlist=data
    datalist.clear()
   
@frappe.whitelist(allow_guest=True)
def get_details(get_email):
    global data
    # data=frappe.db.sql(f" SELECT firstname, lastname, fullname, gender, dob, phonenumber, email, username, address, city, state, zipcode, document  FROM `tabRegistration` WHERE email = '{get_email}'")
    data=frappe.db.get_all('Registration', filters={'email': get_email}, fields=['firstname', 'lastname','fullname','gender','dob','phonenumber','email','username','address','city','state','zipcode','document','signature','location'])
    print(data)
    datalist.append(data)

    