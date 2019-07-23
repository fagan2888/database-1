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
        # Create a new record
        sql = "ALTER TABLE imdb.actors ADD num_of_movies int"
        cursor.execute(sql)

    connection.commit()

finally:
    connection.close()



