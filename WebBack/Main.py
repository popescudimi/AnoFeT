from os                 import curdir, sep, path
from DBController       import DBConnection
from BaseHTTPServer     import BaseHTTPRequestHandler, HTTPServer
from ServerFunctions    import register, login, validate_token
import json
import string
import random
import logging
import calendar
import mimetypes


#Cookie (lib)
#Cookie=Cookie.Simple=Cookie(.self.headers["Cookies"])
#vezi documentatie base hhtp server
#for c_in headers:
#send_header("set.cookie.p")..
#js -ajax -> //cauta
#jason dump
#response.header=["set-cookie"]="s_id"=1234";



#===================================================================================================
class AppHandler(BaseHTTPRequestHandler):

    db_conn = DBConnection.connect("project1", "project1", "localhost") #la mine PROJECT1 e project1,modifica daca vrei sa iti mearga

    active_tokens = {}

    def dispatcher(self, raw_request):
        # ==========================================dispatcher==============================================
        # isi da seama ce fel de request primeste si trimite inapoi raspunsul bun
        # not ready yet -just for getting the ideea scope-

        if 'UsernameBox' in raw_request:
            register(self, raw_request)
            # nu uita de return

        if 'Log' in raw_request and '<!>' in raw_request:
            json_response = login(self, raw_request)
            return json_response

        if 'Token,' in raw_request:
            json_response = validate_token(self, raw_request)
            return json_response

        if 'ItemP' in raw_request:
            json_response = item_item(self)
            return json_response

        if 'FestivalP' in raw_request:
            json_response = item_festival(self)
            return json_response

        if 'CeremonyP' in raw_request:
            json_response = item_ceremony(self)
            return json_response

        if 'PubP' in raw_request:
            json_response = item_pub(self)
            return json_response

        if 'RestaurantP' in raw_request:
            json_response = item_restaurant(self)
            return json_response

        if 'HotelP' in raw_request:
            json_response = item_hotel(self)
            return json_response

        if 'PartyP' in raw_request:
            json_response = item_party(self)
            return json_response

        if 'TitleP' in raw_request:
            json_response = item_title(self)
            return json_response

        if 'Sbox' in raw_request:
            msg = raw_request.split('>')
            json_response = search_item(self, msg[1])
            return json_response

        json_response = json.dumps({'item_name': "Magical Error",
                                    'date_posted': "It's an error date :)",
                                    'item_description': "Those errors man.... I mean look at them... ",
                                    'publisher': "Red Screen of Error"}, indent=4,
                                   separators=(',', ': '))
        return json_response

    def do_HEAD(self):
        print 'HEAD'

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