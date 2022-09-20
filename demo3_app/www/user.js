function myfunction() {
    var user_email = document.getElementById('demo').value;
    alert(user_email)


    frappe.call({
        method: 'demo3_app.www.user.get_userdata',
        args: {
            'user_email': user_email
        },
    });

}