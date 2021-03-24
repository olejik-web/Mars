from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def new_page():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion')
def promotion_page():
    return '''<b>Человечество вырастает из детства.<br>
    Человечеству мала одна планета.<br>
    Мы сделаем обитаемыми безжизненные пока планеты.<br>
    И начнем с Марса!<br>
    Присоединяйся!</b>'''

@app.route('/image_mars')
def image_mars():
    return f'''<h1>Жди нас, Марс!</h1>
    <title>Привет, Марс!</title>
    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
           <p>Вот она какая, красная планета.</p>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')