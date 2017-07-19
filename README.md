## 说明

使用 hanlp-python 与 cx_extractor-python 作为底层支持，使用 flask 开发 api 接口

## Usage
1、检出子模块
```
git clone https://github.com/lsvih/Html-Content-Extraction-And-Named-Entity-Recognition.git

cd Html-Content-Extraction-And-Named-Entity-Recognition

git submodule init

git submodule update
```

2、查看 hanlp 目录中的 README.md，安装相关依赖

3、安装 flask 与 flask_cors

```
pip3 install flask

pip3 install flask_cors
```

3、运行
```
python3 server.py
```

## API

GET http://localhost:${your_port}/analysis?url=${url}   #获取指定网页实体

GET http://localhost:${your_port}/getContent?url=${url}  #获取指定网页正文内容

GET http://localhost:${your_port}/getEntityFromContent?content=${content}   #分析文本中实体
