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
        Carleton = "SELECT acceptrate FROM schoolstats WHERE school = 'Carleton College'"
        # test = "SELECT * FROM schoolstats" 
        cur.execute( Carleton )
        row = cur.fetchone()[0]

        return row
 #"SELECT MIN(school) FROM schoolstats WHERE school = 'Carleton'"    
def cost():
        conn = psycopg2.connect(
                host="localhost",
                port=5432,  
                database="rapaczs", # your sterns account
                user="rapaczs", # your sterns username
                password="chip979bond") # your low security password
        cur = conn.cursor()
      
        test = "SELECT school FROM financialaid" 
        cur.execute( test )
        row = cur.fetchone()[0]

        return row
print (Carleton())
print (cost())
