import logging
import Cookie
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from DBController   import DBConnection
from os import curdir, sep, path


class AppHandler(BaseHTTPRequestHandler):



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

        #self.

        if self.path == "/":
            self.path = "/index.html"

        self.path =  "../WebFront" + self.path

        fname, ext = path.splitext(self.path) # Splits the given string into the simple path and the extension of the final file(including the lading dot, ".html"")
        if ext in content_type.keys():
            with open(self.path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', content_type[ext])
                self.end_headers()
                if self.path.endswith("index.html"):
                    self.wfile.write(f.read().format(""))
                else:
                    self.wfile.write(f.read())
        return

    def do_HEAD(self):
        logging.debug("HEAD")

    def do_POST(self):
        print "POST"
        form = str(self.rfile.read(int(self.headers['Content-Length']))).split('&')

        for f in form:
            f = [f[:f.find("=")], f[f.find("=")+1:]]
            print f



    def register_attempt(self, form):
        if form[0][0] == "Username" and form[1][0] == "Password" and form[2][0] == "Confirm" and form[3][0] == "Email":
            return True

    def register(self, form):
        for c in form[:][:2]:
            if c not in "qwertyuiopasdfghjklzxcvbnm0123456789._":
                return "Invalid characters.\nOnly alphanumeric characters, plus '.' and '_' are allowed."




        # Char reconstruction, to be added later
        # char_list = {'%20' : ' ',}
        #
        # for f in form:
        #     for c in char_list.keys():
        #         f.replace(c, char_list[c])



def run(server=HTTPServer, handler=AppHandler, port=2526):
    server_address = ('', port)
    httpd = server(server_address, handler)
    print "Started the HTTP Server at port", port
    httpd.serve_forever()


run()