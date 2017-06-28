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

print("Welcome To Internet Shopping Web Site\n\n")
print("================ Select ================")
print("1. Consumer  2. Seller")

select = input()
print(select)

if select :
    print("\n\n ")
    print("[Consumer]")
    while True:
        print("1. Register Web site")
        print("2. Display all products")
        print("3. Add Bookmark")
        print("4. Register product comment")
        print("5. Exit")
        menu = input()
        if(menu == 5):
            break

        try:
            db = pymysql.connect(host=config.host,
                                 user=config.user,
                                 password=config.pw,
                                 db=config.dbname,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
            cursor = db.cursor()
            try:
                # sql = "INSERT INTO Test (ID) VALUES (%s)"
                # sql = ('select ID ''From Test')
                # cursor.execute(sql)
                db.commit()
                db.close()
            except Exception as e:
                print(e)
                logging.warning('commit failed')
        except Exception as e:
            print(e)
            logging.error('connection failed')

elif select == 2:
    print("\n\n ")
    print("[Seller]")

    while True:
        print("1. Display all products")
        print("2. Upload Products")
        print("3. Register product comment")
        print("4. Exit")

        menu = input()

        if (menu == 4):
            break
