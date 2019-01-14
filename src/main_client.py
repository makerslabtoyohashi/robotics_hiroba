import time
import datetime

""" original modules """
import MyClient

""" DEFINE """
ipaddress = '192.168.2.103'
page = '/getdata'
port = '1880'

if __name__=='__main__':
    client = MyClient.MyClient(ipaddress, port, page)
    #params = {'ontime':8, 'offtime':22}
    params = {}
    print('send:',params)
    client.send(params)
    time.sleep(1)
