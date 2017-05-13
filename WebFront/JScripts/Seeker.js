/**
 * Created by Bogdan on 13.05.2017.
 */
/* Pentru Search Box */
function Pre_Seek() {
    var to_search=document.getElementById("Sbox").value;
    localStorage.setItem("SearchValue",to_search);
    window.location.replace("http://localhost:2526/Pages/Search_Page.html");

}
function Seek()
{
    var to_search=localStorage.getItem("SearchValue");
    var req=new XMLHttpRequest();
    req.onreadystatechange=function ()
    {
        if(req.readyState==4 && req.status==200)
        {
            decorator(req.response);
        }
    };
    req.open("POST","Search_Page.html",true);
    req.send("Sbox>".concat(to_search));
}