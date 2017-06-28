import logging

import pymysql.cursors

import db_config as config

#f = open("/Users/namnamnam/Desktop/person_List.txt", 'w')

col1_f = open("/Users/namnamnam/Desktop/seller_id.txt", 'r')
col2_f = open("/Users/namnamnam/Desktop/seller_companyname.txt", 'r')
col3_f = open("/Users/namnamnam/Desktop/seller_companyID.txt", 'r')




while True:

    col1 = col1_f.readline()
    col2 = col2_f.readline()
    col3 = col3_f.readline()

    if not col1: break

    try:
        db = pymysql.connect(host=config.host,
                             user=config.user,
                             password=config.pw,
                             db=config.dbname,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        try:
            sql = "INSERT INTO Person_Seller (UserID, CompanyID, CompanyName) VALUES (%s, %s, %s) "
            cursor.execute(sql,
                           (str(col1), str(col2), str(col3)) )

            db.commit()
            db.close()
        except Exception as e:
            print(e)
            logging.warning('commit failed')
    except Exception as e:
        print(e)
        logging.error('connection failed')

    #addr_line = addr_list.readline()


#    data = "INSERT INTO  (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address)\n"
#    f.write(data)
#    data = "VALUES ('%s', '%s', '%s', '%s', '%s', '%s');\n\n" % (id_line , pw_line , name_line ,email_line , ph_line , addr_line)
#    f.write(data)

#f.close()
