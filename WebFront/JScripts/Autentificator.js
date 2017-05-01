/**
 * Created by Bogdan on 26.03.2017.
 */
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
    var sn,sp1,sp2,se,ok1=0;
    sn=document.getElementById('UserNAME').value;
    sp1=document.getElementById('Parola1').value;
    sp2=document.getElementById('Parola2').value;
    se=document.getElementById('email').value;
    if(sn=="")
    {
        window.alert("Te rog completeaza campul UserNAME");
    }
    else
    {
        if(sp1=="")
        {
            window.alert("Te rog introdu o parola");
        }
        else
        {
            if(sp2=="")
                window.alert("Te rog comfirma parola");
            else
                if(se=="")
                {
                    window.alert("Email plz");
                }
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
                document.getElementById("regC").submit();

            }
            else
            {
                window.alert("Email invalid!!!");
            }
        }
        document.getElementById("regC").submit();
    }

    // var socket = new WebSocket("ws://79.112.54.100:2516");
    //     socket.onopen = function () {
    //         alert("fdfd");
    //         socket.send('Ping bla');
    //     }
}