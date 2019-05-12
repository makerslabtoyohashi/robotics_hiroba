import urllib.request


class MyClient:
    def __init__(self, ipaddress, port):
        self.ipaddress = ipaddress
        self.port = port

    def _create_request(self, params, page):
        url = 'http://{}:{}'.format(self.ipaddress, self.port)
        if len(page) > 0:
            url = url + page
        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        return req

    def send(self, params, page=''):
        req = self._create_request(params, page)
        body = None
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return body


if __name__ == '__main__':
    client = MyClient('192.168.24.63', '1880')
    params = {}
    body = client.send(params, page='/getimg')
    with open('test.jpeg', 'wb') as f:
        f.write(body)
