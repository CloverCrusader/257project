import psycopg2

def main():
        conn = psycopg2.connect(
                host="localhost",
                port=5432,  
                database="rapaczs", # your sterns account
                user="rapaczs", # your sterns username
                password="chip979bond") # your low security password
        
        # check for succesful connection, abort on faliure
        if conn is not None:
                print( "Connection Worked!" )
        else:
                print( "Problem with Connection" )
                conn.close()
                return None

def Carleton():
        conn = psycopg2.connect(
                host="localhost",
                port=5432,  
                database="rapaczs", # your sterns account
                user="rapaczs", # your sterns username
                password="chip979bond") # your low security password
        cur = conn.cursor()
             # sql = "SELECT city FROM table WHERE city = 'Northfield'"
        Carleton = "SELECT acceptrate FROM schoolstats WHERE school = 'Carleton'"
        cur.execute( Carleton )
        row = cur.fetchone()

        return (row)
 #"SELECT MIN(school) FROM schoolstats WHERE school = 'Carleton'"    
print (Carleton())
