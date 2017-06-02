/**
 * Created by Bogdan on 13.05.2017.
 */
/* Uses Data_flux functions, so place script after Data_Flux script in html page*/
/*================================================================================*/
/*not working...
function Next_fake_Page_Removal()

{
    var a=document.getElementsById("bd");
    var b=document.getElementById("main");
    b.outerHTML="";
    b.innerHTML="";
    b.parentNode.removeChild(b);
    delete b;
    var divm=document.createElement('div');
    divm.id="main";
    a.appendChild(divm);
}
*/
//=================================================
function get_item()
{
    var i=0;
    var msg="ItemP";
    var pg="Items_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_festival() {
    var i=0;
    var msg="FestivalP";
    var pg="Festivals_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}

function get_Restaurant() {
    var i=0;
    var msg="RestaurantP";
    var pg="Restaurants_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_Ceremony() {
    var i=0;
    var msg="CeremonyP";
    var pg="Ceremonyes_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}

function get_Pub() {
    var i=0;
    var msg="PubP";
    var pg="Pubs_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_Hotel() {
    var i=0;
    var msg="HotelP";
    var pg="Hotels_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_Party() {
    var i=0;
    var msg="PartyP";
    var pg="Partys_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_Title() {
    var i=0;
    var msg="TitleP";
    var pg="Titles_Page.html";
    while (i<10)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_your_publicItems() {
    var i=0;
    var tok=localStorage.getItem("tok");
    tok=tok.replace(' ','');
    var msg="MyItem<!>"+tok;
    var pg="AccountPage.html";
    while (i<4)
    {
        get_test_item(pg,msg);
        i++;
    }
}
function get_private_items() {
    var i=0;
    var msg="Invite<!>";
    var tok=localStorage.getItem("tok");
    tok=tok.replace(' ','');
    msg=msg+tok;
    var pg="PrivateItems.html";
    while (i<5)
    {
        get_test_item(pg,msg);
        i++;
    }
}