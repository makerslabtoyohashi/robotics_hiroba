# マザープログラム
import datetime
import argparse
from MyClient import MyClient
import time
import os

# THIS CODE IS
# データ要求・データ受け取り・保存を自動で行う。


def get_args():
    parser = argparse.ArgumentParser(description='Mother')
    parser.add_argument('--delay', type=int, default=15, help='second')
    parser.add_argument('--ip_sensor', type=str, default='192.168.24.62', help='IP address for Sensor raspberry pi')
    parser.add_argument('--ip_camera2', type=str, default='192.168.24.63', help='IP address for Camera2 raspberry pi')
    parser.add_argument('--ip_camera1', type=str, default='192.168.24.65', help='IP address for camera1 raspberry pi')
    parser.add_argument('--port', type=str, default='1880', help='Port for node-red of raspberry pi')
    parser.add_argument('--outf_sensor', type=str, default='../data/data_sensor.json', help='Output file of sensor data')
    parser.add_argument('--inf_takenphoto1', type=str, default='../data/list_takenphoto1.txt', help='Input file of name list of taken photo file on raspberry pi')
    parser.add_argument('--inf_takenphoto2', type=str, default='../data/list_takenphoto2.txt', help='Input file of name list of taken photo file on raspberry pi')
    parser.add_argument('--outf_savedphoto', type=str, default='../data/list_savedphoto.txt', help='Input file of name list of saved photo file')
    parser.add_argument('--outdir_photo', type=str, default='../data/photo/', help='Output directory of photo file')
    parser.add_argument('--outdir_photo1', type=str, default='../data/photo1/', help='Output directory of photo file on raspberry pi')
    parser.add_argument('--outdir_photo2', type=str, default='../data/photo2/', help='Output directory of photo file on raspberry pi')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()


def save_sensor(outf, client):
    """
    Parameters
    ----------
    outf : str
    client : MyClient
    """
    # センサ値
    data_sensor = client.send({}, page='/getdata')
    with open(outf, 'a') as f:
        f.write(data_sensor)


def load(filename):
    with open(filename, 'r') as f:
        lines = f.read().split('\n')[:-1]
    return lines


def save_camera(inf, outf, outdir, client, page='getimg'):
    # 新たに撮影された画像ファイル名一覧
    with open(inf, 'r') as f:
        filenames = f.read().split('\n')[:-1]
    for filename in filenames:
        img = client.send({'name': filename}, page)
        filename = outdir + os.path.basename(filename)
        with open(filename, 'wb') as f:
            f.write(img)
        with open(outf, 'a') as f:
            f.write(filename + '\n')
        os.remove(inf)


if __name__ == '__main__':
    args = get_args()
    dt_before = datetime.datetime.now()
    sensor = MyClient('localhost', args.port)
    camera1 = MyClient('localhost', args.port)
    camera2 = MyClient('localhost', args.port)
    if True:
        dt_now = datetime.datetime.now()
        # delta = dt_now - dt_before
        # if delta.total_seconds() > args.delay_photo1:
        if True:
            dt_now_str = dt_now.strftime('%Y%m%d%H%M%S')
            filename = '{}camera1_{}.jpeg'.format(args.outdir_photo1, dt_now_str)
            camera1.send({'name': filename}, '/shutter1')
            if args.debug:
                with open(filename, 'w') as f:
                    f.write('test')
            with open(args.inf_takenphoto1, 'a') as f:
                f.write(filename + '\n')
            filename = '{}camera2_{}.jpeg'.format(args.outdir_photo2, dt_now_str)
            camera2.send({'name': filename}, '/shutter2')
            if args.debug:
                with open(filename, 'w') as f:
                    f.write('test')
            with open(args.inf_takenphoto2, 'a') as f:
                f.write(filename + '\n')
            dt_before = dt_now
        save_sensor(args.outf_sensor, sensor)
        save_camera(args.inf_takenphoto1,
                    args.outf_savedphoto,
                    args.outdir_photo,
                    camera1,
                    'getimg1')
        save_camera(args.inf_takenphoto2,
                    args.outf_savedphoto,
                    args.outdir_photo,
                    camera2,
                    'getimg2')
        time.sleep(args.delay)
