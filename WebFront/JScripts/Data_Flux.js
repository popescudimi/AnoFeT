/**
 * Created by Bogdan on 06.05.2017.
 */
function get_test_item()
{
    var xtp=new XMLHttpRequest();
    xtp.onreadystatechange=function ()
{
    if (xtp.readyState == 4 && xtp.status == 200) {
     document.getElementById("it_show").value =(xtp.readyState+xtp.response);
    }
};
    xtp.open("POST", "Items_Page.html", true);
    xtp.send("Stringu");
}