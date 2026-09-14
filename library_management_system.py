#library_management_system
import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

class Book:
    def __init__(self,title , author , year , status = bool):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
class Library:
    def __init__(self):
        pass
    def addBook(self , book):
        query = "INSERT INTO books (title , author , year , status) VALUES (? , ? , ? , ?)"
        parametr = (book.title , book.author , book.year , book.status)
        cursor.execute(query , parametr)
        connection.commit()
    def showBooks(self):
        query = "SELECT * FROM books"
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            print("there is not any book")
        else:
            for row in result:
                print(row)
        
    def search(self , title):
        query = "SELECT * FROM books WHERE title = ?"
        cursor.execute(query , (title,))
        result = cursor.fetchall()
        if not result:
            print("not found anything")
        else:
            for row in result:
                print(row)
    def edit(self):
        pass
    def delete(self , title , author):
        query = "DELETE FROM books WHERE title = ? AND author = ?"
        parametrs = (title , author)
        cursor.execute(query , parametrs)
        result = cursor.fetchone()
        if not result:
            print("there is not this book")
        else:
            connection.commit()
            print("deleted")
  

    
cursor.close()
connection.close()       
