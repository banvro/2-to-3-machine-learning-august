import mysql.connector

con = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "evening")

cuerser = con.cursor()

# if con.is_connected():
#     print("you are connect")

# cuerser.execute("insert into env values('kriss', 'kriss@gmail.com', '923469343');")

# con.commit()


cuerser.execute("select * from env;")
# cuerser.execute("update env set Name = 'oris' where Name = 'moris';")

zx = cuerser.fetchall()
print(zx)
# con.commit()
