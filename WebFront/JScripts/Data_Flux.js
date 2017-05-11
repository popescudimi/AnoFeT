/**
 * Created by Bogdan on 06.05.2017.
 */
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


    //==========================
    var len,info_array;
    len = response.length;
    info_array=response.split('!');

    var ph2=document.createTextNode(info_array[0]);
    var ps=document.createTextNode("May 2000");
    var pp1=document.createTextNode(info_array[1]);
    var ps4=document.createTextNode(info_array[2]);
    //==========================
    //in reverse
    span.appendChild(ps);

    span4.appendChild(ps4);
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


function get_test_item()
{
    var xtp=new XMLHttpRequest();
    xtp.onreadystatechange=function ()
{
    if (xtp.readyState == 4 && xtp.status == 200) {
     document.getElementById("it_show").value =(xtp.readyState+xtp.response);
     decorator(xtp.response);
    }
};
    xtp.open("POST", "Items_Page.html", true);
    xtp.send("Stringu");
}
