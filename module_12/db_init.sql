
CREATE DATABASE whatabook;

DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

USE whatabook; 


ALTER TABLE wishlists DROP FOREIGN KEY fk_books;
ALTER TABLE wishlists DROP FOREIGN KEY fk_users;

DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS wishlists;
DROP TABLE IF EXISTS users;


CREATE TABLE stores (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE books (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    author      VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE users (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlists (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_books
    FOREIGN KEY (book_id)
        REFERENCES books(book_id),
    CONSTRAINT fk_users
    FOREIGN KEY (user_id)
        REFERENCES users(user_Id)
);


INSERT INTO stores(locale)
    VALUES('4 Privet Drive,bellevue,NE,68005');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Philosopher''s Stone', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Chamber of Secrets', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Prisoner of Azkaban', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Goblet of Fire', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Order of Phoenix', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Half-Blood Prince', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Deathly Hallows: Part 1','J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Harry Potter', 'The Deathly Hallows: Part 2', 'J.K. Rowling');

INSERT INTO books(book_name, details, author)
    VALUES('Fantastic Beasts','The Crimes of Grindelwald', 'J.K. Rowling');



INSERT INTO users(first_name, last_name) 
    VALUES('Peter', 'Pan');

INSERT INTO users(first_name, last_name)
    VALUES('Mary', 'May');

INSERT INTO users(first_name, last_name)
    VALUES('Santa', 'Claus');

