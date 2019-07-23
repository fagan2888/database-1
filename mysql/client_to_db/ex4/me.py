from bottle import route, run, static_file, error, get, template, jinja2_view
from jinja2 import Template
import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='19371937',
                             db='imdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "select * from actors"
        cursor.execute(sql)

        result = cursor.fetchall()


    connection.commit()

finally:
    connection.close()


@route('/')
def index():
    return "Hello gilad"


@route('/about')
@jinja2_view('about.html', template_lookup=['templates'])
def index():
    return {'name': "shmulik",
            'dog_img': "https://www.akc.org/wp-content/themes/akc/component-library/assets/img/welcome.jpg",
            "tricks": ["קפיצה בחבל", "תפיסת חתולים", "האכלת כלבים אחרים"], "is_cute": True}

@route('/go')
@jinja2_view('go.html', template_lookup=['templates'])
def index():
    return {'go': result ,"is_cute": True }


@error(404)
def error404(error):
    return static_file("404.html", root="")


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


run(host='localhost', port=5500, debug=True, reloader=True)
