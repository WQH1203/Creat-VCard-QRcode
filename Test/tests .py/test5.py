import mysql.connector

# 登录
mysql_connection = mysql.connector.connect(host="localhost",
                                           # user=input("Enter username: "),
                                           user="root",
                                           # password=input("Enter password: "),
                                           password="sbv2004",
                                           database="python_db"  # 直接连接到数据库
                                           )

cursor = mysql_connection.cursor()
# 创建python_db数据库
# cursor.execute("CREATE DATABASE python_db;")

# 查看mysql数据库
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print(db)

# 在python_db数据库创建Tabel
create_table_01 = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""

create_table_02 = """

CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""

create_table_03 = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""

# cursor.execute(create_table_01)
# cursor.execute(create_table_02)
# cursor.execute(create_table_03)


# 查看movies表格的信息
# cursor.execute("DESCRIBE movies")
# result = cursor.fetchall()
# for row in result:
#     print(row)

# 修改movies表格中collection_in_mil的架构
alter_table_query = """
ALTER TABLE movies
MODIFY COLUMN collection_in_mil DECIMAL(4,1)
"""
# cursor.execute(alter_table_query)

# 删除ratings表格
# cursor.execute("DROP TABLE ratings")

# 在movies表格插入
sql_01 = "INSERT INTO movies (title, release_year, genre, collection_in_mil) VALUES (%s, %s, %s, %s)"
insert_movies_query = [
    ["Forrest Gump", 1994, "Drama", 330.2],
    ["3 Idiots", 2009, "Drama", 2.4],
    ["Eternal Sunshine of the Spotless Mind", 2004, "Drama", 34.5],
    ["Good Will Hunting", 1997, "Drama", 138.1],
    ["Skyfall", 2012, "Action", 304.6]
]
# for insert_aux in insert_movies_query:
#     cursor.execute(sql_01, insert_aux)

#  或者

insert_movies_query_01 = """
INSERT INTO movies (title, release_year, genre, collection_in_mil)
VALUES
    ("HP", 1994, "Drama", 330.2)
"""

# cursor.execute(insert_movies_query_01)

#  或者

insert_reviewers_query = """
INSERT INTO reviewers
(first_name, last_name)
VALUES ( %s, %s )
"""
reviewers_records = [
    ("Chaitanya", "Baweja"),
    ("Mary", "Cooper"),
    ("John", "Wayne")
]

# cursor.executemany(insert_reviewers_query, reviewers_records)

#  或者

insert_ratings_query = """
INSERT INTO ratings
(rating, movie_id, reviewer_id)
VALUES ( %s, %s, %s)
"""
ratings_records = [
    (6.4, 1, 3), (5.6, 2, 2), (6.3, 3, 2), (5.1, 2, 1),
    (5.0, 4, 3)
]

# cursor.executemany(insert_ratings_query, ratings_records)

# 读取movies表格数据
# cursor.execute("SELECT * FROM movies LIMIT 5") # LIMIT 用来限制行数的
# result = cursor.fetchall()
# print(result)
# for row in result:
#     print(row)


# cursor.execute("SELECT title, release_year FROM movies LIMIT 5")
# for row in cursor.fetchall():
#     print(row)

# 过滤movies表格的结果
select_movies_query = """
SELECT title, collection_in_mil
FROM movies
WHERE collection_in_mil > 300
ORDER BY collection_in_mil DESC
"""
# cursor.execute(select_movies_query)
# for movie in cursor.fetchall():
#     print(movie)

select_movies_query_01 = """
SELECT CONCAT(title, " (", release_year, ")"),
      collection_in_mil
FROM movies
ORDER BY collection_in_mil DESC
"""
# cursor.execute(select_movies_query_01)
# for movie in cursor.fetchmany(size=5):
#     print(movie)
# cursor.fetchall()

# 处理多个表格

select_movies_query_02 = """
SELECT title, AVG(rating) as average_rating
FROM ratings
INNER JOIN movies
    ON movies.id = ratings.movie_id
GROUP BY movie_id
ORDER BY average_rating DESC
LIMIT 5
"""
# cursor.execute(select_movies_query_02)
# for movie in cursor.fetchall():
#     print(movie)

select_movies_query_03 = """
SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
FROM reviewers
INNER JOIN ratings
    ON reviewers.id = ratings.reviewer_id
GROUP BY reviewer_id
ORDER BY num DESC
LIMIT 1
"""
# cursor.execute(select_movies_query_03)
# for movie in cursor.fetchall():
#     print(movie)

# 修改reviewers表格的记录
update_query = """
UPDATE
    ratings
SET
    movie_id = 6
WHERE
    movie_id = 2
"""
# cursor.execute(update_query)

# 删除
# 首先查看需要删除的东西再确认删除
select_movies_query_04 = """
SELECT title, id FROM movies
WHERE title = "Forrest Gump"
"""
# cursor.execute(select_movies_query_04)
# for movie in cursor.fetchall():
#     print(movie)
#
delete_query = "DELETE FROM  movies WHERE id = 3"
# cursor.execute(delete_query)
#
# cursor.execute(select_movies_query_04)
# for movie in cursor.fetchall():
#     print(movie)

mysql_connection.commit()
