import MySQLdb

db = MySQLdb.connect(user="root",passwd="root",db="Texter")
cur = db.cursor()

def matrix_insert_one(mId, rowNo, colNo, val):
    sql = """
        INSERT INTO matrices (matrixId, rowNo, colNo, cellValue, created_at)
        VALUES (%s,%s,%s,%s,now())
    """
    cur.execute(sql % (mId, rowNo, colNo, val))


def get_full_matrix(mId):
    sql = """
        SELECT * FROM matrices WHERE matrixId = %s
    """
    cur.execute(sql % mId)
    return cur.fetchall()
    

def remove_full_matrix(mId):
    sql = """
        DELETE FROM matrices WHERE mId = %s
    """
    cur.execute(sql % mId)


