from django.db import connection

def getTypeDetails(ptype) :
    
    query = """ SELECT id FROM reading_types WHERE reading_type=%s """
    cursor = connection.cursor()
    cursor.execute(query,(ptype,))

    return cursor.fetchone()