import frappe
# data=[]
# def get_context(context):
#     context.users = data


@frappe.whitelist()
def get_userdata(user_email):
    # global data
    print(user_email)
    # data = frappe.db.sql(f"SELECT firstname FROM `tabRegistration` WHERE email='{user_email}'")
    # print(data)
    

