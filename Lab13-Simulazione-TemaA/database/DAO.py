from database.DB_connect import DBConnect
from model.State import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnnoConAvvistamenti():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select year(s.`datetime`) as y, count(*) as a
                   from sighting s
                   group by year(s.`datetime`) """
        cursor.execute(query)
        for row in cursor:
            result.append((row["y"],row["a"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * from state s  """
        cursor.execute(query)
        for row in cursor:
            result.append(
                State(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select distinct s.state 
                from sighting s 
                where year(s.`datetime`) = %s"""
        cursor.execute(query,(anno,))
        for row in cursor:
            result.append(row['state'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(stato1,stato2,anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ select s1.state as s1 , s2.state as s2
                    from sighting s1 , sighting s2
                    where year(s1.`datetime`) = year(s2.`datetime`) 
                    and s1.state = %s 
                    and s2.state = %s 
                    and year(s2.`datetime`) = %s
                    and s1.`datetime` < s2.`datetime` """
        cursor.execute(query, (stato1,stato2,anno,))
        for row in cursor:
            result.append((row['s1'],row['s2']))
        cursor.close()
        conn.close()
        return result






