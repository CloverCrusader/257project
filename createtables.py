import psycopg2

def main():
        conn = psycopg2.connect(
                host="localhost",
                port=5432,  

                # please update the following with your own information :

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
              
        cur = conn.cursor()
        
        # table creation parameters
        sql = """DROP TABLE IF EXISTS financialaid; 
                CREATE TABLE financialaid (
                    state text, 
                    school text, 
                    f0to30grand real, 
                    f30to48grand real, 
                    f48to75grand real,
                    f75to110grand real,
                    f110grandup real);  
                DROP TABLE IF EXISTS schoolstats; 
                CREATE TABLE schoolstats (
                    state text, 
                    school text, 
                    tuition real, 
                    acceptrate real, 
                    gradrate real,
                    popmajor text);"""
            
        cur.execute( sql )

        # # copy information from titleless CSV files into tables
        # sql = "\copy financialaid FROM 'financialaid.csv' DELIMITER ',' CSV"
        # cur.execute( sql )

        # sql = "\copy schoolstats FROM 'schoolstats.csv' DELIMITER ',' CSV"
        # cur.execute( sql )

        # close connection to server
        cur.close()
        conn.close()

        return None

# run main
if __name__ == "__main__":
        main()
