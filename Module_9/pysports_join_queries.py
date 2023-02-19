



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

#Establishing Connection 
try:
    db =mysql.connector.connect(**config)
    
    cursor = db.cursor()

     # inner join query 
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM players INNER JOIN teams ON players.team_id = teams.team_id")

     # get the results 
    players = cursor.fetchall()

    print("\n  -- DISPLAYING PLAYER RECORDS -- ")

    for player in players:
         print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:

     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("  The supplied username or password are invalid")

     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("  The specified database does not exist")

     else:
         print(err)
    


