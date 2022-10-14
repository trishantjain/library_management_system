# ****** ____FUNCTION TO INSERT BOOK IN DATABASE____ ******
def insert_into_database(book, no):
    try:
        import mysql.connector

        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sample'
        )

        mydb = con.cursor()
        mydb_insert_query = "insert into booktable(bookname, noofbooks) values(%s, %s)"
        mydb_values = (book, no)
        mydb.execute(mydb_insert_query, mydb_values)
        con.commit()

    except Exception as e:
        print(f"There is error in connecting to database: {e}")


# ****** ____FUNCTION TO GET BOOK LIST____ ******
def get_book_list():
    try:
        import mysql.connector

        con2 = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sample'
        )

        mydb = con2.cursor()
        mydb.execute("select * from booktable;")
        booklist = mydb.fetchall()
        con2.commit()
        return booklist

    except Exception as e:
        print(f"There is error in connecting to database: {e}")

# **** INSERT USERNAME & PASSWORD INTO TABLE ****


def insert_credentials(user, pas, mail, mobile):
    import mysql.connector

    con3 = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sample'
    )

    mydb = con3.cursor()
    insert_query_credentials = "insert into credentials(username, password, email, phone_no) values(%s, %s, %s, %s);"
    value_credentials = (user, pas, mail, mobile)
    mydb.execute(insert_query_credentials, value_credentials)
    con3.commit()


# **** GET LIST OF USERNAME & PASSWORD FROM TABLE ****


def check_credentials(user, pas):
    import mysql.connector

    con4 = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sample'
    )

    mydb = con4.cursor()
    mydb.execute("select * from credentials")

    cred = mydb.fetchall()

    new_cred = []
    for i in cred:
        new_cred.append(i[0:2])

    for j in new_cred:
        if (j[0] == user and j[1] == pas):
            var = 1
            break
        else:
            var = 0

    con4.commit()
    return var


def add_book_cred(book, us, pas):
    import mysql.connector

    con5 = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sample'
    )

    mydb = con5.cursor(buffered=True)
    mydb.execute("select * from credentials")
    mysql_insert_query = "update credentials set bookname = %s where username=%s and password = %s"
    mysql_value = (book, us, pas)
    mydb.execute(mysql_insert_query, mysql_value)
    con5.commit()


def add_cred(obj):
    import mysql.connector

    con5 = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sample'
    )

    mydb = con5.cursor()
    insert_query_credentials = "insert into credentials(username, password, email, phone_no, bookname, nobooks) values(%s, %s, %s, %s, %s, %s);"
    insert_values = ("tri", 'ald#22', 'sldfj@gmail.com', '8178513030', obj, 3)
    mydb.execute(insert_query_credentials, insert_values)
    con5.commit()


if __name__ == '__main__':
    # insert_into_database('C', 1)
    # print(get_book_list())
    # insert_credentials('trishant', 'jain*33', 'trishantjain4444@gmail.com', 7982757222)
    # check_credentials('trishant', 'jain*33')
    # book1 = Book()
    # k = book1.add_list()
    # add_cred(k)
    add_book_cred('python', 'tushant', 'asd*ee')

    pass
