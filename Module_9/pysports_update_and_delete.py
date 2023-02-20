



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




def show_players(cursor, title):

 # Inner Join 
     cursor.execute("SELECT player_id, first_name, last_name, team_name FROM players INNER JOIN teams ON players.team_id = teams.team_id")

 # Get the results
     players = cursor.fetchall()

     print("\n  -- {} --".format(title))

 # Display the results 
     for player in players:
         print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try:
     db = mysql.connector.connect(**config)

 # Get the object 
     cursor = db.cursor()

 # Player Query
     add_player = ("INSERT INTO players(first_name, last_name, team_id,player_id)"
                  "VALUES(%s, %s, %s,%s)")

 # Player data
     player_data = ("Lando", "Norris", 47,12)

 # Insert new record
     cursor.execute(add_player, player_data)


     db.commit()

 # Show all the records for the player
     show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

 # Update the new record
     update_player = ("UPDATE players SET team_id = 7, player_id = 12, first_name = 'Rose', last_name = 'Hamilton' WHERE first_name = 'Lando'")

     cursor.execute(update_player)

     show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

     delete_player = ("DELETE FROM players WHERE first_name = 'Rose'")

     cursor.execute(delete_player)

     show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

     input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:

     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
         print("  The supplied username or password are invalid")

     elif err.errno == errorcode.ER_BAD_DB_ERROR:
         print("  The specified database does not exist")

     else:
         print(err)

finally:
    db.close()
    