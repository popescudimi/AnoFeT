/**
 * Created by Bogdan on 20.05.2017.
 */
function logger() {
    var uname,pass,msg;
    var ajs;
    var credentials;
    uname=document.getElementById('LogU').value;
    pass=document.getElementById('LogP').value;
    ajs=new XMLHttpRequest();
    ajs.onreadystatechange=function ()
    {
        if (ajs.readyState == 4 && ajs.status == 200)
        {
            credentials = JSON.parse(ajs.response);
            if (credentials.Response == "Good") {
                localStorage.setItem("Uname", uname);
                localStorage.setItem("tok", credentials.Token);
                window.location.replace("http://localhost:2526/");
            }
            else
            {window.location.replace("http://localhost:2526/");}
        }

    };
    ajs.open("POST","Login.html",true);
    msg="Log"+uname+"<!>"+pass;
    ajs.send(msg);

}




function Log_aspect() {
    var a;
    a="Welcome "+localStorage.getItem("Uname");
    document.getElementById("Login").textContent=a;
    document.getElementById("Login").href="http://localhost:2526/Pages/AccountPage.html";
    document.getElementById("Register").textContent="Logout";
    document.getElementById("Register").href="http://localhost:2526/Pages/DelogPage.html";
}

function check_token()
{
    if(localStorage.getItem("tok").length>5)
    {
        var chk = new XMLHttpRequest();
        chk.onreadystatechange = function () {
            if (chk.readyState == 4 && chk.status == 200) {
                if (JSON.parse(chk.response).verify == "Ok") {
                    Log_aspect();
                }
            }
        };
        chk.open("POST", "index.html", true);
        chk.send("Token,"+localStorage.getItem("tok"));
    }
}
function logout() {
    localStorage.setItem("Uname", "");
    localStorage.setItem("tok", "");
    window.location.replace('http://localhost:2526/');
}