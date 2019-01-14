import urllib.request

class MyClient:
    def __init__(self, ipaddress, port, page = ''):
        self.ipaddress = ipaddress
        self.page = page
        self.port = port
    def _create_request(self, params):
        url = 'http://{}:{}'.format(self.ipaddress, self.port)
        if len(self.page)>0:
            url = url + self.page
        req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
        return req
    def send(self, params):
        req = self._create_request(params)
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print('recv :', body)

#if __name__=='__main__':
#    client = MyClient('192.168.2.103', '12345')
#    params = {'foo':'123'}
#    client.send(params)
