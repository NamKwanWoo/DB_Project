import logging

import pymysql.cursors

import db_config as config

# Database Function
# 1. 판매자가 상품 등록
# 2. 구매자가 상품 평가
# 3. 구매자가 원하는 상품 (즐겨찾기) 등록
# 4. 구매자가 상품 배송정보 등록
# 5. 판매자가 상품 배송 방식 정하기
# 6. 구매자가 구매 상품 정보 보기

print("\nWelcome To Internet Shopping Web Site")
print("================ User Type ================")
print("1. Consumer  2. Seller")

select = input()

if select == "Consumer":
    print("\n\t[Consumer]")

    while True:
        print("1. Register Web site")
        print("2. Display all products")
        print("3. Add Bookmark")
        print("4. Register product comment")
        print("5. Exit")

        menu = int(input())

        if menu == 1:
            print("\n\t[Register User]")
            userID = input("User ID: ")
            passWord = input("Password: ")
            Name = input("Name: ")
            Email = input("E-mail: ")
            Phone_number = input("Phone-number: ")
            Address = input("Address: ")
            Birth = input("Birth Day: ")
            Sex = input("Sex: ")



            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "INSERT INTO Person (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address) VALUES (%s, %s, %s, %s, %s, %s) "
                    cursor.execute(sql,
                                   (str(userID), str(passWord), str(Name), str(Email), str(Phone_number), str(Address)))

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')

            except Exception as e:
                print(e)
                logging.error('connection failed')

        elif menu == 2:
            print("\nDisplay all products")
            print("You will able to purchase products")
            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "SELECT * FROM Online_Products"
                    cursor.execute(sql)
                    for row in cursor:
                        print(cursor.fetchone())

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')

        elif menu == 3:
            print("\nAdd Bookmark")
            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "SELECT * FROM Online_Products"
                    cursor.execute(sql)
                    print("\nSelect What you want to add\n")
                    for row in cursor:
                        print(cursor.fetchone())
                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')
        elif menu == 4:
            print("\nAdd comment")
            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    userID = input("User ID: ")
                    product = input("Product ID: ")
                    title = input("Product's title: ")
                    comment = input("Please type product comment: ")
                    rating = input("Rating 0~10: ")

                    sql = "INSERT INTO Consuemr_Online_Feedback (userID, product_id, title, comment, rating) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, str(userID), str(product), str(title), str(comment), str(rating))

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')
        elif menu == 5:
            break


elif select == "Seller":
    print("\n\t[Seller]")

    while True:
        print("1. Reister Seller ID")
        print("2. Upload Products")
        print("3. Display all products")
        print("4. Display all Users")
        print("5. Exit")

        menu = int(input())

        if menu == 1:
            print("\n\t[Register Seller]")

            userID = input("User ID: ")
            passWord = input("Password: ")
            Name = input("Name: ")
            Email = input("E-mail: ")
            Phone_number = input("Phone-number: ")
            Address = input("Address: ")
            companyID = input("Company ID: ")
            companyName = input("Company Name: ")

            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "INSERT INTO Person (NamDB.Person.UserID, NamDB.Person.Password, NamDB.Person.Name, NamDB.Person.Email, NamDB.Person.Phone, NamDB.Person.Address) VALUES (%s, %s, %s, %s, %s, %s) "
                    cursor.execute(sql,
                                   (str(userID), str(passWord), str(Name), str(Email), str(Phone_number), str(Address)))
                    sql = "INSERT INTO Person_Seller (UserID, CompanyID, CompanyName) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (str(userID), str(companyID), str(companyName)))

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')

        elif menu == 2:
            print("\nUpload Products\n")
            id = input("Product ID: ")
            sel_ID = input("Seller ID: ")
            category = input("Category: ")
            prd_Name = input("Product name: ")
            price = input("price: ")
            rating_Sum = input("rating sum: ")
            rating_CNT = input("rating cnt: ")
            use_Opt = input("Option?: ")

            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "INSERT INTO Online_Products (id, seller_id, category, product_name, price, rating_sum, rating_cnt, use_options) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) "
                    cursor.execute(sql,
                                   (str(id), str(sel_ID), str(category), str(prd_Name), str(price), str(rating_Sum),
                                    str(rating_CNT), str(use_Opt)))
                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')

        elif menu == 3:
            print("\nDisplay all products")
            print("You will able to purchase products")
            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "SELECT * FROM Online_Products"
                    cursor.execute(sql)
                    for row in cursor:
                        print(cursor.fetchone())

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')
        elif menu == 4:
            print("\nDisplay all Users")

            try:
                db = pymysql.connect(host=config.host,
                                     user=config.user,
                                     password=config.pw,
                                     db=config.dbname,
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)
                cursor = db.cursor()
                try:
                    sql = "SELECT * FROM Person"
                    cursor.execute(sql)
                    for row in cursor:
                        print(cursor.fetchone())

                    db.commit()
                    db.close()
                except Exception as e:
                    print(e)
                    logging.warning('commit failed')
            except Exception as e:
                print(e)
                logging.error('connection failed')
        elif menu == 5:
            break
