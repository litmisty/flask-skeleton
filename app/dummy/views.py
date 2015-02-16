from app.parser.rss_parser import Parser
from flask import Blueprint, render_template, request
import json
import logging


dummy = Blueprint('dummy', __name__, url_prefix='/dummy')


@dummy.route('')
def index():
    """
    This is template example
    :return:
    """
    ctx = {'value': 'This is test value'}
    logging.info("this is test message")
    return render_template('index.html', **ctx)


@dummy.route("test")
def test():
    return Parser.test_method()


@dummy.route("json_test", methods=['GET', 'POST'])
def json_test():
    if request.method == 'GET':
        return json.dumps({'key': 'value'})

    elif request.method == 'POST':
        return request.get_data()