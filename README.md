## 说明

使用 hanlp-python 与 cx_extractor-python 作为底层支持，使用 flask 开发 api 接口

## Usage

1、查看 hanlp 目录中的 README.md，安装相关依赖

2、安装 flask

```
pip3 install flask
```

3、运行
```
python3 server.py
```

GET http://localhost:5000/getEntityFromContent?content=${your_content}