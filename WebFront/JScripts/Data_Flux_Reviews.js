/**
 * Created by Bogdan on 31.05.2017.
 */
function decorator2 (response,wereToApp) {
    //========= Pt divuri ============
    var div1=document.createElement('div');
    div1.id="post-3";
    div1.className="entryBox"

    var div2=document.createElement('div');
    div2.className="title";
    var h2=document.createElement('h2');
    var span=document.createElement('span');
    span.className="date";

    var div3=document.createElement('div');
    div3.className="entry";
    var p1=document.createElement('P');
    p1.className="entry";

    var div4=document.createElement('div');
    div4.className="entryBottom"

    var span4=document.createElement('span');


    //==========================
    var info_response;
    //pregatirea jsonului
    info_response=JSON.parse(response);
    var It_name=info_response.item_name;

    var ph2=document.createTextNode(info_response.item_name);
    var ps=document.createTextNode(info_response.date_posted);
    var pp1=document.createTextNode(info_response.item_description);
    var ps4=document.createTextNode(info_response.publisher);
    //==========================
    //in reverse
    span.appendChild(ps);

    span4.appendChild(ps4);//publisher zone
    div4.appendChild(span4);

    p1.appendChild(pp1);
    div3.appendChild(p1);

    h2.appendChild(ph2);
    div2.appendChild(h2);

    div1.appendChild(div2);
    div1.appendChild(span);
    div1.appendChild(div3);
    div1.appendChild(div4);
    document.getElementById(wereToApp).appendChild(div1);
}
function get_the_item()
{
    var reviewed_it=localStorage.getItem("To_Review");
    reviewed_it=reviewed_it.replace(' ','');

    var xtp=new XMLHttpRequest();
    xtp.onreadystatechange=function ()
    {
    if (xtp.readyState == 4 && xtp.status == 200) {

     decorator2(xtp.response,"BottomHeaderWrapp");
    }
    };
    xtp.open("POST","ReviewPage.html", true);
    xtp.send("Sbox>"+reviewed_it);
}
function get_the_review()
{
    var reviewed_it=localStorage.getItem("To_Review");
    reviewed_it=reviewed_it.replace(' ','');

    var xtr=new XMLHttpRequest();
    xtr.onreadystatechange=function ()
    {
    if (xtr.readyState == 4 && xtr.status == 200) {

     decorator2(xtr.response,"main");
    }
    };
    xtr.open("POST","ReviewPage.html", true);
    xtr.send("Review_Get>"+reviewed_it);
}
function get_reviews()
{
    var i=0;
    while (i<3)
    {
        get_the_review();
        i++;
    }
}

function response_action(response){
    var procesed_response=JSON.parse(response);
    if(procesed_response.Ack=="Success!")
    {
        document.getElementById("reviu").value="Success!";
    }
    if(procesed_response.Ack=="Bad Token")
    {
        window.location.replace("http://localhost:2526/Pages/Login.html");
    }
    if(procesed_response.Ack=="Error")
    {
        document.getElementById("reviu").value="Something bad happened and your review could not be submited";
    }
}

function submit_review() {
    var content=document.getElementById("reviu").value;
    var tk=localStorage.getItem("tok");
    var itm=localStorage.getItem("To_Review");
    itm=itm.replace(' ','');

        var xhr=new XMLHttpRequest();
    xhr.onreadystatechange=function ()
    {
    if (xhr.readyState == 4 && xhr.status == 200) {

     response_action(xhr.response);
    }
    };
    xhr.open("POST","ReviewPage.html", true);
    xhr.send("Review_Submit<!>"+tk+"<!>"+itm+"<!>"+content);
}
