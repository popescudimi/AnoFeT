function response_chk(response) {
    var procesed_response = JSON.parse(response);
    if (procesed_response.Stat == "Success!") {
        document.getElementById("description").value = "Success!";
        window.location.replace("http://localhost:2526/Pages/AccountPage.html");

    }
    if (procesed_response.Stat == "Bad Token") {
        window.location.replace("http://localhost:2526/Pages/Login.html");
    }
    if (procesed_response.Stat == "Bad Email") {
        document.getElementById("description").value = "Check Emails.";
    }
    if (procesed_response.Stat == "Error") {
        document.getElementById("description").value = "Something bad happened and your review could not be submited";
    }
}

function creater() {
    var title=document.getElementById("TitleT").value;
    var content=document.getElementById("description").value;
    var e = document.getElementById("category");
    var category = e.options[e.selectedIndex].text;
    var tk=localStorage.getItem("tok");
    var tick=document.getElementById('private').checked;
    var invites="";
    var type="";
    if(tick===false)
    {type="Public";}
    else
    {type="Private";
    invites=document.getElementById('invites').value;
    invites=invites.replace(' ','');
    }

    tk=tk.replace(' ','');

    var req=new XMLHttpRequest();
    req.onreadystatechange=function ()
    {
    if (req.readyState == 4 && req.status == 200) {

     response_chk(req.response);
    }
    };
    req.open("POST","ItemCreation.html", true);
    req.send("IObject<!>"+tk+"<!>"+type+"<!>"+title+" "+category+"<!>"+content+"<!>"+invites);
}
