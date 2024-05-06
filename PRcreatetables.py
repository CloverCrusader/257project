import psycopg2

def main():
        # connect to server
        conn = psycopg2.connect(
                host="localhost",
                port=5432,  
                database="rapaczs",
                user="rapaczs",
                password="chip979bond")
        
        # check for successful connection, abort on faliure
        if conn is not None:
                print( "Connection Worked!" )
        else:
                print( "Problem with Connection" )
                conn.close()
                return None
              
        cur = conn.cursor()
        
        # table creation parameters
        sql = """DROP TABLE IF EXISTS financialAid; 
                CREATE TABLE financialAid (
                    state text, 
                    school text, 
                    f0to30grand real, 
                    f30to48grand real, 
                    f48to75grand real,
                    f75to110grand real,
                    f110grandup real); 
                DROP TABLE IF EXISTS schoolStats; 
                CREATE TABLE schoolStats (
                    state text, 
                    school text, 
                    tuition real, 
                    acceptrate real, 
                    gradrate real,
                    popmajor text);"""
            
        cur.execute( sql )

        # copy information from titleless CSV files into tables
        sql = "\copy financialAid FROM 'financialAid.csv' DELIMITER ',' CSV"
        cur.execute( sql )

        sql = "\copy schoolStats FROM 'schoolStats.csv' DELIMITER ',' CSV"
        cur.execute( sql )

        # close connection to server
        cur.close()
        conn.close()

        return None

# run main
if __name__ == "__main__":
        main()
