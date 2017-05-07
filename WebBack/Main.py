import logging
import mimetypes
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from DBController   import DBConnection
from os import curdir, sep, path
from random import randint
#Cookie (lib)
#Cookie=Cookie.Simple=Cookie(.self.headers["Cookies"])
#vezi documentatie base hhtp server
#for c_in headers:
#send_header("set.cookie.p")..
#js -ajax -> //cauta
#jason dump
#response.header=["set-cookie"]="s_id"=1234";
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
        print recived
        if 'UsernameBox' in recived:
            form = recived.split('&')
            for f in form:
              f = [f[:f.find("=")], f[f.find("=")+1:]]

              print f[1]
        else:
            t=randint(0,9000);

            self.send_response(200)
            self.send_header("content-type","text/html")
            self.end_headers()
            self.wfile.write("An Item!"+"Here is a Random Generated Code YeaH!"+str(t))
            return



def run(server=HTTPServer, handler=AppHandler, port=2526):
    server_address = ('', port)
    httpd = server(server_address, handler)
    print "Started the HTTP Server at port", port
    httpd.serve_forever()

run()