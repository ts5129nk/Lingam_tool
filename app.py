import streamlit as st

from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import plotly.express as px

import graphviz
import lingam
from lingam.utils import make_dot,print_causal_directions, print_dagc,make_prior_knowledge

def read_sample_data():
  #住宅価格データセットの読み込み
  data_housing = fetch_california_housing()
  df = pd.DataFrame(data_housing.data, columns=data_housing.feature_names).assign(MidInc=np.array(data_housing.target))
  #正規化
  df=df.apply(lambda x: (x-x.mean())/x.std(), axis=0)
  return df
  

def lingam_f(data): 
  # numpyでの小数点以下桁数表示と指数表記の禁止を設定
  np.set_printoptions(precision=3, suppress=True)
  # 再現性のためにランダムシードを固定
  np.random.seed(0)
  #因果探索実行
  model = lingam.DirectLiNGAM()
  model.fit(data)
  return model,list(data.columns) #因果関係グラフとノード名（データカラム名）

st.title("hello")

data=None

st.write('分析データのアップロード')
upload_file=st.file_uploader('upload a csv file')
if upload_file is not None:
  data=pd.read_csv(upload_file)
  st.write(data.head())



#係数足切り下限値フォーム
input_limit = st.number_input('表示する係数の下限')
st.write('下限値は{}'.format(round(input_limit,3)))
#データ正規化の有無確認フォーム
on_norm =st.checkbox('データの正規化')



if st.button('実行'):
  if data is None:
    st.write('データが未読み込みの状態で実行されました。サンプルデータで実行します')
    data = read_sample_data()
  if on_norm:
    #正規化
    data=data.apply(lambda x: (x-x.mean())/x.std(), axis=0)
  #因果探索
  model, label=lingam_f(data)
  #因果グラフ表示
  dot=make_dot(model._adjacency_matrix,labels=label,lower_limit=input_limit) 
  st.graphviz_chart(dot)
  #係数のヒストグラム表示
  coeff_flat=[abs(x) for row in model._adjacency_matrix for x in row if x != 0]
  if on_norm:
    hist_fig = px.histogram(coeff_flat,nbins=30)
    st.plotly_chart(hist_fig)
else:
  st.write('NO..')



