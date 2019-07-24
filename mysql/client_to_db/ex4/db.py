# Connect to the database
import pymysql

def connect_2_db():
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
        return result