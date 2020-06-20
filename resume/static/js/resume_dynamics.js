const url = 'https://randomuser.me/api/?results=10';
fetch(url).then(response =>{
                    response.json()
                .then( function(data) {
                    console.log(data)
                })
                })
    var name = 'Peter';
    var formatedName = HTMLheaderName.replace("%data%", name);

    var contact = HTMLcontactGeneric;
    var mobile = HTMLmobile;
    var email = HTMLemail;
    var schoolStart = HTMLschoolStart;
    var workStart = HTMLworkStart;
    var projectStart = HTMLprojectStart

    $("#template_header").append(formatedName);
    $("#template_projects").append(projectStart);
    $("#template_work_exp").append(workStart);
    $("#template_education").append(schoolStart);
    $("#contact_info").append(email);
    $("#contact_info").append(mobile);
    $("#contact_info").append(contact);