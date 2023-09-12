# mysql connect package
# pip  --> conda
import pymysql

# connect Mysql
# ip, port, username, password, databass name
ip = 'localhost'
port = 3306
username = 'yojulab'
password = '!yojulab*'
databass = 'db_cars'

# editor - statement
connect = pymysql.connect(host=ip, user=username, password=password,
                          database=databass, port=port)

# make select statement
sql_query = 'SELECT * FROM db_cars.car_infors;'
#  execute select query
import pandas

# return resultset and then display
df = pandas.read_sql(sql=sql_query, con=connect)
# close
connect.close()

pass