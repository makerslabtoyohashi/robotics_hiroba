from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse

def start(port, myfunc):
    """ start server
    Parameters
    ------
    port : str
    myfunc : method
    """
    def handler(*args):
        MyServer(myfunc, *args)
    server = HTTPServer(('', int(port)), handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:server.server_close()

class MyServer(SimpleHTTPRequestHandler):
    """ http server """
    def __init__(self, myfunc, *args):
        self.myfunc = myfunc
        SimpleHTTPRequestHandler.__init__(self, *args)

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _path_parser(self):
        parsed_path = urlparse(self.path)
        query = parsed_path.query
        return query

    def do_GET(self):
        data = self._path_parser()
        self._set_headers()
        message = self.myfunc(data)
        self.wfile.write(message.encode('utf-8'))
        return
