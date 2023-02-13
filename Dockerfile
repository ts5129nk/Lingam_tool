# pythonの3.8.0をベースにする
FROM python:3.9.13-slim-buster

RUN apt-get update \
    # imageのサイズを小さくするためにキャッシュ削除
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    # pipのアップデート
    && pip install --upgrade pip

#アプリケーション（ホストに直接マウントして開発するときはコメントアウトする）
COPY app.py /home/ 
#pythonライブラリ
COPY requirements.txt ${PWD}


# pythonのパッケージをインストール
RUN pip install -r requirements.txt

WORKDIR /home/
