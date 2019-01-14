# robotics_hiroba

## Node-Red files
### LEDendpoint
#### abstract
http endpointです。

http GETでLEDの点灯消灯時刻の設定を受け取る

#### flow
1. http GET requestを受け取り、パラメタから点灯時刻と消灯時刻の設定を受け取ります。`req.quey.ontime`と`req.query.offtime`で参照。  
typical request: `http://IPaddress:1880/setled?ontime=XXXX&offtime=XXXX`
1. responseを作成します。※LEDendpointは送るべき情報を持っていませんが、確認のため受け取った設定をそのまま返信。
1. http responseを返します。

- 受け取ったパラメタの内容はdebugで表示しています。



### SENSORendpoint
#### abstract
http endpointです。

http GETでセンサ値の要求を受け、センサ値を返す

#### flow
1. http GET requestを受け取ります。  
typical request: `http://IPaddress:1880/getdata'
1. responseを作成します。ここに、各種センサで取得した値が乗るようにします。
1. http responseを返します。

- 受け取ったパラメタの内容はdebugで表示しています。

### CAMERAendpoint
#### abstract
http endpointです。

http GETで画像の要求を受け、センサ値を返す

#### flow
1. http GET requestを受け取ります。  
typical request: `http://IPaddress:1880/getimg'
1. responseを作成します。ここに、画像データが乗るようにします。
1. http responseを返します。

- 受け取ったパラメタの内容はdebugで表示しています。
