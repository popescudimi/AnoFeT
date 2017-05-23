from os                 import curdir, sep, path
from DBController       import DBConnection
from BaseHTTPServer     import BaseHTTPRequestHandler, HTTPServer
from ServerFunctions    import register, login, validate_token, item_category, search_item
import json



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

        if 'Sbox' in raw_request:
            return search_item(self, raw_request.split('>')[1])

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