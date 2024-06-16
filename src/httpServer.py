from http.server import HTTPServer, BaseHTTPRequestHandler, _url_collapse_path
from urllib import parse
import http.server
from mako.template import Template

from . import plotter

class Handler(BaseHTTPRequestHandler):
  def sanitize_path(self):
    collapsed_path = self.path
    if collapsed_path.endswith("/") and collapsed_path != "/":
      collapsed_path = collapsed_path[:-1]
    return collapsed_path

  def do_GET(self):
    path = self.sanitize_path()
    
    if path == "/":
      return self.do_Index()
    elif path.startswith("/img"):
      return self.do_Image(path)
    else:
      return self.do_Debug(path)

  def do_Index(self):
    plotter.plot()
    
    tmp = Template(filename='src/templates/index.pyhtml')
    
    self.send_response(200)
    self.send_header("content-type", "text/html")
    self.end_headers()
    self.wfile.write(tmp.render(param="test").encode())
  
  def do_Debug(self, msg):
    self.send_response(200)
    self.send_header("content-type", "text/html")
    self.end_headers()
    self.wfile.write(msg.encode())
    
  def do_Image(self, path):
    filepath = path.partition("/img/")[2]
    img = self.load_binary(filepath)
    
    self.send_response(200)
    self.send_header("content-type", "image/png")
    self.end_headers()
    self.wfile.write(img)

  def load_binary(self, filename):
    with open(filename, 'rb') as file_handle:
        return file_handle.read()


def run(port):
  server = HTTPServer(("", port), Handler)
  print(f"Server running on port {port}")
  server.serve_forever()
