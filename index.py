from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>������ ����������� �����</h1>'


@app.route('/index')
def new_page():
    return '<h2>� �� ����� ����� ������ ������!</h2>'


@app.route('/promotion')
def promotion_page():
    return '''<b>������������ ��������� �� �������.<br>
    ������������ ���� ���� �������.<br>
    �� ������� ���������� ������������ ���� �������.<br>
    � ������ � �����!<br>
    �������������!</b>'''

@app.route('/image_mars')
def image_mars():
    return f'''<h1>��� ���, ����!</h1>
    <title>������, ����!</title>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="����� ������ ���� ���� ��������, �� �� �������">
           <p>��� ��� �����, ������� �������.</p>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')