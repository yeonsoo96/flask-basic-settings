import psycopg2 as pg2


conn_string = "host='localhost' dbname ='postgres' user='postgres' password='root'"
conn = pg2.connect(conn_string)

(date1, ranking1, score1, press1, title1, link1)='9999-12-31',1,1,1,1,1
cur = conn.cursor()
# cur.execute(
#     "CREATE TABLE mytest (nid SERIAL PRIMARY KEY, press_date DATE, ranking INTEGER, score INTEGER, press TEXT, title TEXT, link TEXT, creation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
# conn.commit()

# cur.execute("INSERT INTO mytest (press_date, ranking, score, press, title, link) VALUES (%s, %s, %s, %s, %s, %s)",
#             (date1, ranking1, score1, press1, title1, link1))

conn.commit()
cur.execute("SELECT nid, press_date, ranking, press, link FROM mytest WHERE nid=1 order by press_date, ranking;")
result = cur.fetchall()


print(result)