import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError


class MyClient:
    def __init__(self, ipaddress, port, clientname='noname'):
        self.ipaddress = ipaddress
        self.port = port
        self.clientname = clientname

    def _create_request(self, params, page):
        url = 'http://{}:{}'.format(self.ipaddress, self.port)
        if len(page) > 0:
            url = url + page
        req = Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        return req

    def send(self, params, page=''):
        req = self._create_request(params, page)
        body = None
        try:
            with urlopen(req, timeout=10) as res:
                body = res.read()
        except URLError as e:
            print('MyClient Err: {}'.format(self.clientname))
            if hasattr(e, 'reason'):
                print('We failed to reach a server')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
        return body


if __name__ == '__main__':
    client = MyClient('192.168.24.63', '1880')
    params = {}
    body = client.send(params, page='/getimg')
    with open('test.jpeg', 'wb') as f:
        f.write(body)
