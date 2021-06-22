from flask import Flask, jsonify

manager = Flask(__name__)


@manager.route('/test', methods=['GET'])
def test():
    response = {'test': 'hello world!'}
    return jsonify(response)




