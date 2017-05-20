import logging
import mimetypes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from DBController   import DBConnection
from os import curdir, sep, path
import random ,string
import json
import calendar
#Cookie (lib)
#Cookie=Cookie.Simple=Cookie(.self.headers["Cookies"])
#vezi documentatie base hhtp server
#for c_in headers:
#send_header("set.cookie.p")..
#js -ajax -> //cauta
#jason dump
#response.header=["set-cookie"]="s_id"=1234";

#global
token_vector={}
#=================================pt transformarea unei date primite din SQL in ceva calumea
def convert_todate(an, luna, zi):
    an_bun=an.split('(')
    zi_num=calendar.weekday(int(an_bun[1]),int(luna),int(zi))
    zi_name=calendar.day_name[zi_num]
    good_date=calendar.month_name[int(luna)]+' '+an_bun[1]+' '+zi_name+zi
    return good_date

#==========================================================================
#pt general use (category items) -folosita in functii care iau iteme direct
#nu folosi la altceva!
def item_like_support(selfie,querry):
    prearanged_querry = str(querry).split(',')
    uname_querry = selfie.db_conn.execute("select username from site_users where id=" + prearanged_querry[1])
    uname_rdy = str(uname_querry).translate(None, '()[]",')
    uname_rdy = uname_rdy.translate(None, "'")
    iname_rdy = prearanged_querry[2].translate(None, "'")
    #print uname_querry
    #print str(prearanged_querry)
     #===============JSON POWAH!!!================================
    #un fisier json e un fisier k=cheie valoare dupa cum probabil se si observa
    #un fisier json poate fi si vector de vectori de chei valori (lista ar fi un cuv mai bun) , but let's keep things simple
    raspuns_json=json.dumps({'item_name': iname_rdy,'date_posted':convert_todate(prearanged_querry[4],prearanged_querry[5],prearanged_querry[6]), 'item_description': prearanged_querry[3],'publisher':uname_rdy},indent = 4, separators = (',', ': '))
    return raspuns_json

#============================================================================
#============================================================================

#=====pt pg de iteme======
def item_item(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Item%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de festivals======
def item_festival(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Festival%' or title LIKE '%Contest%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Ceremonii======
def item_ceremony(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Ceremony%' or title LIKE '%Gathering%'order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Restaurants======
def item_restaurant(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Restaurant%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Pubs======
def item_pub(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Pub%' or title LIKE '%Cafe%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Hotels======
def item_hotel(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Hotel%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Party======
def item_party(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Party%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt pg de Titles======
def item_title(selfie):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%Title%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    itmw=item_like_support(selfie,querry)
    return itmw
#=========================
#=====pt Search======
def search_item(selfie,msg):
    querry = selfie.db_conn.execute("select * from (select * from items where title LIKE '%"+msg+"%' order by DBMS_RANDOM.RANDOM) where rownum<2")
    print "aici"
    print msg;
    print querry;
    if str(querry)!="[]":
        itmw=item_like_support(selfie,querry)
    else:
        itmw=json.dumps({'item_name': "Void Error",
                               'date_posted': "Search Harder!",
                               'item_description': "This is not an Error ", 'publisher': "Red Screen of Error"}, indent=4,
                              separators=(',', ': '))

    return itmw

#===============================================================================================================================================
#====Register data Processer====
def reg_data_processer(reg_request):
    it=0
    vect_info = ["" for x in range(6)]
    form = reg_request.split('&')
    for f in form:
        f = [f[:f.find("=")], f[f.find("=") + 1:]]
        vect_info[it]=f[1]
        it=it+1
    vect_info[3]=vect_info[3].replace('%40','@')
    return vect_info

#==========================Verifiers=====================================(care vrea poate sa faca o verificare mult mai stricta si mai calumea)
#informatiile pt inregistrare sunt verificate sa fie bune
def verify_corect_reg_info(request):
    if len(request[0])>3:
        if len(request[1])>5:
            if(request[1]==request[2]):
                if('@' in request[3] and '.' in request[3] and len(request[3])>8):
                    if(len(request[4])>3):
                        if(len(request[5])>3):
                            return True
    return False
#verifica daca nu este deja un utilizator cu un username asemanator sau cu email la fel
def verify_database_for_reg(selfie,request):
    uq="select * from site_users where USERNAME LIKE '%"+request[0]+"%'"
    unameQ=selfie.db_conn.execute(uq)
    emailQ=selfie.db_conn.execute("select * from site_users where EMAIL LIKE '%"+request[3]+"%'")
    if(str(unameQ)=='[]' and str(emailQ)=='[]'):
        return True
    return False
#===============================================================================================================================================
#The Tokenizer
def token_baker():
    token="";
    for c in range(1,10):
        t=random.randint(0,1);
        if(t==0):
            char=str(random.randint(0,9));
            token=token+char;
        else:
            char=str(random.choice(string.lowercase))
            token=token+char
    print token
    return token




#===============================================================================================================================================
def inregistrare(selfie,raw_request):
    processed_request=reg_data_processer(raw_request)
    if(verify_corect_reg_info(processed_request)==True):
        if(verify_database_for_reg(selfie,processed_request)==True):
            count=str(selfie.db_conn.execute("select count(*) from site_users")).split('(')
            number=int(count[1].split(',')[0])
            print number
            number=number+1
            #insertop="insert into site_users VALUES ("+str(number)+","+"'"+processed_request[5]+"'"+","+"'"+processed_request[4]+"'"+","+"'"+processed_request[3]+"'"+","+"TO_TIMESTAMP(SYSDATE)"+","+"'"+processed_request[0]+"'"+","+"'"+processed_request[1]+"'"+","+"'"+"A Question?"+"'"+","+"'"+"Maybye"+"'"+")"
            #str(insertop);
            #print insertop
            selfie.db_conn.callProcedure("insert_site_users",(number,processed_request[5],processed_request[4],processed_request[3],processed_request[0],processed_request[1],"A Question?","Maybye"))
            #selfie.connection.comit()
            print "am facut inregistrarea"
            #to be continued




def logare(selfie,raw_request):
    request=raw_request.split("<!>")
    request[0]=request[0].replace("Log","",1)
    querry="select * from site_users where USERNAME LIKE '"+request[0]+"' AND PASSWORD LIKE '"+request[1]+"'";
    q_serch=selfie.db_conn.execute(querry);
    if(str(q_serch)=='[]'):
        raspuns=json.dumps({"Response":"Bad","Token":"0"},indent = 4, separators = (',', ': '))
        return raspuns
    else:
        fortune_cookie=token_baker()
        global token_vector
        token_vector[fortune_cookie] = request[0]
        raspuns = json.dumps({"Response": "Good", "Token": fortune_cookie}, indent=4, separators=(',', ': '))
        return raspuns

def validare_token(selfie,raw_request):
    request=raw_request.split(',');
    global token_vector
    if request[1] in token_vector.keys() :
        raspuns=json.dumps({"verify":"Ok"},indent=4,separators=(',', ': '))
        return raspuns
    else:
        raspuns = json.dumps({"verify": "No"}, indent=4, separators=(',', ': '))
        return raspuns



#==========================================dispatcher==============================================
#isi da seama ce fel de request primeste si trimite inapoi raspunsul bun
#not ready yet -just for getting the ideea scope-
def dispatcher(selfie,raw_request):
    if 'UsernameBox' in raw_request:
        inregistrare(selfie,raw_request)
    #nu uita de return
    if 'Log' in raw_request and '<!>' in raw_request:
        raspuns_json=logare(selfie,raw_request)
        return raspuns_json
    if 'Token,' in raw_request:
        raspuns_json=validare_token(selfie,raw_request)
        return raspuns_json
    if 'ItemP' in raw_request:
        raspuns_json = item_item(selfie)
        return raspuns_json
    if 'FestivalP' in raw_request:
        raspuns_json = item_festival(selfie)
        return raspuns_json
    if 'CeremonyP' in raw_request:
        raspuns_json = item_ceremony(selfie)
        return raspuns_json
    if 'PubP' in raw_request:
        raspuns_json =item_pub(selfie)
        return raspuns_json
    if 'RestaurantP' in raw_request:
        raspuns_json=item_restaurant(selfie)
        return raspuns_json
    if 'HotelP' in raw_request:
        raspuns_json=item_hotel(selfie)
        return raspuns_json
    if 'PartyP'in raw_request:
        raspuns_json = item_party(selfie)
        return raspuns_json
    if 'TitleP'in raw_request:
        raspuns_json = item_title(selfie)
        return raspuns_json
    if 'Sbox' in raw_request:
        msg=raw_request.split('>')
        raspuns_json = search_item(selfie,msg[1])
        return raspuns_json
    raspuns_json = json.dumps({'item_name': "Magical Error",
                               'date_posted': "It's an error date :)",
                               'item_description': "Those errors man.... I mean look at them... ", 'publisher': "Red Screen of Error"}, indent=4,
                              separators=(',', ': '))
    return raspuns_json;

#===================================================================================================
class AppHandler(BaseHTTPRequestHandler):
    db_conn = DBConnection.connect("project1", "project1", "localhost") #la mine PROJECT1 e project1,modifica daca vrei sa iti mearga

    def do_GET(self):
        content_type = {
            '.css' : 'text/css',
            '.gif' : 'image/gif',
            '.htm' : 'text/html',
            '.html': 'text/html',
            '.jpeg': 'image/jpeg',
            '.jpg' : 'image/jpg',
            '.js'  : 'text/javascript',
            '.png' : 'image/png',
            '.text': 'text/plain',
            '.txt' : 'text/plain',
        }


        print self.path

        if self.path == "/":
            self.path = "/index.html"
        if self.path == "favico.ico":
            return

        self.path =  "../WebFront" + self.path

        fname, ext = path.splitext(self.path) # Splits the given string into the simple path and the extension of the final file(including the lading dot, ".html"")
        if ext in content_type.keys():
            with open(self.path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', content_type[ext])
                self.end_headers()
                self.wfile.write(f.read())
        return

    def do_HEAD(self):
        logging.debug("HEAD")



    def do_POST(self):
        print "POST"
        recived=str(self.rfile.read(int(self.headers['Content-Length'])))
        raspuns_json=dispatcher(self,recived)

        #===========================send response to webpage====================

        #t=randint(0,9000);
        self.send_response(200)
        #self.send_header("content-type","text/html")
        self.send_header("content-type","application/json")
        self.end_headers()
        self.wfile.write(raspuns_json)#jason.dumps(content)
        return



def run(server=HTTPServer, handler=AppHandler, port=2526):
    server_address = ('', port)
    httpd = server(server_address, handler)
    print "Started the HTTP Server at port", port
    httpd.serve_forever()

run()