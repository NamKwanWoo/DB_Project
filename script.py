import logging

import pymysql.cursors

import db_config as config

#f = open("/Users/namnamnam/Desktop/person_List.txt", 'w')


col1_f = open("/Users/namnamnam/Desktop/seller_companyname.txt", 'r')
col2_f = open("/Users/namnamnam/Desktop/seller_id.txt", 'r')
col3_f = open("/Users/namnamnam/Desktop/product_ID.txt", 'r')
col4_f = open("/Users/namnamnam/Desktop/product_name.txt", 'r')
col5_f = open("/Users/namnamnam/Desktop/product_price.txt", 'r')
col6_f = 100
col7_f = 1
col8_f = 1




while True:

    col1 = col1_f.readline()
    col2 = col2_f.readline()
    col3 = col3_f.readline()
    col4 = col4_f.readline()
    col5 = col5_f.readline()
    col6 = col6_f
    col7 = col7_f
    col8 = col8_f

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
            sql = "INSERT INTO Online_Products (seller_id, category, product_name, price, rating_sum, rating_cnt, use_options) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
            cursor.execute(sql,
                           (str(col2), str(col3), str(col4), str(col5), str(col6), str(col7), str(col8)) )

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
