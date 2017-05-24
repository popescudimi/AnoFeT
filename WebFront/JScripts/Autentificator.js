/**
 * Created by Bogdan on 26.03.2017.
 */
function reg_send(un,ps,cps,em,fn,nn)
{

    var tosend="UsernameBox="+un+"&"+"Password="+ps+"&"+"ConfirmPassword="+cps+"&"+"Email="+em+"&"+"FirstName="+fn+"&"+"FamilyName="+nn;
    var chk = new XMLHttpRequest();
        chk.onreadystatechange = function () {
            if (chk.readyState == 4 && chk.status == 200) {
                if (JSON.parse(chk.response).Response == "Success") {
                    window.location.replace("http://localhost:2526/Pages/Login.html")
                }
                if(JSON.parse(chk.response).Response == "User or Email taken")
                {
                    window.location.replace("http://localhost:2526/Pages/RegisterWait.html");
                }
                if(JSON.parse(chk.response).Response=="Bad Data")
                {
                    window.location.replace("http://localhost:2526/Pages/RegisterWait.html");
                }
            }
        };
        chk.open("POST", "User_email_pass.html", true);
        chk.send(tosend);
}
function Email_bun(x)
{
    var i = x.length;
    var n = x.length;
    var ok1=0,ok2=0,ok3=0;
    while (i--) {
        if(ok2===0 && x[i]==='.' && i!==(n-1))
        {
            ok1=1;
        }
        if(i>0 && x[i]==='@')
        {
            ok2=1;
        }
    }
    if(ok1 && ok2)
    {
        return true;
    }
    return false;
}
function verificare()
{
    var sn,sp1,sp2,se,ok1=0,fn,na;
    sn=document.getElementById("UserNAME").value;
    sp1=document.getElementById('Parola1').value;
    sp2=document.getElementById('Parola2').value;
    se=document.getElementById('email').value;
    fn=document.getElementById('Fname').value;
    na=document.getElementById("Nname").value;
    if(sn==="")
    {
        window.alert("Te rog completeaza campul UserNAME");
    }
    else
    {
        if(sp1==="")
        {
            window.alert("Te rog introdu o parola");
        }
        else
        {
            if(sp2==="")
                window.alert("Te rog comfirma parola");
            else
                if(se==="")
                {
                    window.alert("Email plz");
                }
                else
                    if(fn.length<3)
                        window.alert("Introdu un First Name Valid");
                    else
                        if (na.length<3)
                            window.alert("Introdu un Nume Valid");
                        else
                            ok1=1;
        }
    }
    if(ok1==1)
    {
        if(sp1!==sp2)
        {
            window.alert("Parolele nu se potrivesc!");
        }
        else
        {
            if(Email_bun(se)===true) {
                // document.write("AUTENTIFICARE REUSITA !!! WAHOO!!!!!");
                //window.location.replace("file:///E:/Facultate/Web/hot-orange/index.html#");
                //send info to server
                reg_send(sn,sp1,sp2,se,fn,na);
                //window.location.href='86.124.39.178:2526';


            }
            else
            {
                window.alert("Email invalid!!!");
            }
        }
    }

}