


#import statements 
import mysql.connector
from mysql.connector import errorcode

#Database config object
config = {
    "user": "root",
    "password" : "Loverson#696",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

#Connection test code 
try:
    db =mysql.connector.connect(**config)
    print ("\n  Database user {} connected to MYSQL on host {} with database {}".format(config['user'], config['host'], config['database']))
    input ("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print (" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)
    
finally:
    db.close ()
    


