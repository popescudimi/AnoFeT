/**
 * Created by Bogdan on 06.05.2017.
 */
/*function prepForReview(name) {
    localStorage.setItem("To_Review",name);
    window.location.replace("http://localhost:2526/Pages/ReviewPage.html");
}*/

function decorator (response) {
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

    var spacing=document.createTextNode("   ")
    var review=document.createTextNode("Review it!")
    var alink=document.createElement('a');

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
    span4.appendChild(spacing);
    alink.appendChild(review);//link to review it
    alink.title="Review it and View Reviews";
    alink.href="#";
    //singurul mod in care onclick chiar merge si listeneru nu se apeleaza imediat
    // It_name e vizibil si in functia din listener
    // atributul din mijloc de la addListener trebuie sa fie o referinta la o functie(altfel apeleaza instant fct) ori asa
    alink.addEventListener("click",function(){
        var newName=It_name;
        localStorage.setItem("To_Review",newName);
        window.location.replace("http://localhost:2526/Pages/ReviewPage.html");
                         },false);
    //alink.onclick="prepForReview(It_name)";
    span4.appendChild(alink);
    //====
    div4.appendChild(span4);

    p1.appendChild(pp1);
    div3.appendChild(p1);

    h2.appendChild(ph2);
    div2.appendChild(h2);

    div1.appendChild(div2);
    div1.appendChild(span);
    div1.appendChild(div3);
    div1.appendChild(div4);
    document.getElementById("main").appendChild(div1);

}


function get_test_item(pgn,req_type)
{
    var xtp=new XMLHttpRequest();
    xtp.onreadystatechange=function ()
    {
    if (xtp.readyState == 4 && xtp.status == 200) {
     //document.getElementById("it_show").value =(xtp.readyState+xtp.response);//jason.parse(text)
     decorator(xtp.response);
    }
    };
    xtp.open("POST",pgn, true);
    xtp.send(req_type);
}
//"Items_Page.html"