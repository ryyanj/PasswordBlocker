# import pymysql.cursors
# import pymysql

# cnx = pymysql.connect(user='root', password='1234',
#                               host='127.0.0.1',
#                               database='PasswordBlock')
# cursor = cnx.cursor()

# def getCurrentTime():
# 	cursor.execute('SELECT UNIX_TIMESTAMP()')
# 	row = cursor.fetchone()
# 	return row[0]

# def getStopTime():
# 	cursor.execute('SELECT stop_time from time')
# 	row = cursor.fetchone()
# 	return row[0]

# def getPassword():
# 	cursor.execute('SELECT password from time')
# 	row = cursor.fetchone()
# 	return row[0]

# def updateStopTime(newStopTime):
# 	sqlQuery = 'UPDATE time SET stop_time=' + str(newStopTime) + 'WHERE identifier=' + '88'
# 	cursor.execute(sqlQuery)

# def updatePassword(password):
# 	sqlQuery = 'UPDATE time SET password=' + "\"" + str(password) + "\"" + ' WHERE identifier=' + '88'
# 	cursor.execute(sqlQuery)


#cnx.close()