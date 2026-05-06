1-sudo service mariadb start   
2-sudo -i      (as root)
3-mysql -u root  
4-CREATE DATABASE practice;  
5-USE practice;      
6-CREATE TABLE books( id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), year
 INT);      
7-MariaDB [practice]> CREATE TABLE loans( id INT AUTO_INCREMENT PRIMARY KEY,book_id INT, borrower VARCHAR(255),loan_date DATE, FOREIGN KEY (book_id) REFERENCES books(id));    انشاء جدول اللانز
8-MariaDB [practice]> INSERT INTO books (title, author, year) VALUES ('the great gatsby', 'f. scott fitzgeraled'
, 1925), ('1984', 'george orwell', 1949), ('the hobbit','j.r.r tolkien',1937), ('clean code','robert c.martin'
,2008),('refactoring','martin fowler',1999);  
9- MariaDB [practice]> INSERT INTO loans (book_id, borrower, loan_date) VALUES (1, 'mahmoud','2026-05-06'), (4, 'ahmed','2026-05-05'), (2,'sara','2026-05-04');
10-MariaDB [practice]> SELECT * FROM books;
+----+------------------+----------------------+------+
| id | title            | author               | year |
+----+------------------+----------------------+------+
|  1 | the great gatsby | f. scott fitzgeraled | 1925 |
|  2 | 1984             | george orwell        | 1949 |
|  3 | the hobbit       | j.r.r tolkien        | 1937 |
|  4 | clean code       | robert c.martin      | 2008 |
|  5 | refactoring      | martin fowler        | 1999 |
+----+------------------+----------------------+------+
5 rows in set (0.006 sec)

11-MariaDB [practice]> SELECT * FROM books WHERE year > 2000;
+----+------------+-----------------+------+
| id | title      | author          | year |
+----+------------+-----------------+------+
|  4 | clean code | robert c.martin | 2008 |
+----+------------+-----------------+------+
1 row in set (0.004 sec)

12-MariaDB [practice]> SELECT books.title, loans.borrower
    -> FROM books
    -> INNER JOIN loans ON books.id = loans.book_id;
+------------------+----------+
| title            | borrower |
+------------------+----------+
| the great gatsby | mahmoud  |
| clean code       | ahmed    |
| 1984             | sara     |
+------------------+----------+
3 rows in set (0.004 sec)

13-MariaDB [practice]> SELECT books.title, COUNT(loans.id) AS All_loans
    -> FROM books
    -> LEFT JOIN loans ON books.id = loans.book_id
    -> GROUP BY books.title;
+------------------+-----------+
| title            | All_loans |
+------------------+-----------+
| 1984             |         1 |
| clean code       |         1 |
| refactoring      |         0 |
| the great gatsby |         1 |
| the hobbit       |         0 |
+------------------+-----------+
5 rows in set (0.058 sec)

14-MariaDB [practice]> SELECT books.title FROM books LEFT JOIN loans ON books.id = loans.book_id
    -> WHERE loans.id IS NUll;
+-------------+
| title       |
+-------------+
| the hobbit  |
| refactoring |
+-------------+
2 rows in set (0.002 sec)

15-
