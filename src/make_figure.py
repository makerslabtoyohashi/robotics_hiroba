import plotly.offline as offline
import plotly.graph_objs as go
import numpy as np
import json
import os
import argparse


###############################################################################
# THIS CODE IS
# plotlyを用いてセンサデータをグラフ化し、htmlファイルにして出力する
###############################################################################


def get_args():
    parser = argparse.ArgumentParser(description='データの図化')
    parser.add_argument('--inf', type=str, default='../data/data_sensor.json',
                        help='センサデータのjsonファイル')
    parser.add_argument('--outf', type=str, default='../data/fig_sensor.html',
                        help='センサデータを可視化した図のhtmlファイル')
    return parser.parse_args()


def load(filename):
    """
    JSON形式のファイルを読み込む

    Returns
    -------
    data : numpy.array of float
        センサ数 x データ点数
    dtime : numpy.array of str
        長さ=データ点数
    header : numpy.array of str
        長さ=センサ数
    """
    data = None
    dtime = None
    header = None
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        dtime = [x for x in data.keys()]
        data = [data[x] for x in dtime]
        header = list(data[0].keys())
        data = [[float(d[h]) for d in data] for h in header]
        data = np.array(data)
        dtime = np.array(dtime)
    return data, dtime, header


def make_lineplot(data, dtime, header):
    """
    Parameters
    ----------
    data : numpy.array of float
        データの種類数 x 時系列での点数
    dtime : numpy.array of str
    header : list of str
    """
    traces = [go.Scatter(x=dtime,
                         y=y,
                         mode='lines+markers',
                         name=h) for y, h in zip(data, header)]
    layout = go.Layout(title='センサデータ',
                       xaxis=dict(title='計測時間(年/月/日/時/分/秒)'),
                       yaxis=dict(title='計測値'),
                       showlegend=True)
    fig = dict(data=traces, layout=layout)
    return fig


def output_figure_html(inf, outf):
    # load json
    data, dtime, header = load(inf)
    if data is not None:
        # make graph
        fig = make_lineplot(data, dtime, header)
        # make html file
        offline.plot(fig, filename=outf, auto_open=False)


if __name__ == '__main__':
    args = get_args()
    output_figure_html(args.inf, args.outf)
