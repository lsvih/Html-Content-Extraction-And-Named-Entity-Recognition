from flask import Flask,request
import sys
import os
sys.path.append('./hanlp')


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

entityTags = ['an','Mg']

app = Flask(__name__)


@app.route('/getEntityFromContent')
def hello():
    c = request.args.get('content')
    x = nlpTool.segment(c, params)['response']
    return str(filter(x))




def filter(list):
    rs = []
    for i in list:
        word = i.split('/')[0]
        tag = i.split('/')[1]
        if i.split('/')[1] in entityTags or tag[0] == 'n' or tag[0] == 'g':
            if len(word) > 1 and tag != 'n':
                if word not in rs:rs.append(word)
    return rs

app.run()