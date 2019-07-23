import pymysql

# actors = ['Andrew Adamson', 'William Addy', 'Seth Adkins']

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
        sql = "INSERT INTO `actors` (`id`, `full_name`, `gender`) VALUES (24, 'gilad benatiya', 'M')"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "select * from actors"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()