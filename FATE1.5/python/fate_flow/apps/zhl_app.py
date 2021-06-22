from flask import Flask, jsonify, request, redirect
from werkzeug.routing import BaseConverter

manager = Flask(__name__)


class MobileConverter(BaseConverter):
    regx = r'1[3-9]\d{9}'


manager.url_map.converters['mobile'] = MobileConverter


@manager.route('/zhl', methods=['GET'])
def test1():
    response = {'zhl': 'hello world!'}
    return jsonify(response)


@manager.route('/zhl/<id>', methods=['GET'])
def get_userid(id):
    return 'get users {}'.format(id)


@manager.route('/tag/list/<int:page>/', methods=['POST'])
def tag_list(page):
    return 'get list{}'.format(page)


@manager.route('/sms_codes/<mobile:mob_num>/', methods=['post'])
def send_sms_code(mob_num):
    return 'send sms code'.format(mob_num)


# /articles?channel_id123  args查询请求参数
@manager.route('/article', methods=['post'])
def get_articles():
    channel_id = request.args.get('channel_id')
    return 'you want get articles of channel'.format(channel_id)


# pic与前端发送的的文件名是一致的
@manager.route('/upload', methods=['post'])
def upload_file():
    f = request.files.['pic']
    # with open('./app/demo.png', 'wb')as new_file:
    #     new_file.write(f.read)
    f.save('./demo.png')
    return 'ok'


@manager.route('/test2')
def test2():
    return redirect('http:www.baidu.com')


@manager.route('/test3')
def test3():
    json_dict = {
        "user_id": 10,
        "user_name": "zhanghonglei"
    }
    return jsonify(json_dict)

