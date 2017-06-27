CREATE TABLE Person (
  UserID   VARCHAR(40)  NOT NULL,
  Password VARCHAR(100) NOT NULL,
  Name     VARCHAR(100) NOT NULL,
  Email    VARCHAR(100) NULL,
  Phone    VARCHAR(100) NOT NULL,
  Address  VARCHAR(150) NOT NULL,

  PRIMARY KEY (UserID)
);

CREATE TABLE Person_Seller (
  UserID      VARCHAR(40)  NOT NULL,
  CompanyID   VARCHAR(150) NOT NULL,
  CompanyName VARCHAR(100) NOT NULL,

  PRIMARY KEY (UserID),
  FOREIGN KEY Person_Seller(UserID) REFERENCES Person (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE Person_Consumer (
  UserID VARCHAR(40) NOT NULL,
  Birth  DATE        NULL,
  Sex    VARCHAR(5)  NOT NULL
    CHECK (VALUE IN ('MAN', 'WOMAN')),

  PRIMARY KEY (UserID),
  FOREIGN KEY (UserID)
  REFERENCES Person (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE Only_for_Online_Coupon (
  ID          INT(20)    NOT NULL,
  ValidTerm   INTEGER(2) NOT NULL,
  SalePercent INTEGER(2) NOT NULL,

  PRIMARY KEY (ID)
);

CREATE TABLE List_of_Online_Coupon (
  id        INT(60)     NOT NULL AUTO_INCREMENT,
  own_id    VARCHAR(40) NOT NULL,
  coupon_id INT(20),
  PRIMARY KEY (id),
  FOREIGN KEY (own_id)
  REFERENCES Person_Consumer (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (coupon_id)
  REFERENCES Only_for_Online_Coupon (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE Category_of_Products (
  ID    INT(60)     NOT NULL AUTO_INCREMENT,
  title VARCHAR(40) NOT NULL
    CHECK (VALUE IN (
      'fashion/beauty',
      'kids/grocery',
      'living/health',
      'computer/digital',
      'culture/travel/e-coupon',
      'sports/car/hobby')),

  PRIMARY KEY (ID)
);

CREATE TABLE Online_Products (
  id           INT(60)      NOT NULL AUTO_INCREMENT,
  seller_id    VARCHAR(40)  NOT NULL,
  category     INT(50)      NOT NULL,
  product_name VARCHAR(120) NOT NULL DEFAULT ' ',
  price        INT(100)     NOT NULL,
  rating_sum   INT(100)     NOT NULL DEFAULT '0',
  rating_cnt   INT(40)      NOT NULL DEFAULT '0',
  use_options  INT(1)       NOT NULL DEFAULT '0',

  PRIMARY KEY (id),
  FOREIGN KEY (seller_id) REFERENCES Person_Seller (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (category) REFERENCES Category_of_Products (ID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE Option_of_Products (
  id         INT(60)      NOT NULL AUTO_INCREMENT,
  product_id INT(60)      NOT NULL,
  title      VARCHAR(120) NOT NULL DEFAULT ' ',
  add_price  INT(100)     NOT NULL DEFAULT '0',

  PRIMARY KEY (id),

  FOREIGN KEY (product_id) REFERENCES Online_Products (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE Cousumer_Online_Feedback (
  user_id    VARCHAR(40)  NOT NULL,
  product_id INT(60)      NOT NULL,
  title      VARCHAR(120) NOT NULL DEFAULT ' ',
  content    TEXT         NOT NULL,
  rating     INT(100)     NOT NULL DEFAULT '0',

  PRIMARY KEY (user_id, product_id),
  FOREIGN KEY (user_id) REFERENCES Person (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (product_id) REFERENCES Online_Products (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE List_of_Online_Products_Consumer_Wants (
  id                INT(60)     NOT NULL AUTO_INCREMENT,
  user_id           VARCHAR(40) NOT NULL,
  product_id        INT(60)     NOT NULL,
  product_option_id INT(60)     NULL,
  number            INT(5)      NOT NULL DEFAULT '1',

  PRIMARY KEY (id),

  FOREIGN KEY (user_id) REFERENCES Person_Consumer (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (product_id) REFERENCES Online_Products (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (product_option_id) REFERENCES Option_of_Products (id)
    ON DELETE SET NULL
    ON UPDATE RESTRICT
);

CREATE TABLE Thd_Kind_of_Delivery_Service (
  id            INT(60)      NOT NULL AUTO_INCREMENT,
  type_name     VARCHAR(100) NOT NULL
    CHECK (VALUE IN ('PRE', 'POST', 'INTERNATIONAL')),
  price         INT(60)      NOT NULL DEFAULT '3000',
  delivery_time INT(60)      NOT NULL DEFAULT '0',

  PRIMARY KEY (id)
);

CREATE TABLE List_of_Purchases (
  id                INT(60)     NOT NULL AUTO_INCREMENT,
  consumer_id       VARCHAR(60) NOT NULL,
  product_id        INT(60)     NOT NULL,
  product_option_id INT(60)     NULL,
  product_cnt       INT(40)     NOT NULL,
  purchase_type     VARCHAR(10) NOT NULL
    CHECK (VALUE IN ('CARD', 'CASH', 'MOBILE')),
  price             INT(100)    NOT NULL DEFAULT '0',
  created           DATETIME    NOT NULL DEFAULT '0000-00-00 00:00:00',

  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES Online_Products (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (product_option_id) REFERENCES Option_of_Products (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (consumer_id) REFERENCES Person (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);

CREATE TABLE DeliveryService (
  PurchaseNum  INT(60)     NOT NULL,
  Address      VARCHAR(100),
  Consumer     VARCHAR(40) NOT NULL,
  Recipient    VARCHAR(40) NOT NULL,
  DeliveryType INT(60)     NOT NULL AUTO_INCREMENT,

  PRIMARY KEY (PurchaseNum),

  FOREIGN KEY (PurchaseNum)
  REFERENCES List_of_Purchases (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (Consumer)
  REFERENCES Person (UserID)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  FOREIGN KEY (DeliveryType)
  REFERENCES Thd_Kind_of_Delivery_Service (id)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT
);




