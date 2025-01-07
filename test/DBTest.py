import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "client",
    passwd = "raspi",
    database= "iot_trafo_client")
cursor = db.cursor()

sql = "SELECT * FROM transformer_data"

#cursor.execute(sql)
#trafoSetting = cursor.fetchall()[0]
#print(trafoSetting)

def gatherValues():
    cursor = db.cursor()
    sql = "SELECT * FROM reading_data ORDER BY data_id DESC LIMIT 1"
    cursor.execute(sql)
    result = cursor.fetchall()
    listResult = list(result[0])
    listResult.pop(0)
    listResult.pop(0)
    db.commit()
    return listResult

print(gatherValues())
