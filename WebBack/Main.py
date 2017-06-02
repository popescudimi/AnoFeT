from os                 import curdir, sep, path
from DBController       import DBConnection
from BaseHTTPServer     import BaseHTTPRequestHandler, HTTPServer
from ServerFunctions    import login, register, validate_token, item_category, search_item, review_getter, review_inserter, public_getter, insert_item
import json
import random



#Cookie (lib)
#Cookie=Cookie.Simple=Cookie(.self.headers["Cookies"])
#vezi documentatie base hhtp server
#for c_in headers:
#send_header("set.cookie.p")..
#js -ajax -> //cauta
#jason dump
#response.header=["set-cookie"]="s_id"=1234";


#global

#====================================================
# def generate_token():
#     token = ""
#     for c in range(1, 10):
#         if(random.randint(0,1) == 0):   # Digit in token
#             token = token + str(random.randint(0,9))
#         else:                           # Letter in token
#             token = token + str(random.choice("abcdefghijklmnopqrstuvwxyz"))
#     return token
#
#
#
# def validare_token(selfie,raw_request):
#     request=raw_request.split(',')
#     global token_vector
#     if request[1] in token_vector.keys() :
#         raspuns=json.dumps({"verify":"Ok"},indent=4,separators=(',', ': '))
#         return raspuns
#     else:
#         raspuns = json.dumps({"verify": "No"}, indent=4, separators=(',', ': '))
#         return raspuns
#
# def logare(selfie, raw_request):
#     request = raw_request.split("<!>")
#     request[0] = request[0].replace("Log", "", 1)
#     querry = "select * from site_users where USERNAME LIKE '" + request[0] + "' AND PASSWORD LIKE '" + request[1] + "'"
#     q_serch = selfie.db_conn.execute(querry);
#     if (str(q_serch) == '[]'):
#         raspuns = json.dumps({"Response": "Bad", "Token": "0"}, indent=4, separators=(',', ': '))
#         return raspuns
#     else:
#         fortune_cookie = generate_token()
#         global token_vector
#         token_vector[fortune_cookie] = request[0]
#         raspuns = json.dumps({"Response": "Good", "Token": fortune_cookie}, indent=4, separators=(',', ': '))
#         return raspuns
#===================================================================================================

class AppHandler(BaseHTTPRequestHandler):

    content_type = {'.css' : 'text/css',
                    '.gif' : 'image/gif',
                    '.htm' : 'text/html',
                    '.html': 'text/html',
                    '.jpeg': 'image/jpeg',
                    '.jpg' : 'image/jpg',
                    '.js'  : 'text/javascript',
                    '.png' : 'image/png',
                    '.text': 'text/plain',
                    '.txt' : 'text/plain'}

    db_conn = DBConnection.connect("PROJECT1", "project1", "localhost") #la mine PROJECT1 e project1,modifica daca vrei sa iti mearga

    active_tokens = {}

    def dispatcher(self, raw_request):
        # ==========================================dispatcher==============================================
        # isi da seama ce fel de request primeste si trimite inapoi raspunsul bun
        # not ready yet -just for getting the ideea scope-

        if 'MyItem<!>' in raw_request:
            return public_getter(self, raw_request, self.active_tokens)

        if 'UsernameBox' in raw_request:
            return register(self, raw_request)
            # nu uita de return

        if 'Log' in raw_request and '<!>' in raw_request:
            return login(self, raw_request)

        if 'Token,' in raw_request:
            return validate_token(self, raw_request)

        if 'ItemP' in raw_request:
            return item_category(self, "item")
        if 'FestivalP' in raw_request:
            return item_category(self, "festival")
        if 'CeremonyP' in raw_request:
            return item_category(self, "ceremony")
        if 'PubP' in raw_request:
            return item_category(self, "pub")
        if 'RestaurantP' in raw_request:
            return item_category(self, "restaurant")
        if 'HotelP' in raw_request:
            return item_category(self, "hotel")
        if 'PartyP' in raw_request:
            return item_category(self, "party")
        if 'TitleP' in raw_request:
            return item_category(self, "title")

        if 'Review_Get>' in raw_request:
            return review_getter(self,raw_request)
        if 'Review_Submit<!>' in raw_request:
            return review_inserter(self,raw_request, self.active_tokens)

        if 'Sbox' in raw_request:
            return search_item(self, raw_request.split('>')[1])

        if 'IObject' in raw_request:
            return insert_item(self, raw_request)

        return json.dumps({'item_name'       : "Magical Error",
                           'date_posted'     : "It's an error date :)",
                           'item_description': "Those errors man.... I mean look at them... ",
                           'publisher'       : "Red Screen of Error"},
                          indent=4,
                          separators=(',', ': '))


    def do_GET(self):
        if self.path == "favico.ico":
            return

        if self.path == "/":
            self.path = "/index.html"
        self.path =  "../WebFront" + self.path

        fname, ext = path.splitext(self.path) # Splits the given string into the simple path and the extension of the final file(including the lading dot, ".html"")
        if ext in self.content_type.keys():
            with open(self.path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', self.content_type[ext])
                self.end_headers()
                self.wfile.write(f.read())


    def do_POST(self):
        print "POST"
        received = str(self.rfile.read(int(self.headers['Content-Length'])))
        raspuns_json = self.dispatcher(received)

        #===========================send response to webpage====================
        self.send_response(200)
        #self.send_header("content-type","text/html")
        self.send_header("content-type","application/json")
        # pai daca tu trimiti json doar inapoi... ce kkt sa iti primeasca saraca pagina?
        self.end_headers()
        self.wfile.write(raspuns_json)#jason.dumps(content)
        return



def run(server=HTTPServer, handler=AppHandler, port=2526):
    server_address = ('', port)
    httpd = server(server_address, handler)
    print "Started the HTTP Server at port", port
    httpd.serve_forever()


if __name__ == "__main__":
    run()
