import pymysql

actors = ['Andrew Adamson', 'William Addy', 'Seth Adkins']

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
        print(result)

    connection.commit()

finally:
    connection.close()

