from flask import Flask, request
import sys
import os
sys.path.append('./hanlp')

from cx import cx_extractor_Python
from flask_cors import CORS


# current_path = os.path.dirname(__file__)
# module_path = os.path.join(current_path, 'hanlp')
# sys.path.append(module_path)        # 导入的绝对路径
# mod = __import__('NLPTool', globals(), locals())

# from hanlp import NLPTool
import hanlp

nlpTool = hanlp.NLPTool()
params = {
    'enableCustomDic': True,
    'enablePOSTagging': True
}

entityTags = ['an', 'Mg']

app = Flask(__name__)
CORS(app)

cx = cx_extractor_Python()


@app.route('/getEntityFromContent')
def entity():
    return getEntity(request.args.get('content'))


def getEntity(content):
    x = nlpTool.segment(content, params)['response']
    return ','.join(filter(x))


def filter(list):
    rs = []
    for i in list:
        word = i.split('/')[0]
        tag = i.split('/')[1]
        if len(tag) is not 0:
            if tag in entityTags or tag[0] == 'n' or tag[0] == 'g':
                if len(word) > 1 and tag != 'n':
                    if word not in rs:
                        rs.append(word)
    return rs


@app.route('/getContent')
def content():
    return getContent(request.args.get('url'))


def getContent(url):
    html = cx.getHtml(url)
    content = cx.filter_tags(html)
    s = cx.getText(content)
    return str(s)


@app.route('/analysis')
def default():
    c = request.args.get('url')
    return getEntity(getContent(c))


app.run(port='10087',threaded=True)
