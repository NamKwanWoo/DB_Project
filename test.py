import logging
import pymysql.cursors
import db_config as config

ID = 123
idx = 0

print ("Welcome To Internet Shopping Web Site")

while idx < 10:
    idx += 1
    try:
        db = pymysql.connect(host=config.host, user=config.user, password=config.pw, db=config.dbname, charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        try:
            ID += idx
            #sql = "INSERT INTO Test (ID) VALUES (%s)"
            sql = ('select ID '
                   'From Test')
            cursor.execute(sql)
            db.commit()
            db.close()
        except Exception as e:
            print(e)
            logging.warning('commit failed')
    except Exception as e:
        print(e)
        logging.error('connection failed')
