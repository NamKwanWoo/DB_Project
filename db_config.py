host = "namdb.cyvpars8gmu4.ap-northeast-2.rds.amazonaws.com"
user = "NamDB"
pw = "skarhksdn1!"
dbname = "NamDB"


"""""
# 1.판매량 순 상품 정렬
SELECT P.*
		FROM Products as P JOIN Purchases as U
		WHERE	U.product_id = P.id
		ORDER by U.product_cnt DESC;


# 2.평가 순 상품 정렬
	SELECT *, rating_sum / rating_cnt as 'rating_percent'
		FROM	Products
		ORDER BY 'rating_percent' DESC;


# 3. 카테고리 별 상품 출력   (여기선 1번 카테고리 출력)
	SELECT A.* FROM Products as A JOIN Category as B
		WHERE B.ID = '1' AND B.ID = A.category
		ORDER BY id DESC;



# 4. 판매자 검색 상품 출력   Choi 이라는 판매자가 올린 상품 출력
	SELECT P.* FROM Products as P JOIN Users as U
    WHERE U.Name = 'Choi' AND P.seller_id = U.UserID
    ORDER BY id DESC ;


# 5. 상품 키워드 검색

SELECT * FROM Products
  WHERE product_name LIKE 'coat' ORDER BY id DESC ;

# 6.어떤 사용자가 소유한 쿠폰 리스트 출력 (kims 가 사용한 쿠폰)

SELECT * FROM couponlist
  WHERE couponlist.own_id = 'kims';


# 7. 나이, 성별 별 가장 많이 구매한 물품 출력

SELECT
  SUM(P.price + PO.add_price)
FROM
    ProductOptions as PO,
    Products as P,
    Wishlist as W,
    Users as U
WHERE
    U.Name = 'Choi' AND
      W.user_id = U.UserID AND
    (
      P.id = W.product_id AND
        PO.id = W.product_option_id
    )


# 8.사용자의 위시리스트 총 가격 출력 *집계*

SELECT SUM('price')
  FROM Purchases
  WHERE '2014-11-01' <= created AND created < '2014-12-01';

# 9. 일정 기간 내에 결제한 총 가격

SELECT
  P.*,
  count(*) as 'purchase_count'
FROM
  Purchases as U,
  Consumer as C,
  Products as P
WHERE
    C.Sex = 'WOMAN' AND
      U.consumer_id = C.UserID AND
      P.id = U.product_id
ORDER BY
  purchase_count DESC;

"""""
