# -*- coding:utf-8 -*- 
import SimpleHTTPServer
import SocketServer
import sys
import cgi
import json
import predict

PORT = 80

class DoodleHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

  def _set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    post_data = self.rfile.read(content_length)
    
    response = {
        'status':'SUCCESS',
        'data':'server got your post data'
    }
    self._set_headers()
    try:
      res = predict.get_prediction(post_data[6:])
      print('res=',res)
      results = {"status":'ok', "msg":res}
    except:
      results = {"status":'err', "msg":'暂不可用...'}
      print('error, post_data: ',post_data)
    self.wfile.write(json.dumps(results))

def run():
    httpd = SocketServer.TCPServer(("", PORT), DoodleHTTPHandler)
    print("serving at port", PORT)
    httpd.serve_forever()

if len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    
run()