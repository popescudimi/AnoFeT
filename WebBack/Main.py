import logging
import Cookie
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from DBController   import DBConnection
from os import curdir, sep, path


class AppHandler(BaseHTTPRequestHandler):

    db_conn = DBConnection.connect("PROJECT1", "project1", "localhost")

    def format_path(self):
        if self.path == "/":
            self.path = "/index.html"

        self.path =  "../WebFront" + self.path

        return path.splitext(self.path)



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



        fpath, ext =  self.format_path() # Splits the given string into the simple path and the extension of the final file(including the lading dot, ".html")
        if ext in content_type.keys():
            with open(self.path, 'rb') as f:
                self.send_response(200)
                self.send_header('Content-type', content_type[ext])
                self.end_headers()

                self.wfile.write(f.read())
        return

    def do_POST(self):
        print "POST"
        form = str(self.rfile.read(int(self.headers['Content-Length']))) # Read the message as a string

        if form.find("item") > 0:
            result = self.db_conn.execute("select title from items") # ce select vrei tu
            # acum result e o matrice bidimensionala. Daca ai result[row][cell], row va fi index al randului pe care il
            # vrei, iar cell va fi index-ul coloanei din tabel pe care o vrei. Ambii indecsi incep de la 0, nu de la 1
            # Ex. result[0][2] imi va lua primul rand, si a treia coloana. Daca le vrei ca str faci str(result[x][y])

        # for f in form.split('&'):
        #     f = [f[:f.find("=")], f[f.find("=")+1:]]
        #     print f




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