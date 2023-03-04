""" 
    Title: what_a_book.py
    Author: Professor Henry Le
    Date: 27 February 2023
    Description: WhatABook program; Console program that interfaces with a MySQL database
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Example enter: 1 for book listing>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):
    # inner join query 
    _cursor.execute("SELECT book_id, book_name, author, details from books")

    # get the results from the cursor object 
    books = _cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    
    # iterate over the player data set and display the results 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from stores")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

def validate_users():
    """ validate the users ID """

    try:
        user_id = int(input('\n      Enter a customer id <Example 1 for user_id 1>: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_account_menu():
    """ display the users account menu """

    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Remove Book\n        4. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))

        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_wishlists(_cursor, _user_id):
    """ query the database for a list of books added to the users wishlist """

    _cursor.execute("SELECT users.user_id, users.first_name, users.last_name, books.book_id, books.book_name, books.author, books.details " + 
                    "FROM wishlists " + 
                    "INNER JOIN users ON wishlists.user_id = users.user_id " + 
                    "INNER JOIN books ON wishlists.book_id = books.book_id " + 
                    "WHERE users.user_id = {}".format(_user_id))
    
    wishlists = _cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlists:
        print("  Book ID: {}\n  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[3], book[4], book[5], book[6]))


        
def show_books_to_remove(_cursor,_user_id):
    """ query the database for a list of books in the users wishlists """
    query = ("SELECT book_id, book_name, author, details "
            "FROM books "
            "WHERE book_id IN (SELECT book_id FROM wishlists WHERE user_id = {})".format(_user_id))
    print(query)

    

def show_books_to_add(_cursor, _user_id):
    """ query the database for a list of books not in the users wishlists """

    query = ("SELECT book_id, book_name, author, details "
            "FROM books "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlists WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlists(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlists(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
    
def remove_book_from_wishlists(_cursor, user_id, book_id):
    """ Remove a book from a user's wishlist using the book_id. """

    # check if the user exists and has a wishlist
    _cursor.execute("SELECT * FROM wishlists WHERE user_id = {} AND book_id = {}".format(user_id, book_id))
    if not _cursor.fetchone():
        print("User with ID {} does not have book with ID {} in their wishlist.".format(user_id, book_id))
        return False
    
    # perform SQL query to remove the book from the wishlist
    _cursor.execute("DELETE FROM wishlists WHERE user_id = {} AND book_id = {}".format(user_id, book_id))
    print("Book with ID {} removed from user with ID {}'s wishlist.".format(book_id, user_id))
    return True

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config) # connect to the WhatABook database 

    cursor = db.cursor() # cursor for MySQL queries

    print("\n  Welcome to the WhatABook Application! ")

    user_selection = show_menu() # show the main menu 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            show_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            show_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_users()
            account_option = show_account_menu()

            # while account option does not equal 4
            while account_option != 4:

                # if the use selects option 1, call the show_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    show_wishlists(cursor, my_user_id)

                # if the user selects option 2, call the show_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    show_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlists(cursor, my_user_id, book_id)

                    db.commit() # commit the changes to the database 

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))
                    
                if account_option == 3:
                    
                    show_wishlists(cursor, my_user_id)
                    
                     # get the entered book_id 
                    book_id = int(input("\n        Enter the id of the book you want to remove: "))
                    
                    #remove books 
                    remove_book_from_wishlists(cursor, my_user_id,book_id)
                    

                # if the selected option is less than 0 or greater than 4, display an invalid user selection 
                if account_option < 1 or account_option > 4:
                    print("\n      Invalid option, please retry....")

                # show the account menu 
                account_option = show_account_menu()
        
        # if the user selection is less than 0 or greater than 5, display an invalid user selection
        if user_selection < 1 or user_selection > 4:
            print("\n      Invalid option, please retry...")
            
        # show the main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
    
    
  
