# lingam_tool
因果探索手法の1つであるLiNGAMを実行できるWebアプリ


+ 手法：DirectLiNGAM

+ ライブラリ：https://lingam.readthedocs.io/en/latest/

+ Webアプリフレームワーク:Streamlit


Streamlit SherでWebアプリも公開（ローカルで実行したい方は以下の構築手順にて）

https://ts5129nk-lingam-tool-app-vr9rur.streamlit.app/

## UI画面
<img src=image/tool_ui.png width='600px'>

## 結果イメージ
<img src=image/sample_result.png width='500px'>


## 構築手順
### 必要なもの
Dockerが実行できる環境
### 手順
本githubをローカルにcloneし、展開先フォルダに移動

以下を実行
~~~
docker build . -t lingam_img
docker run -it --rm -p 8501:8501 lingam_img streamlit run app.py
~~~

以下にアクセス

~~~
http://localhost:8501/
~~~
