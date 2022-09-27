// function myfunction() {
//     var user_email = document.getElementById('demo').value;
//     alert(user_email)


//     frappe.call({
//         method: 'demo3_app.www.user.userdata',
//         args: {
//             'user_email': user_email
//         },
//     });

// }
function myfunction() {
    var get_email = document.getElementById('email').value;
    // alert(get_email)
    frappe.call({
        method: 'demo3_app.www.data.get_details',
        args: {
            'get_email': get_email
        },
        // callback: function (r) {
        //     if (!r.exc) {

        //     }
        // }
    }).then(r => {
        console.log(r.message)
    });
}